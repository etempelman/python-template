# src/project_name/main.py
import logging
import os
from dotenv import load_dotenv
from project_name.mylogger import init_logger, logger, log_function_call

def configure_logging():
    # Load .env file (if exists)
    load_dotenv()

    # Read environment from .env or system env
    env = os.getenv("APP_ENV", "dev").lower()
    log_dir = os.getenv("LOG_DIR", f"logs/{env}")
    log_file = os.getenv("LOG_FILE", "app.log")

    # Environment-specific log levels
    if env == "dev":
        console_level = logging.DEBUG
        file_level = logging.DEBUG
    elif env == "test":
        console_level = logging.INFO
        file_level = logging.DEBUG
    elif env == "stage":
        console_level = logging.WARNING
        file_level = logging.INFO
    elif env == "prod":
        console_level = logging.ERROR
        file_level = logging.INFO
    else:
        console_level = logging.INFO
        file_level = logging.INFO

    # Initialize logger
    init_logger(
        app_name="demo_app",
        log_dir=log_dir,
        log_file=log_file,
        console_level=console_level,
        file_level=file_level,
        rotation="midnight",  # daily rotation
        backup_count=7,       # keep 7 days
    )

    logger.info(f"Application started in {env} mode", extra={"target": "console"})


@log_function_call
def add(x, y):
    return x + y


def main():
    configure_logging()
    result = add(2, 3)
    logger.info(f"Result = {result}", extra={"target": "console"})


if __name__ == "__main__":
    main()
