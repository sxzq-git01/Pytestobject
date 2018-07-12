import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import copy
from libs.ShareModules import GetSkipScripts_P
from libs.ShareModules import GetSkipTestCases_P
from libs.ShareModules import InsertLog_P
from libs.ShareModules import GetNewReport_P
from libs.ShareModules import SendEmail_P


#获取不需要执行的模块名称
ConfigFilePath = "./config.xlsx"
m = GetSkipScripts_P(ConfigFilePath)

#获取不需要执行的用例名称
TestCasePath = './testcase/测试用例.xlsx'
t = GetSkipTestCases_P(TestCasePath)

def get_test_suite(discover):
    #筛选出并去除不需要执行的脚本
    suite_m = copy.deepcopy(discover)
    for i in range(len(m)):
        for j in range(discover._tests.__len__()):
            d = discover._tests[j]
            if m[i] in str(d):
                suite_m._tests.remove(d)
    #筛选出并去除不需要执行的用例
    suite_c = copy.deepcopy(suite_m)
    for i in range(len(t)):
        for j in range(suite_m._tests.__len__()):
            s_m =  suite_m._tests[j]
            for z in range(s_m._tests.__len__()):
                s_c = s_m._tests[z]
                for k in range(s_c._tests.__len__()):
                    s_t = s_c._tests[k]
                    if t[i] == s_t._testMethodName:
                        suite_c._tests[j]._tests[z]._tests.remove(s_t)
    return suite_c


def run_tests():
    try:
        log = InsertLog_P()
        dirpath = './scripts'
        discover = unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')
        suite = get_test_suite(discover)
        currenttime = time.strftime('%y%m%d%H%M%S ')
        filedir = './reports/' + 'report' + currenttime + '.html'
        fp = open(filedir,'wb+')
        runner = HTMLTestRunner(stream=fp,title='系统API自动化测试报告',description='填写项目描述信息' )
        runner.run(suite)
        fp.close()
        # f = GetNewReport_P()
        # SendEmail_P('pythondldysl01@163.com','wxqcl258258','752175073@qq.com','smtp.163.com',f,25)
        log.info("脚本成功运行")
    except BaseException as msg:
        log.error(msg)

if __name__ == '__main__':
    run_tests()