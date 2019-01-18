#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import HTMLTestRunner
import os
import time


def save_file(flag):
    # 确定生成报告的路径
    #case_path = os.path.join(os.getcwd())
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), 'report')
    # html报告文件路径
    exist = os.path.exists(report_path)
    if not exist:
        os.mkdir(report_path, 1)
    # 生成报告时间
    #report_time = time.strftime("%Y-%m-%d %H_%M_%S_", time.localtime())
    htmlFile = os.path.join(report_path, "testReport.html")
    fp = file(htmlFile, mode='ab+')
    # 生成报告的Title,描述:测试报告  测试报告详情 test report Details of the test report
    #title='测试报告', description='测试报告详情'
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试详情')
    #保持报告中只有一个“测试报告”字样
    if flag != 0:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='', description='测试详情')
    return runner


def remove_report():
    report_path = os.path.join(os.getcwd(), 'report')
    # html报告文件路径
    exist = os.path.exists(report_path)
    # 目录不存在，直接返回
    if not exist:
        return
    else:
        htmlFile = os.path.join(report_path, "testReport.html")
        if os.path.isfile(htmlFile):
            os.remove(htmlFile)
