import telnetlib
from base_connector import BaseConnector


class TelnetConnection(BaseConnector):
    def __init__(self):
        self.telnet = None

    def connect(self):
        """Establish a Telnet connection"""
        self.telnet = telnetlib.Telnet(self.host)
        self.telnet.read_until(b"login: ")
        self.telnet.write(self.username.encode('ascii') + b"\n")
        self.telnet.read_until(b"Password: ")
        self.telnet.write(self.password.encode('ascii') + b"\n")

    def execute_commands(self, command):
        """Execute a command via Telnet"""
        self.telnet.write(command.encode('ascii') + b"\n")
        return self.telnet.read_all().decode('ascii')

    def close_connection(self):
        """Close Telnet connection"""
        self.telnet.close()
