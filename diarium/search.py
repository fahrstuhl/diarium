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


def makeNameList(fromList):
    nameList = list()
    for textFile in fromList:
        pageName = nameFromFilename(textFile)
        if(pageName == None):
            continue
        nameList.append(pageName)
    nameList.sort()
    return nameList


def makeNameListFromDate(fromDate, tilDate, fromList):
    nameList = list()
    fromDate = diarium.makeDate(fromDate)
    tilDate = diarium.makeDate(tilDate)
    for textFile in fromList:
        pageName = nameFromFilename(textFile)
        if(pageName == None):
            continue
        try:
            pageDate = diarium.makeDate(pageName)
        except ValueError:
            continue
        if(pageDate >= fromDate and pageDate <= tilDate):
            nameList.append(pageName)
    nameList.sort()
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
    dirList = os.listdir(config.journalPath)
    if(not fromDate and not tilDate):
        nameList = makeNameList(dirList)
    else:
        if(not fromDate):
            fromDate = diarium.makeDateString(datetime.datetime(datetime.MINYEAR, 1, 1))
        elif(not tilDate):
            tilDate = diarium.makeDateString(datetime.datetime(datetime.MAXYEAR, 1, 1))
        nameList = makeNameListFromDate(fromDate, tilDate, dirList)
    findings = searchTag(tag, nameList)
    return findings


def printFindings(tags, fromDate, tilDate):
    for page in search(tags, fromDate, tilDate):
        for entry in page:
            print(entry)

def externalPrintFindings(args):
    printFindings(args.tags, args.fromDate, args.tilDate)
