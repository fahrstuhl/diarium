'''
Created on Jan 28, 2013

@author: fahrstuhl
'''
import unittest
import os
import re


import page


class Test(unittest.TestCase):

    def setUp(self):
        self.page = page.Page("Test")

    def testFileName(self):
        self.assertEqual("/home/fahrstuhl/journal/{}.txt".format(self.page.name), self.page.filename)

    def testWriteAndRead(self):
        testinhalt = "Testinhalt zum testen."
        self.page.write(testinhalt)
        self.assertEqual(self.page.getLines(), ["# Test\n", testinhalt])

    def testGetMatchingEntries(self):
        print(self.page.getMatchingEntries(["Test"], True))

    def tearDown(self):
        os.remove(self.page.filename)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()