'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import ConfigParser
import os.path


#TODO: Configparser
config = ConfigParser.SafeConfigParser()
if(config.read('config.txt') == []):
    raise 
dateFormat = config
timeFormat = "%H:%M:%S"
fileExtension = ".txt"
#TODO: Create path on first run
journalPath = os.path.expanduser("~/journal")
editor = "/usr/bin/gvim --nofork"
reader = editor

class Error(Exception):
    