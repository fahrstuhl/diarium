'''
Created on Jan 26, 2013

@author: fahrstuhl
'''
import datetime


import config


if __name__ == '__main__':
    pass


time = datetime.datetime.strftime(datetime.datetime.today(), config.timeFormat)
date = datetime.datetime.strftime(datetime.datetime.today(), config.dateFormat)


def getDate():
    date = datetime.datetime.strftime(datetime.datetime.today(), config.dateFormat)
    return date


def getTime():
    time = datetime.datetime.strftime(datetime.datetime.today(), config.timeFormat)
    return time


def makeDate(givenDate):
    try:
        return datetime.datetime.strptime(givenDate, config.dateFormat)
    except ValueError:
        #print("Date format doesn't match")
        raise

def makeDateString(givenDate):
    return datetime.datetime.strftime(givenDate, config.dateFormat)
