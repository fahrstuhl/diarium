'''
Created on Jan 27, 2013

@author: fahrstuhl
'''

import diarium
import config
import page


pageName = diarium.getDate()
time = diarium.getTime()


def prepareEntry(tags=None):
    if(not tags):
        tags = ""
    entry = "\n{0} {1}  \n".format(time, tags)
    return entry


def prepareContent(content=None):
    if(content == None):
        return ""
    content = "{0}\n".format(content)
    return content


def write(name=None, tags=None, content=None, quiet=None):
    if(not name):
        name = diarium.getDate()
    f = page.Page(name)
    f.write(prepareEntry(tags))
    f.write(prepareContent(content))
    if(not quiet):
        f.openWith(config.editor)

def externalWrite(args):
    write(args.date, args.tags, args.content, args.quiet)

