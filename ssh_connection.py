import paramiko
from base_connector import BaseConnector


class SshConnection(BaseConnector):
    def __init__(self):
        self.client = None

    def connect(self):
        """Establish an SSH connection"""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, username=self.username, password=self.password)

    def execute_commands(self, command):
        """Execute a command via SSH"""
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close_connection(self):
        """Close SSH connection"""
        self.client.close()
