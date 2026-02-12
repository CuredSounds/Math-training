import logging
import os
from datetime import datetime

class Logger:
    _instance = None

    def __new__(cls, log_file="logs/app.log", level=logging.INFO):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(log_file, level)
        return cls._instance

    def _initialize(self, log_file, level):
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir) and log_dir:
            os.makedirs(log_dir)

        # Create logger
        self.logger = logging.getLogger("MathApp")
        self.logger.setLevel(level)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

# Usage: log = Logger().get_logger()
