import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.path import CASEPATH,REPORTFILE

def run():
    suite = unittest.TestSuite()
    cases = unittest.defaultTestLoader.discover(CASEPATH)
    # print(cases)
    for case in cases:
        suite.addTest(case)
    f = open(REPORTFILE,'wb')
    runner = HTMLTestRunner(f,verbosity=1,title=u'测试报告',description=u'测试用例执行情况：')
    runner.run(suite)
    f.flush()
    f.close()


run()

