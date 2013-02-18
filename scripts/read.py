#!/usr/bin/env python2.7
'''
Created on Jan 27, 2013

@author: fahrstuhl
'''


from diarium import config
from diarium import page
from diarium import diarium


pageName = diarium.getDate()


def setPage(name):
    global pageName
    pageName = name


def read(name=None, filename=None):
    if(name == None):
        global pageName
        name = pageName
    f = page.Page(name, filename)
    f.openWith(config.reader)


if __name__ == "__main__":
    import argparse
    argumentParser = argparse.ArgumentParser(description="Write new journal entry")
    argumentParser.add_argument("-d", "--date",
                            help="Date or name of page to read.")
    args = argumentParser.parse_args()
    if args.date:
        setPage(args.date)
    read()
