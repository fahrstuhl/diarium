'''
Created on Mar 26, 2013

@author: fahrstuhl
'''
import unittest
import tempfile
import os
import filecmp

import write
import config
import page
import sync


class Test(unittest.TestCase):

    def setUp(self):
        self.localDir = tempfile.mkdtemp(suffix="local")
        self.remoteDir = tempfile.mkdtemp(suffix="remote")
        config.journalPath = self.localDir
        self.localContent = ["tag1, tag2, tag3", "LoremIpsum\nDolorSit amet\nLOCAL\nLOCAl"]
        self.sharedContent = ["tag2, tag4", "Share the Lorem Ipsum\nShare IT!"]
        self.remoteContent = ["tag4, tag5", "Remote\nStuff"]
        write.write(name="1900-01-01", tags=self.localContent[0], content=self.localContent[1], quiet=True)
        write.write(name="1841-01-01", tags=self.sharedContent[0], content=self.sharedContent[1], quiet=True)
        config.journalPath = self.remoteDir
        write.write(name="1841-01-01", tags=self.sharedContent[0], content=self.sharedContent[1], quiet=True)
        write.write(name="1841-01-01", tags=self.remoteContent[0], content=self.remoteContent[1], quiet=True)
        write.write(name="1800-01-01", tags=self.remoteContent[0], content=self.remoteContent[1], quiet=True)
        write.write(name="1900-01-01", tags=self.remoteContent[0], content=self.remoteContent[1], quiet=True)

    def tearDown(self):
        for i in ["1900-01-01", "1841-01-01", "1800-01-01"]:
            try:
                os.remove(os.path.join(self.localDir, i + config.fileExtension))
            except:
                pass
            try:
                os.remove(os.path.join(self.remoteDir, i + config.fileExtension))
            except:
                pass
        os.rmdir(self.localDir)
        os.rmdir(self.remoteDir)

    def testPush(self):
        oneWaySync = sync.Sync(self.remoteDir, self.localDir)
        oneWaySync.push()
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).right_only, [])
        with open(os.path.join(self.remoteDir, "1900-01-01" + config.fileExtension)) as f:
            self.assertTrue(self.localContent[0] in f.read())

    def testPull(self):
        oneWaySync = sync.Sync(self.remoteDir, self.localDir)
        oneWaySync.pull()
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).left_only, [])
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).diff_files, ["1900-01-01" + config.fileExtension])

    def testMerge(self):
        merge = sync.Sync(self.remoteDir, self.localDir)
        merge.merge()
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).left_only, [])
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).right_only, [])
        self.assertEqual(filecmp.dircmp(self.remoteDir, self.localDir).diff_files, [])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
