'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import os
import subprocess
import re


import config


class Page:

    def __init__(self, name, filename=None):
        self.name = name
        if(filename == None):
            self.filename = self.createFilename()
        else:
            self.filename = filename
        if(not os.path.exists(self.filename)):
            self.create()

    def write(self, content):
        with open(self.filename, "a") as page:
            page.write(content)

    def firstLine(self):
        return "# {}\n".format(self.name)

    def create(self):
        self.write(self.firstLine())

    def openWith(self, command):
        command = command.split(" ")
        try:
            subprocess.call((command[0], command[1], self.filename))
        except IndexError:
            subprocess.call((command[0], self.filename))

    def createFilename(self):
        filename = os.path.join(config.journalPath, str(self.name)
                                + str(config.fileExtension))
        return filename

    def getLines(self):
        with open(self.filename, "r") as page:
            return page.readlines()

    def findString(self, string):
        with open(self.filename, "r") as page:
            for line in page:
                if(string in line):
                    print(line)

    def getEntriesWithTag(self, tags, exact=True):
        tagList = tags.split(",")
        return self.getMatchingEntries(tagList, exact)

    def matchesAllTags(self, line, tags=[""]):
        return all(tag in line for tag in tags)

    def matchesAnyTags(self, line, tags=[""]):
        return any(tag in line for tag in tags)

    def isBeginningOfEntry(self, line):
        match = r"\d\d:\d\d:\d\d [\w ,]"
        regularExpression = re.compile(match, re.IGNORECASE)
        return regularExpression.match(line)

    def isExactlyWhatWeAreLookingFor(self, line, tags):
        return self.isBeginningOfEntry(line) and self.matchesAllTags(line, tags)

    def isPartlyWhatWeAreLookingFor(self, line, tags):
        return self.isBeginningOfEntry(line) and self.matchesAnyTags(line, tags)

    def extractEntryFromLines(self, lineList):
        entry = lineList[0]
        for part in lineList[1:]:
            if(self.isBeginningOfEntry(part)):
                break
            entry += part
        return entry

    def getMatchingEntries(self, tags, exact):
        entries = list()
        content = self.getLines()
        for i, line in enumerate(content):
            if((exact and self.isExactlyWhatWeAreLookingFor(line, tags)) or
               (not exact and self.isPartlyWhatWeAreLookingFor(line, tags))):
                entry = self.extractEntryFromLines(content[i:])
                entries.append(entry)
        return entries
