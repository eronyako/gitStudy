#!/usr/bin/env python
""" gitStudy.basic.test_info

"""
from basic import *


class TestInfo(object):
    def test_getinfo(self):
        ret = info.getinfo()
        assert len(ret) == 5
