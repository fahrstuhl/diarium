diarium
=======

A simple journal: A place to dump your brain just one command away.

## Goals
- Quickly accessible  
  Done: Only one command to an editor with the current page and time  
  ToDo: Convenient setup with pip or something
- Simple and human readable  
  Done: Simple plaintext files written in markdown  
  ToDo: Easier configuration  
  ToDo: Documentation
- Tags and search  
  Done: Entries can be tagged  
  Done: Search for one or more tags  
  ToDo: Search only on specific date or page  
  ToDo: Open search result in viewer
- Cross platform
  Done: Linux  
  Untested: Windows, Mac OS X, other desktop os  
  ToDo: Pandora, Android  
- Encryption  
  ToDo: GPG encryption  
  Working: Container encryption like Truecrypt, encfs or ecryptfs  
- Synchronisation  
  ToDo: Internal merge tool  
  Working: SCM like git
- Information separation for publishing  
  Done: Information can be separated by tag search  
  Working: Search returns parsable markdown  
  ToDo: Use Python's markdown module to search and export in one go  

## Setup
- open config.py
- set date- and timeformat
  see [Python's strftime function](http://docs.python.org/2/library/time.html#time.strftime)
- set a file extension like .txt, .journal or leave it blank
- set a path to your journal and create it manually (ToDo...)
- set a command for your favorite texteditor  
  make sure it runs in foreground and doesn't fork and detach. Gvim needs the --nofork flag for example. Consult the manual of your favorite texteditor for more information
- set a command for your favorite textreader or reuse your editor
- run write.py -h, read.py -h and search.py -h for an overview of the command line settings
- set up symlinks in your PATH or aliases in your shell

## File format
``` markdown
# filename without extension

time comma, separated, tags  (two spaces to get a <br \> after parsing the markdown)
As much content as your filesystem allows.

Also new lines and stuff.

time tags, for new, entry  (tags can be multiple words, just separate them by commas)
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
