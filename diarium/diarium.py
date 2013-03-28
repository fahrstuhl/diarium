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


def convertDateString(date, originalFormat, convertedFormat = config.dateFormat):
    date = datetime.datetime.strptime(date, originalFormat)
    dateString = datetime.datetime.strftime(date, convertedFormat)
    return dateString


def convertTimeString(date, originalFormat, convertedFormat = config.timeFormat):
    time = datetime.datetime.strptime(time, originalFormat)
    timeString = datetime.datetime.strftime(time, convertedFormat)
    return timeString


def makeDate(givenDate):
    try:
        return datetime.datetime.strptime(givenDate, config.dateFormat)
    except ValueError:
        #print("Date format doesn't match")
        raise

def makeDateString(givenDate):
    return datetime.datetime.strftime(givenDate, config.dateFormat)
