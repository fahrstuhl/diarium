'''
Created on Jan 26, 2013

@author: fahrstuhl
'''
from time import localtime, strftime, strptime


import config


if __name__ == '__main__':
    pass


time = strftime(config.timeFormat, localtime())
date = strftime(config.dateFormat, localtime())


def getDate():
    date = strftime(config.dateFormat, localtime())
    return date


def getTime():
    time = strftime(config.timeFormat, localtime())
    return time


def checkDate(givenDate):
    try:
        strptime(givenDate, config.dateFormat)
    except ValueError:
        print("Date format doesn't match")
        raise
