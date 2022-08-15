import configparser
import os

class FoenixConfig:
    """Configuration data for the FoenixMgr. Exposes the foenix.ini file."""

    def __init__(self):
        """Attempt to read and process the config file."""
        config = configparser.ConfigParser()
        config.read(['foenix.ini', os.path.expandvars('$FOENIXHOME/foenix.ini'), os.path.expanduser('~/foenix.ini')])

        self._flash_size = int(config['DEFAULT'].get('flash_size', '524288'), 10)
        self._port = config['DEFAULT'].get('port', 'COM3')
        self._chunk_size = int(config['DEFAULT'].get('chunk_size', '4096'), 10)
        self._data_rate = int(config['DEFAULT'].get('data_rate', '6000000'), 10)
        self._label_file = config['DEFAULT'].get('labels', 'basic8')
        self._address = config['DEFAULT'].get('address', '380000')
        self._timeout = int(config['DEFAULT'].get('timeout', '60'), 10)

    def flash_size(self):
        """Return the required size of the flash binary file in bytes."""
        return self._flash_size

    def chunk_size(self):
        """Return the size of the data packet that gets sent over the debug port."""
        return self._chunk_size

    def data_rate(self):
        """Return the data rate in bits per second that the serial port should use."""
        return self._data_rate

    def port(self):
        """Return the name of the port to use to connect to the debug port."""
        return self._port

    def label_file(self):
        """Return the name of the label file."""
        return self._label_file

    def address(self):
        """Return the address (in hex) to use in loading the flash file."""
        return self._address

    def timeout(self):
        """Return the timeout to allow for serial communications (in seconds)."""
        return self._timeout
