#!/usr/bin/python
import ConfigParser, os

class ConfigLoader():
    def __init__(self,configfile):
        self.load_config(configfile)
        self.token         = self.config.get('ACCOUNT','TOKEN')
        self.version       = self.config.get('ACCOUNT','VERSION')
        self.host          = self.config.get('ACCOUNT','HOST')
        self.namebot       = self.config.get('ACCOUNT','NAMEBOT')
        self.nameproject   = self.config.get('ACCOUNT','NAMEPROJECT')
        self.log_path      = self.config.get('LOGGER','LOG_PATH')
        self.log_file_name = self.config.get('LOGGER','LOG_FILE_NAME')
        self.pid_file      = self.config.get('PID','FILE')

    def load_config(self,configfile):
        self.config = ConfigParser.ConfigParser()
        self.config.read(configfile)

    def get_log_path_file(self):
        return os.path.join(os.getcwd(),self.log_path) + self.log_file_name

    def get_pid_path_file(self):
        return os.path.join(os.getcwd(), self.pid_file)