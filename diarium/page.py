'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import os
import subprocess
import re


import config


entryRegex = re.compile(r"(?P<time>\d\d:\d\d:\d\d)(?P<tags>.*)(\n|$)")


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
        return "# {0}\n".format(self.name)

    def create(self):
        self.write(self.firstLine())

    def openWith(self, command):
        command = command.split(" ")
        command.append(self.filename)
        subprocess.call(command)

    def createFilename(self):
        filename = os.path.join(config.journalPath, str(self.name)
                                + str(config.fileExtension))
        return filename

    def getLines(self):
        with open(self.filename, "r") as page:
            return page.readlines()

    def getText(self):
        with open(self.filename, "r") as page:
            return page.read()

    def findString(self, string):
        with open(self.filename, "r") as page:
            for line in page:
                if(string in line):
                    print(line)

    def getEntriesWithTag(self, tags, exact=True):
        tagList = list()
        for tag in tags.split(","):
            tagList.append(tag.strip())
        return self.getMatchingEntries(tagList, exact)

    def matchesAllTags(self, entry, tags=[""]):
        foundTags = entryRegex.match(entry).group("tags")
        return all(tag in foundTags for tag in tags)

    def matchesAnyTags(self, entry, tags=[""]):
        foundTags = entryRegex.match(entry).group("tags")
        return any(tag in foundTags for tag in tags)

    def extractEntryFromLines(self, lineList):
        entry = lineList[0]
        for part in lineList[1:]:
            if(entryRegex.match(part)):
                break
            entry += part
        return entry

    def getEntries(self):
        entries = list()
        content = self.getLines()
        for i, line in enumerate(content):
            if entryRegex.match(line):
                entry = self.extractEntryFromLines(content[i:])
                entries.append(entry)
        return entries

    def getMatchingEntries(self, tags, exact):
        entries = self.getEntries()
        result = list()
        for entry in entries:
            if((exact and self.matchesAllTags(entry, tags)) or
               not exact and self.matchesAnyTags(entry, tags)):
                result.append(entry)
        return result
