import logging
import pytest
from logging.handlers import TimedRotatingFileHandler
from project_name.mylogger import init_logger, log_function_call, TRACE_LEVEL_NUM


# ----------------------------
# Fixtures
# ----------------------------
@pytest.fixture(autouse=True)
def init_test_logger(tmp_path):
    """
    Initialize the global logger for each test with TRACE level.
    Ensures handlers are closed after the test to avoid file locks on Windows.
    """
    # Initialize logger
    init_logger(
        app_name="test_app",
        log_dir=tmp_path,
        log_file="test.log",
        console_level=TRACE_LEVEL_NUM,  # TRACE
        file_level=TRACE_LEVEL_NUM,  # TRACE
        rotation="midnight",
        backup_count=3,
    )

    # Re-fetch the logger after initialization
    import project_name.mylogger as mylogger

    mylogger.logger = logging.getLogger("test_app")

    yield tmp_path

    # Cleanup: close all handlers
    for handler in mylogger.logger.handlers[:]:
        handler.close()
        mylogger.logger.removeHandler(handler)


# ----------------------------
# Tests
# ----------------------------
def test_trace_level_added():
    """TRACE level should exist on the logger."""
    import project_name.mylogger as mylogger

    assert hasattr(mylogger.logger, "trace")
    assert mylogger.logger.isEnabledFor(mylogger.TRACE_LEVEL_NUM)


def test_logger_writes_file(tmp_path):
    """Logger should write messages to the log file."""
    import project_name.mylogger as mylogger

    log_file = tmp_path / "test.log"

    mylogger.logger.info("Test info message", extra={"target": "file"})

    # Close handlers to safely read log file
    for handler in mylogger.logger.handlers[:]:
        handler.flush()
        handler.close()

    assert log_file.exists()
    content = log_file.read_text()
    assert "Test info message" in content


def test_logger_console_vs_file(tmp_path):
    import project_name.mylogger as mylogger

    # Send console message
    mylogger.logger.info("Console message", extra={"target": "console"})

    # Check console handler receives the message
    console_handlers = [
        h for h in mylogger.logger.handlers if getattr(h, "filter", None)
    ]
    found = False
    for handler in console_handlers:
        for f in handler.filters:
            if getattr(f, "__class__", None).__name__ == "ConsoleOnlyFilter":
                record = logging.LogRecord(
                    name="test",
                    level=logging.INFO,
                    pathname="",
                    lineno=0,
                    msg="Console message",
                    args=(),
                    exc_info=None,
                )
                record.target = "console"
                if f.filter(record):
                    found = True
    assert found


def test_log_function_call_decorator(tmp_path):
    """Decorator should log function entry and exit at TRACE level."""
    import project_name.mylogger as mylogger

    log_file = tmp_path / "test.log"

    @log_function_call
    def add(a, b):
        return a + b

    add(2, 3)

    # Close handlers before reading file
    for handler in mylogger.logger.handlers[:]:
        handler.flush()
        handler.close()

    content = log_file.read_text()
    assert "Entering add with args=(2, 3)" in content
    assert "add returned 5" in content


def test_timed_rotating_file_handler_rotation(tmp_path):
    """Simulate rollover and check that rotated files are created."""
    import project_name.mylogger as mylogger

    # Find the TimedRotatingFileHandler
    fh = None
    for handler in mylogger.logger.handlers:
        if isinstance(handler, TimedRotatingFileHandler):
            fh = handler
            break
    assert fh is not None, "TimedRotatingFileHandler not found"

    # Simulate rotation
    fh.doRollover()

    # Log after rollover
    mylogger.logger.info("After rollover", extra={"target": "file"})
