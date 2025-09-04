# src/project_name/main.py
import logging
import os
from project_name.mylogger import init_logger, logger, log_function_call


def configure_logging():
    env = os.getenv("APP_ENV", "dev").lower()

    if env == "dev":
        log_dir = "logs/dev"
        console_level = logging.DEBUG
        file_level = logging.DEBUG
    elif env == "test":
        log_dir = "logs/test"
        console_level = logging.INFO
        file_level = logging.DEBUG
    elif env == "stage":
        log_dir = "logs/stage"
        console_level = logging.WARNING
        file_level = logging.INFO
    elif env == "prod":
        log_dir = "logs/prod"
        console_level = logging.ERROR
        file_level = logging.INFO
    else:
        log_dir = "logs/other"
        console_level = logging.INFO
        file_level = logging.INFO

    init_logger(
        app_name="demo_app",
        log_dir=log_dir,
        log_file="app.log",
        console_level=console_level,
        file_level=file_level,
        rotation="midnight",
        backup_count=7,
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
