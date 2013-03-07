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

    def testFileName(self):
        self.assertEqual("/home/fahrstuhl/journal/{0}{1}".format(self.page.name, config.fileExtension), self.page.filename)

    def testWriteAndRead(self):
        testinhalt = "Testinhalt zum testen."
        self.page.write(testinhalt)
        self.assertEqual(self.page.getLines(), ["# Test\n", testinhalt])

    def tearDown(self):
        os.remove(self.page.filename)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
