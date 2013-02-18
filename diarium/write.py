#! /usr/bin/env python2
'''
Created on Jan 27, 2013

@author: fahrstuhl
'''

import diarium
import config
import page


global pageName, globalTags, globalContent, globalQuiet
globalQuiet = False
globalContent = ""
globalTags = ""
pageName = diarium.getDate()
time = diarium.getTime()


def setTime(timeToSet):
    global time
    time = timeToSet


def setPage(name):
    global pageName
    pageName = name


def setTags(givenTags):
    global globalTags
    globalTags = givenTags


def setContent(givenContent):
    global globalContent
    globalContent = givenContent


def setQuiet(value):
    global globalQuiet
    globalQuiet = value


def prepareEntry(tags=None):
    if(tags == None):
        return ""
    entry = "\n{} {}  \n".format(time, tags)
    return entry


def prepareContent(content=None):
    if(content == None):
        return ""
    content = "{}\n".format(content)
    return content


def write(name=None, tags=None, content=None, quiet=None):
    if(name == None):
        global pageName
        name = pageName
    if(tags == None):
        global globalTags
        tags = globalTags
    if(content == None):
        global globalContent
        content = globalContent
    if(quiet == None):
        global globalQuiet
        quiet = globalQuiet
    f = page.Page(name)
    f.write(prepareEntry(tags))
    f.write(prepareContent(content))
    if(not quiet):
        f.openWith(config.editor)


if __name__ == "__main__":
    import argparse
    argumentParser = argparse.ArgumentParser(description="Write new journal entry")
    argumentParser.add_argument("-d", "--date",
                            help="Date or name of page to edit")
    argumentParser.add_argument("-t", "--tags", help="Comma separated tags of entry")
    argumentParser.add_argument("-c", "--content", help="Content of entry")
    argumentParser.add_argument("-q", "--quiet", action="store_true", help="Don't open editor")
    args = argumentParser.parse_args()
    if args.date:
        setPage(args.date)
    if args.tags:
        setTags(args.tags)
    if args.content:
        setContent(args.content)
    if args.quiet:
        setQuiet(args.quiet)
    write()
