'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import ConfigParser
import os.path
import appdirs


class ConfigFileNotFoundAt(Exception):
    """Exception raised if the config file can not be found.

    Attributes:
        path -- path where the config file should have been
    """
    def __init__(self, path):
        self.path = path

    def __str__(self):
        self.str = "No config file found at \n"
        for i in self.path:
            str += i + "\n"
        return repr(self.str)

config = ConfigParser.ConfigParser()
configDir = appdirs.user_data_dir("diarium")
if(not os.path.exists(configDir)):
    os.mkdir(configDir)
configFile = os.path.join(configDir, "config.ini")
if(not os.path.exists(configFile)):
    config.add_section("journal")
    config.set("journal", "dateFormat", "%Y-%m-%d")
    config.set("journal", "timeFormat", "%H:%M:%S")
    config.set("journal", "journalPath", "~/journal")
    config.set("journal", "fileExtension", ".txt")
    config.set("journal", "reader", "/usr/bin/gvim --nofork")
    config.set("journal", "editor", "/usr/bin/gvim --nofork")
    with open(configFile, "w") as filePointer:
        config.write(filePointer)
configFiles = list()
configFiles.append(configFile)
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
