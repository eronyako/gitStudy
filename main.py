#!/usr/bin/env python
""" gitStudy.main

"""
import sys
import platform
if __name__ == '__main__':
    print(f"Python {sys.version}")
    print(f"{platform.node()}: {platform.system()}, {platform.architecture()}")
    print(f"argv: {sys.argv}")

