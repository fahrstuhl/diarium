'''
Created on Mar 25, 2013

@author: fahrstuhl
'''


import filecmp
import shutil
import os.path
import tempfile
import sys

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
        fromDict = fromPage.getEntries(rstrip=True)
        toDict = toPage.getEntries(rstrip=True)
        entryList = self.mergeDicts(fromDict, toDict)
        entryList.sort()
        return entryList

    def dictKeyDifference(self, fromDict, toDict):
        if(sys.version[0:3] == '2.6'):
            return set(fromDict.keys()) - set(toDict.keys())
        else:
            return fromDict.viewkeys() - toDict.viewkeys()

    def dictItemIntersection(self, fromDict, toDict):
        if(sys.version[0:3] == '2.6'):
            return set(fromDict.items()) & set(toDict.items())
        else:
            return fromDict.viewitems() & toDict.viewitems()

    def dictItemDifference(self, fromDict, toDict):
        if(sys.version[0:3] == '2.6'):
            return set(fromDict.items()) - set(toDict.items())
        else:
            return fromDict.viewitems() - toDict.viewitems()

    def mergeDicts(self, fromDict, toDict):
        entryList = list()
        for key in self.dictKeyDifference(fromDict, toDict):
            entryList.append(fromDict.pop(key))
        for key in self.dictKeyDifference(toDict, fromDict):
            entryList.append(toDict.pop(key))
        for key, value in self.dictItemIntersection(fromDict, toDict):
            entryList.append(fromDict.pop(key))
            del toDict[key]
        for key, value in self.dictItemDifference(fromDict, toDict):
            entryList.append(self.resolveConflict(fromDict, toDict, key))
        return entryList

    def resolveConflict(self, fromDict, toDict, key):
        conflictingEntries = {"1": fromDict[key], "2": toDict[key]}
        conflictString = """The following two entries conflict:\n
[1]{0}:\n
{1}\n\n
[2]{2}\n
{3}\n
Please chose which version should be used: 
        """.format(self.dirDiff.left, conflictingEntries["1"], self.dirDiff.right, conflictingEntries["2"])
        choice = raw_input(conflictString)
        chosenEntry = conflictingEntries.pop(choice)
        return chosenEntry

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
