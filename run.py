# -*- coding: utf-8 -*-

#from test_case import test_suite
import unittest
from public import mypool
from public import report
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    print "Start automation  test......"

    # 删除原先的测试文件
    test_dir = "./test_case/"

    report.remove_report()

    parttern_dic = []
    parttern_dic.append("")

    discover_list = []

    temp = ["TestMath1.py", "TestMath2.py"];
    threadCount = len(temp)

    for pattern_str in temp:
        dic = (None,{'start_dir': test_dir, 'pattern': pattern_str})
        discover_list.append(dic)
    pool = mypool.MyPool(unittest.defaultTestLoader.discover, threadCount, discover_list)
    result_list = pool.run()
    flag = 0
    #保持测试报告中只有一个"测试报告"字样
    for discover_res in result_list:
         runner = report.save_file(flag)
         runner.run(discover_res)
         flag = flag + 1







