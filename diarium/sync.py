'''
Created on Mar 25, 2013

@author: fahrstuhl
'''


import filecmp
import shutil
import os.path
import tempfile

import search
import page
import config


class Sync:

    def __init__(self, remoteDir, localDir):
        self.remoteDir = remoteDir
        self.localDir = localDir

    def copyMissingFiles(self, twoWay):
        for each in search.makeNameList(self.dirDiff.left_only):
            shutil.copy(os.path.join(self.dirDiff.left, each + config.fileExtension), self.dirDiff.right)
        if twoWay:
            for each in search.makeNameList(self.dirDiff.right_only):
                shutil.copy(os.path.join(self.dirDiff.right, each + config.fileExtension), self.dirDiff.left)

    def syncDifferentFiles(self, twoWay):
        for name in search.makeNameList(self.dirDiff.diff_files):
            self.syncPage(name, twoWay)

    def syncPage(self, name, twoWay):
        fromPage = self.makePage(self.dirDiff.left, name)
        toPage = self.makePage(self.dirDiff.right, name)
        entryList = self.mergeEntries(fromPage, toPage)
        replacement = self.createReplacementPage(name, entryList)
        shutil.copy(replacement.filename, toPage.filename)
        if twoWay:
            shutil.copy(replacement.filename, fromPage.filename)
        os.remove(replacement.filename)

    def mergeEntries(self, fromPage, toPage):
        entrySet = set()
        self.cleanNewlinesAndAdd(entrySet, fromPage)
        self.cleanNewlinesAndAdd(entrySet, toPage)
        entryList = list(entrySet)
        entryList.sort()
        return entryList

    def cleanNewlinesAndAdd(self, entrySet, cleanPage):
        for entry in cleanPage.getEntries():
            entrySet.add(entry.rstrip("\n"))

    def createReplacementPage(self, name, contentList):
        replacementFile = tempfile.mkstemp()
        replacementPage = page.Page(name=name, filename=replacementFile[1])
        replacementPage.create()
        for each in contentList:
            replacementPage.write("\n" + each + "\n")
        return replacementPage

    def makePage(self, path, name):
        filename = os.path.join(path, name + config.fileExtension)
        newPage = page.Page(name=name, filename=filename)
        return newPage

    def oneWaySync(self):
        self.copyMissingFiles(twoWay=False)
        self.syncDifferentFiles(twoWay=False)

    def twoWaySync(self):
        self.copyMissingFiles(twoWay=True)
        self.syncDifferentFiles(twoWay=True)

    def pull(self):
        self.dirDiff = filecmp.dircmp(self.remoteDir, self.localDir)
        self.oneWaySync()

    def push(self):
        self.dirDiff = filecmp.dircmp(self.localDir, self.remoteDir)
        self.oneWaySync()

    def merge(self):
        self.dirDiff = filecmp.dircmp(self.remoteDir, self.localDir)
        self.twoWaySync()


def merge(localDir, remoteDir):
    merge = Sync(localDir, remoteDir)
    merge.merge()


def extMerge(args):
    merge(args.remote, args.local)


def pull(fromDir, toDir):
    pull = Sync(fromDir, toDir)
    pull.pull()


def extPull(args):
    pull(args.remote, args.local)


def push(fromDir, toDir):
    push = Sync(fromDir, toDir)
    push.push()


def extPush(args):
    push(args.remote, args.local)
