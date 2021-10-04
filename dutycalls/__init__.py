import logging
from logging import NullHandler

try:
    # The import might fail when importing __version__ from setup.py
    from .client import Client
except ImportError:
    pass

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())

__version__ = '0.4.0'
