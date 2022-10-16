import logging

from .message import Message
from .client import Client


logging.getLogger(__name__).addHandler(logging.NullHandler())
