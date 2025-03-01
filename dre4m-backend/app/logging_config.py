# Imports
import os
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
import logging

# From imports
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the logging level from an environment variable, DEBUG is the default
log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()


# Configure logging
logging.basicConfig(
    filename='dre4m-backend.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    level=getattr(logging, log_level, logging.DEBUG)
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    pass
