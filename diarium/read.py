'''
Created on Jan 27, 2013

@author: fahrstuhl
'''


import config
import page
import diarium


def read(name=None):
    if(not name):
        name = diarium.getDate()
    f = page.Page(name)
    f.openWith(config.reader)


def externalRead(args):
    read(args.date)
