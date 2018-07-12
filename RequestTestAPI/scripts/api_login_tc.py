# coding:utf-8

import unittest
from po.LoginAPI import LoginAPI
from libs.ShareModules import GetIniFileData_P


class TestRegisterAPI(unittest.TestCase):
    u"""登录接口测试"""

    def setUp(self):
        self.file_path = './data/loginAPI_test_data.ini'
        print(self)

    def test_login_success_001(self):
        u"""登录成功验证"""
        data = GetIniFileData_P(self.file_path, 'test_login_success_001', 'input_data')
        error_code = GetIniFileData_P(self.file_path, 'test_login_success_001', 'expect_result_error_code')['error_code']
        r = LoginAPI(**data)
        self.assertEqual(r['error_code'],error_code)



    def test_login_username_error_002(self):
        u"""错误用户名"""
        data = GetIniFileData_P(self.file_path, 'test_login_username_error_002', 'input_data')
        error_message = GetIniFileData_P(self.file_path, 'test_login_username_error_002', 'expect_result_error_message')['error_message']
        r = LoginAPI(**data)
        # self.assertEqual(r['error_message'], error_message)
        self.assertNotEqual(r['error_message'], error_message)

if __name__ == '__main__':

    unittest.main()


