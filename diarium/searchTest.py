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
            name = "test-{}".format(i)
            for j in range(10):
                write.write(name, tags=str(j), content=str(i), quiet=True)

    def testSingleTagSearch(self):
        tag = self.tagList[7]
        content = self.contentList[1]
        write.write("test-42", tags=tag, content=content, quiet=True)
        self.assertEquals(["# test-42\n", "{} {}  \n".format(write.time, tag) +
                           write.prepareContent(content)], search.searchTag(tag)[0])

    def testMultiTagSearch(self):
        tags = "{}, {}, {}".format(self.tagList[1], self.tagList[9], self.tagList[2])
        content = self.contentList[2]
        write.write("test-13", tags=tags, content=content, quiet=True)
        self.assertEquals(["# test-13\n", "{} {}  \n".format(write.time, tags) +
                           write.prepareContent(content)], search.searchTag(tags)[0])

    def testMultiPageSearch(self):
        tag = self.tagList[5]
        content = self.contentList[0]
        write.write("test-1", tags=tag, content=content, quiet=True)
        write.write("test-99", tags=tag, content=content, quiet=True)
        expected = [["# test-1\n", "{} {}  \n".format(write.time, tag)
                      + write.prepareContent(content)],
                     ["# test-99\n", "{} {}  \n".format(write.time, tag)
                       + write.prepareContent(content)]]
        self.assertEquals(expected, search.searchTag(tag))

    def tearDown(self):
        for i in range(self.numberOfFiles):
            name = "test-{}".format(i)
            os.remove(page.Page(name).filename)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
