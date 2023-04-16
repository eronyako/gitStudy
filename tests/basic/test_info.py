#!/usr/bin/env python
""" gitStudy.basic.test_info

"""
import unittest
from basic import info


class TestInfo(unittest.TestCase):
    def test_getinfo(self):
        ret = info.getinfo()
        self.assertEqual(len(ret), 5)
