'''
Created on Jan 28, 2013

@author: fahrstuhl
'''
import unittest
import os

import page
import config


class Test(unittest.TestCase):

    def setUp(self):
        self.page = page.Page("Test")
        self.taggedEntry = "12:34:56 alpha, beta, gamma  \n Lorem Ipsum\nDolor Sit Amet\n"
        self.untaggedEntry = "13:33:37\nMore Lorem Ipsum\n"
        self.singleTaggedEntry = "10:04:00 beta  \n Muspi Muspi\noO(Head in the clouds)\n"
        self.page.write(self.taggedEntry)
        self.page.write(self.untaggedEntry)
        self.page.write(self.singleTaggedEntry)

    def testFileName(self):
        self.assertEqual("{0}/{1}{2}".format(config.journalPath, self.page.name, config.fileExtension), self.page.filename)

    def testWriteAndRead(self):
        self.assertEqual(self.page.getEntries(), [self.taggedEntry, self.untaggedEntry, self.singleTaggedEntry])
        self.assertEqual(self.page.getText(), "# Test\n" + self.taggedEntry
                         + self.untaggedEntry
                         + self.singleTaggedEntry)

    def testTagSearch(self):
        bothTagged = [self.taggedEntry, self.singleTaggedEntry]
        self.assertEqual(self.page.getEntriesWithTag("alpha, beta", exact=False), bothTagged)
        self.assertEqual(self.page.getEntriesWithTag("alpha, beta", exact=True), [self.taggedEntry])
        self.assertEqual(self.page.getEntriesWithTag("beta", exact=True), bothTagged)

    def tearDown(self):
        os.remove(self.page.filename)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
