import os

from pathlib import Path
from functools import cache

from structlog import get_logger
from jsonschematools.config import settings

logger = get_logger()


def initialize_storage():
    """Initialize the storage directory."""
    local_storage = settings.storage.local.path
    
    dirs = ["tmp"]
    dirs = [os.path.join(local_storage, d) for d in dirs]
    for dir in dirs:
        Path(dir).mkdir(parents=True, exist_ok=True)
        
    logger.info("Initialized storage directory", localpath=local_storage)


@cache
def setup_environment():
    """Create the necessary environment and resources for the application."""
    initialize_storage()
    logger.info("Environment setup completed")
    
