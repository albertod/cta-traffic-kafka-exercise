"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        data = json.loads(message.value())
        logger.info(f"Data: {data}")
        self.temperature = message["temperature"]
        self.status = message["status"]
