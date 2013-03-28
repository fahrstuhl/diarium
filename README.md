diarium
=======

A simple journal: A place to dump your brain just one command away.

## Goals
- Quickly accessible  
  Done: Only one command to an editor with the current page and time  
  Done: Convenient setup with pip or something
- Simple and human readable  
  Done: Simple plaintext files written in markdown  
  Done: Easier configuration and sane default values  
  ToDo: Documentation
- Tags and search  
  Done: Entries can be tagged  
  Done: Search for one or more tags  
  Done: Search before, after or inbetween dates  
  ToDo: Search only in specific page
  ToDo: Open search result in viewer
- Cross platform  
  Done: Linux  
  Working: Pandora  
  Untested: Windows, Mac OS X, other desktop os  
  ToDo: Android  
- Encryption  
  ToDo: GPG encryption  
  Working: Container encryption like Truecrypt, encfs or ecryptfs  
- Synchronisation  
  Done: Internal (local) merge tool  
  ToDo: Merge over ssh/rsync/ftp  
  Working: SCM like git  
  Working: Remote merge over sshfs/ftpfs
- Information separation for publishing  
  Done: Information can be separated by tag search  
  Working: Search returns parsable markdown  
  Working: Export single entry based on tag search  
  ToDo: Export multiple entries based on tag search  
  ToDo: Parse exported entries
  ToDo: Use Python's markdown module to search and export in one go  

## Setup
- (Python 2.6 only) install [argparse](http://pypi.python.org/pypi/argparse)
- install [appdirs](http://pypi.python.org/pypi/appdirs)
- install diarium
- run diarium once
- set a command for your favorite texteditor  
  make sure it runs in foreground and doesn't fork and detach. Gvim needs the --nofork flag for example. Consult the manual of your favorite texteditor for more information
- set a command for your favorite textreader or reuse your editor
- run diarium -h

- (optional) set a different path to your journal
- (optional) set a different date- and timeformat
  see [Python's strftime function](http://docs.python.org/2/library/time.html#time.strftime)
- (optional) set a file extension like .txt, .md, .journal or .whatever. Don't leave it blank.

## File format
``` markdown
# filename without extension

time comma, separated, tags  (two spaces to get a <br \> after parsing the markdown)
As much content as your filesystem allows.

Also new lines and stuff.

time tags, for new, entry  (tags can be multiple words, just separate the tags with commas)
more content
```
My __2013-02-18.txt__ file for example:
``` markdown
# 2013-02-18

05:11:40 public, example  
It's really hard to come up with example text.

05:13:16 example, public  
Really hard.
```
