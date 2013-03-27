'''
Created on Mar 25, 2013

@author: fahrstuhl
'''


import difflib
import filecmp
import shutil
import os.path
import tempfile

import page
import config


class Sync:

    def __init__(self, remoteDir, localDir):
        self.remoteDir = remoteDir
        self.localDir = localDir

    def copyMissingFiles(self, dirDiff):
        for each in dirDiff.left_only:
            shutil.copy(os.path.join(dirDiff.left, each), dirDiff.right)

    def syncDifferentFiles(self, dirDiff):
        for each in dirDiff.diff_files:
            self.syncPage(each)

    def syncPage(self, name):
        fromPage = self.makePage(self.dirDiff.left, name)
        toPage = self.makePage(self.dirDiff.right, name)
        self.mergeEntries(fromPage, toPage)

    def mergeEntries(self, fromPage, toPage):
        entrySet = set()
        self.cleanNewlinesAndAdd(entrySet, fromPage)
        self.cleanNewlinesAndAdd(entrySet, toPage)
        entryList = list(entrySet)
        entryList.sort()
        self.replacePage(toPage, entryList)

    def cleanNewlinesAndAdd(self, entrySet, cleanPage):
        for entry in cleanPage.getEntries():
            entrySet.add(entry.rstrip("\n"))

    def replacePage(self, updatePage, entryList):
        replacement = self.createReplacementPage(updatePage.name, entryList)
        shutil.copy(replacement.filename, updatePage.filename)
        os.remove(replacement.filename)

    def createReplacementPage(self, name, contentList):
        replacementFile = tempfile.mkstemp()
        replacementPage = page.Page(name=name, filename=replacementFile[1])
        replacementPage.create()
        for each in contentList:
            replacementPage.write("\n" + each + "\n")
        return replacementPage

    def makePage(self, path, name):
        filename = os.path.join(path, name)
        name = os.path.splitext(name)[0]
        newPage = page.Page(name=name, filename=filename)
        return newPage

    def oneWaySync(self):
        self.copyMissingFiles(self.dirDiff)
        self.syncDifferentFiles(self.dirDiff)

    def pull(self):
        self.dirDiff = filecmp.dircmp(self.remoteDir, self.localDir)
        self.oneWaySync()

    def push(self):
        self.dirDiff = filecmp.dircmp(self.localDir, self.remoteDir)
        self.oneWaySync()

    def merge(self):
        self.pull()
        self.push()
