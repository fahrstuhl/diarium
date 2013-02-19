#!/usr/bin/env python2.7
'''
Created on Jan 27, 2013

@author: fahrstuhl
'''


import config
import page
import diarium


pageName = diarium.getDate()


def setPage(name):
    global pageName
    pageName = name


def read(name=None, filename=None):
    if(not None):
        global pageName
        name = pageName
    f = page.Page(name, filename)
    f.openWith(config.reader)

def externalRead(args):
    read(args.date)


if __name__ == "__main__":
    import argparse
    argumentParser = argparse.ArgumentParser(description="Read a page of your journal.")
    argumentParser.add_argument("-d", "--date",
                            help="Date or name of page to read.")
    args = argumentParser.parse_args()
    if args.date:
        setPage(args.date)
    #read()
