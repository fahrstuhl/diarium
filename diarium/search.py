#!/usr/bin/env python2
'''
Created on Feb 1, 2013

@author: fahrstuhl
'''
import os.path


import page
import config


#TODO: Suche nach mehreren Tags in verschiedenen Kombinationen
def nameFromFilename(fileName):
    fileNameSplit = os.path.splitext(fileName)
    if(fileNameSplit[1] == config.fileExtension):
        return fileNameSplit[0]
    return None


def searchTag(tag):
    findings = list()
    for textFile in os.listdir(config.journalPath):
        pageName = nameFromFilename(textFile)
        if(pageName == None):
            continue
        searching = page.Page(pageName)
        finding = searching.getEntriesWithTag(tag)
        if(finding != []):
            firstLine = [searching.firstLine()]
            firstLine.extend(finding)
            findings.append(firstLine)
    return findings


def printFindings(tag):
    for page in searchTag(tag):
        for entry in page:
            print(entry)


if __name__ == "__main__":
    import argparse
    argumentParser = argparse.ArgumentParser(description="Search for journal entries by tags.")
    argumentParser.add_argument("tags", help="Comma separated tags to look for.")
    args = argumentParser.parse_args()
    printFindings(args.tags)