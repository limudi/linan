#!/usr/bin/env python
# coding: utf8

import unittest
import HTMLTestRunner
import os
from test_001 import *

def test_suite():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),  # 表示获取当前路径
        pattern="test_*.py",  # 运行以test开头的所有文件
        top_level_dir=None
    )  # 默认参数
    return suite


def run():
    html = HTMLTestRunner.HTMLTestRunner(
        stream=open(r"C:\Users\samji\PycharmProjects\linan\report.html", "wb"),
        title="report",
        description="reporttest"
    )
    html.run(test_suite())

run()