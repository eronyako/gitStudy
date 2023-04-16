#!/usr/bin/env python
""" gitStudy.basic.info

"""
import sys
import platform


def getinfo():
    return {
        "python_ver": sys.version,
        "node": platform.node(),
        "system": platform.system(),
        "arch": platform.architecture(),
        "argv": sys.argv,
    }
