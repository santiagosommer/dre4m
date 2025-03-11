"""
This module configures the logging for the application.
"""
# Imports
import os
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
import logging

# From imports
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Get the logging level from an environment variable, DEBUG as default
log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()

# Validate the logging level
valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
if log_level not in valid_log_levels:
    log_level = 'DEBUG'
    logging.warning(
        "Invalid LOG_LEVEL environment variable. Defaulting to DEBUG.")

# Configure logging
logging.basicConfig(
    filename='dre4m-backend.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    level=getattr(logging, log_level, logging.DEBUG)
)

# Add a console handler for showing logs in the console
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, log_level, logging.DEBUG))
console_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

# Create a logger
logger = logging.getLogger('dre4m-backend')

if __name__ == '__main__':
    pass
