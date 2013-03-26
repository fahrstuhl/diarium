'''
Created on Feb 6, 2013

@author: fahrstuhl
'''
import unittest
import page
import search
import write
import random
import string
import os


class Test(unittest.TestCase):

    def setUp(self):
        self.numberOfFiles = 100
        self.tagList = list()
        self.contentList = list()
        for j in range(10):
            self.tagList.append(''.join(random.choice(string.ascii_letters) for k in range(10)))
            self.contentList.append(''.join(random.choice(string.ascii_letters) for k in range(100)))
        for i in range(self.numberOfFiles):
            name = "test-{0}".format(i)
            for j in range(10):
                write.write(name, tags=str(j), content=str(i), quiet=True)
        write.write("0001-01-01", content="Start of datesearch", quiet=True)
        write.write("0015-01-01", content="Middle of datesearch", quiet=True)
        write.write("0031-01-01", content="End of datesearch", quiet=True)

    def testSingleTagSearch(self):
        tag = self.tagList[7]
        content = self.contentList[1]
        write.write("test-42", tags=tag, content=content, quiet=True)
        self.assertEquals(["# test-42\n", "{0} {1}  \n".format(write.time, tag) +
                           write.prepareContent(content)], search.search(tag)[0])

    def testMultiTagSearch(self):
        tags = "{0}, {1}, {2}".format(self.tagList[1], self.tagList[9], self.tagList[2])
        content = self.contentList[2]
        write.write("test-13", tags=tags, content=content, quiet=True)
        self.assertEquals(["# test-13\n", "{0} {1}  \n".format(write.time, tags) +
                           write.prepareContent(content)], search.search(tags)[0])

    def testMultiPageSearch(self):
        tag = self.tagList[5]
        content = self.contentList[0]
        write.write("test-1", tags=tag, content=content, quiet=True)
        write.write("test-99", tags=tag, content=content, quiet=True)
        expected = [["# test-1\n", "{0} {1}  \n".format(write.time, tag)
                      + write.prepareContent(content)],
                     ["# test-99\n", "{0} {1}  \n".format(write.time, tag)
                       + write.prepareContent(content)]]
        self.assertEquals(expected, search.search(tag))

    def testDateSearch(self):
        self.assertEquals([["# 0001-01-01\n", "{0}   \n".format(write.time)
                            + write.prepareContent("Start of datesearch")],
                           ["# 0015-01-01\n", "{0}   \n".format(write.time)
                            + write.prepareContent("Middle of datesearch")]],
                           search.search("", "0001-01-01", "0015-01-01"))
        self.assertEquals([["# 0001-01-01\n", "{0}   \n".format(write.time)
                            + write.prepareContent("Start of datesearch")],
                           ["# 0015-01-01\n", "{0}   \n".format(write.time)
                            + write.prepareContent("Middle of datesearch")],
                           ["# 0031-01-01\n", "{0}   \n".format(write.time)
                            + write.prepareContent("End of datesearch")]],
                           search.search("", "0001-01-01", "0031-01-01"))

    def tearDown(self):
        for i in range(self.numberOfFiles):
            name = "test-{}".format(i)
            os.remove(page.Page(name).filename)
        os.remove(page.Page("0001-01-01").filename)
        os.remove(page.Page("0015-01-01").filename)
        os.remove(page.Page("0031-01-01").filename)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
