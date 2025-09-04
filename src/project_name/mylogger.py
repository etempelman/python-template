# src/project_name/mylogger.py
import logging
from pathlib import Path
from functools import wraps
from logging.handlers import TimedRotatingFileHandler

# --- 1. Define TRACE level below DEBUG ---
TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")


def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kwargs)


logging.Logger.trace = trace  # Add trace method to all loggers

# --- 2. Filters for console/file routing ---
class ConsoleOnlyFilter(logging.Filter):
    def filter(self, record):
        return getattr(record, "target", "") == "console"


class FileOnlyFilter(logging.Filter):
    def filter(self, record):
        return getattr(record, "target", "") == "file"


# --- 3. Global logger ---
logger = logging.getLogger("default_logger")


# --- 4. Initialization method ---
def init_logger(
    app_name: str = "my_app",
    log_dir: str = "logs",
    log_file: str = "app.log",
    console_level: int = logging.INFO,
    file_level: int = logging.INFO,
    rotation: str = "midnight",
    backup_count: int = 7,
):
    """
    Initialize the global logger with console and file handlers.

    :param app_name: Name of the logger
    :param log_dir: Directory where log file will be saved
    :param log_file: Log file name
    :param console_level: Logging level for console handler (default INFO)
    :param file_level: Logging level for file handler (default INFO)
    :param rotation: When to rotate logs (e.g., "midnight", "H", "D", "W0")
    :param backup_count: Number of rotated log files to keep
    """
    global logger
    logger = logging.getLogger(app_name)
    logger.setLevel(TRACE_LEVEL_NUM)  # capture all levels including TRACE

    # Ensure log directory exists
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_path = Path(log_dir) / log_file

    # --- Console handler ---
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    ch.addFilter(ConsoleOnlyFilter())

    # --- Timed rotating file handler ---
    fh = TimedRotatingFileHandler(
        filename=log_path,
        when=rotation,          # "midnight" = rotate daily
        interval=1,             # rotate every interval
        backupCount=backup_count,  # keep N old logs
        encoding="utf-8"
    )
    fh.setLevel(file_level)
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    fh.addFilter(FileOnlyFilter())

    # Clear existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add handlers
    logger.addHandler(ch)
    logger.addHandler(fh)


# --- 5. Decorator to auto-log function calls at TRACE level ---
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.trace(f"Entering {func.__name__} with args={args}, kwargs={kwargs}", extra={"target": "file"})
        result = func(*args, **kwargs)
        logger.trace(f"{func.__name__} returned {result}", extra={"target": "file"})
        return result
    return wrapper
