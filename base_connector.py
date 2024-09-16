from abc import ABC, abstractmethod


class BaseConnector(ABC):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    @abstractmethod
    def connect(self):
        """Method to establish a connection"""
        pass

    @abstractmethod
    def execute_commands(self, command):
        """Execute a command on the remote server"""
        pass

    @abstractmethod
    def close_connection(self):
        """Close the connection"""
        pass
