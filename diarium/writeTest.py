'''
Created on Jan 27, 2013

@author: fahrstuhl
'''
import unittest
import write


class Test(unittest.TestCase):

    def testPrepareEntry(self):
        self.assertEquals("\n{0} public, private  \n".format(write.time),
                          write.prepareEntry("public, private"))
        self.assertEqual("\n{0}   \n".format(write.time), write.prepareEntry(""))

    def testPrepareContent(self):
        self.assertEquals("", write.prepareContent(None))
        self.assertEquals("Test\n", write.prepareContent("Test"))

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
