'''
Created on Feb 18, 2013

@author: fahrstuhl
'''
from distutils.core import setup

setup(
      name = 'diarium',
      packages = ['diarium'],
      version = '0.1',
      author = 'Gabriel Zoeller',
      author_email = "fahrstuhl@mailbox.tu-berlin.de",
      url = "https://github.com/fahrstuhl/diarium",
      description = '''A simple journal:
      A place to dump your brain one command away.''',
      classifiers = [
      'Programming Language :: Python :: 2.7',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Development Status :: 3 - Alpha',
      'Topic :: Office/Business :: News/Diary',
      ],
      scripts=['scripts/diarium'],
      )
