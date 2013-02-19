#!/usr/bin/env python2.7
'''
Created on Feb 1, 2013

@author: fahrstuhl
'''
import os.path
import datetime


import page
import config
import diarium


def nameFromFilename(fileName):
    fileNameSplit = os.path.splitext(fileName)
    if(fileNameSplit[1] == config.fileExtension):
        return fileNameSplit[0]
    return None


def makeNameList():
    nameList = list()
    for textFile in os.listdir(config.journalPath):
        pageName = nameFromFilename(textFile)
        if(pageName == None):
            continue
        nameList.append(pageName)
    return nameList


def makeNameListFromDate(fromDate, tilDate):
    nameList = list()
    fromDate = diarium.makeDate(fromDate)
    tilDate = diarium.makeDate(tilDate)
    for textFile in os.listdir(config.journalPath):
        pageName = nameFromFilename(textFile)
        if(pageName == None):
            continue
        try:
            pageDate = diarium.makeDate(pageName)
        except ValueError:
            continue
        if(pageDate >= fromDate and pageDate <= tilDate):
            nameList.append(pageName)
    return nameList


def searchTag(tag, nameList):
    findings = list()
    for pageName in nameList:
        searching = page.Page(pageName)
        finding = searching.getEntriesWithTag(tag)
        if(finding != []):
            firstLine = [searching.firstLine()]
            firstLine.extend(finding)
            findings.append(firstLine)
    return findings


def search(tag, fromDate=None, tilDate=None):
    if(not fromDate and not tilDate):
        nameList = makeNameList()
    else:
        if(not fromDate):
            fromDate = diarium.makeDateString(datetime.datetime(1900, 1, 1))
        elif(not tilDate):
            tilDate = diarium.makeDateString(datetime.datetime(datetime.MAXYEAR, 1, 1))
        nameList = makeNameListFromDate(fromDate, tilDate)
    findings = searchTag(tag,nameList)
    return findings


def printFindings(tags, fromDate, tilDate):
    for page in search(tags, fromDate, tilDate):
        for entry in page:
            print(entry)

def externalPrintFindings(args):
    printFindings(args.tags, args.fromDate, args.tilDate)


if __name__ == "__main__":
    import argparse
    argumentParser = argparse.ArgumentParser(description="Search for journal entries by tags.")
    argumentParser.add_argument("tags", help="Comma separated tags to look for.")
    argumentParser.add_argument("-f", "--fromDate", help="Search for tags in pages from this date on.")
    argumentParser.add_argument("-t", "--tilDate", help= "Search for tags in pages until this date.")
    args = argumentParser.parse_args()
    #printFindings(args.tags, args.fromDate, args.tilDate)
