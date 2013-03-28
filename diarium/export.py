'''
Created on Mar 28, 2013

@author: fahrstuhl
'''

try:
    import markdown
except ImportError:
    pass

import search
import diarium
import page
import config


def export(tag, fromDate=None, tilDate=None):
    sR = search.search(tag, fromDate, tilDate)
    fE = list()
    for eL in sR:
        for entry in eL[1:]:
            fE.append([eL[0], entry])
    for i, entry in enumerate(fE):
        print("[{0}] {1}{2}".format(i, entry[0], entry[1]))
    choice = fE[int(raw_input("Choose entry to export: "))]
    return choice


def exportToNikola(entry):
    #Hrm... Maybe import nikola or something?
    date = entry[0]
    date = diarium.convertDateString(date, config.dateFormat, "%Y/%m/%d")
    entry = page.entryRegex.match(entry[1])
    tags = entry.group("tags")
    time = entry.group("time")
    time = diarium.convertTimeString(time, config.timeFormat, "%H:%M:%S")
    title = raw_input("Title: ")


def extExport(args):
    exported = export(args.tags, args.fromDate, args.tilDate)
    exported = exported[0] + exported[1]
    if args.outFile:
        with open(args.outFile, "w") as f:
            f.write(exported)
    else:
        print(exported)
