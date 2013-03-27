'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import sys
if(sys.version[0] == '3'):
    import configparser as ConfigParser
else:
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


def firstRun():
    config.add_section("journal")
    config.set("journal", "dateFormat", "%Y-%m-%d")
    config.set("journal", "timeFormat", "%H:%M:%S")
    config.set("journal", "journalPath", "~/journal")
    config.set("journal", "fileExtension", ".txt")
    config.set("journal", "reader", "/usr/bin/gvim --nofork")
    config.set("journal", "editor", "/usr/bin/gvim --nofork")
    with open(configFile, "w") as filePointer:
        config.write(filePointer)
    print("""
    Hi,
    it seems like this is your first run of diarium.
    Before you can start, please open
    {0}
    in a texteditor and set up the commands for your editor and reader and
    maybe customize your journal directory or whatever else you'd like to change.
    """.format(configFile))
    sys.exit()

config = ConfigParser.RawConfigParser({
                                    "dateFormat": "%Y-%m-%d",
                                    "timeFormat": "%H:%M:%S",
                                    "journalPath": "~/journal",
                                    "fileExtension": ".txt",
                                    })
configDir = appdirs.user_data_dir("diarium")
if(not os.path.exists(configDir)):
    os.mkdir(configDir)
configFile = os.path.join(configDir, "config.ini")
if(not os.path.exists(configFile)):
    firstRun()

configFiles = list()
configFiles.append(configFile)
if(config.read(configFiles) == []):
    raise ConfigFileNotFoundAt(configFiles)

dateFormat = config.get("journal", "dateFormat")
timeFormat = config.get("journal", "timeFormat")
fileExtension = config.get("journal", "fileExtension")
journalPath = config.get("journal", "journalPath")
journalPath = os.path.expanduser(journalPath)
editor = config.get("journal", "editor")
reader = config.get("journal", "reader")
if(not os.path.exists(journalPath)):
    os.mkdir(journalPath)
