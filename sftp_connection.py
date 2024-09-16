from abc import ABC

import paramiko
from base_connector import BaseConnector


class SftpConnection(BaseConnector):
    def __init__(self):
        self.client = None
        self.sftp = None

    def connect(self):
        """Establish an SSH connection"""
        self.client = paramiko.sftp_client()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.username, self.password)
        self.sftp = self.client.open_sftp()

    def execute_commands(self, command):
        """SFTP doesn't directly support command execution, so this function could handle file operations"""
        raise NotImplementedError("SFTP is for file transfer. Use SSH for command execution.")

    def upload_file(self, local_file, remote_file):
        """Upload a file via SFTP"""
        self.sftp.put(local_file, remote_file)

    def download_file(self, remote_file, local_file):
        """Download a file via SFTP"""
        self.sftp.get(remote_file, local_file)

    def close_connection(self):
        """Close SSH connection"""
        self.sftp.close()
        self.client.close()
