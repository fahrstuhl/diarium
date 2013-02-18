'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import ConfigParser
import os.path


class ConfigFileNotFoundAt(Exception):
    """Exception raised if the config file can not be found.

    Attributes:
        path -- path where the config file should have been
    """
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "No config file found at " + self.path

configFiles = list()
codeDirectory = os.path.dirname(__file__)
configFiles.append(os.path.join(codeDirectory, "config.txt"))
config = ConfigParser.SafeConfigParser()
if(config.read(configFiles) == []):
    raise ConfigFileNotFoundAt(configFiles)
dateFormat = config.get("journal", "dateFormat", "raw")
timeFormat = config.get("journal", "timeFormat", "raw")
fileExtension = config.get("journal", "fileExtension")
#TODO: Create path on first run
journalPath = config.get("journal", "journalPath", "raw")
journalPath = os.path.expanduser(journalPath)
editor = config.get("journal", "editor")
reader = config.get("journal", "reader")
