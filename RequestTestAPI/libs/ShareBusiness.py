import requests
from libs.ShareModules import InsertLog_P

# -------------------------------------------------------------------------------
# ###############################################################################
# -------------------------------------------------------------------------------
# 函数/过程名称：Login_B
# 函数/过程的目的：登录系统获取token值
# 假设：无
# 影响：无
# 输入：无
# 返回值：登录成功token值（包含在返回的Cookies中）
# 创建者：王波
# 创建时间：2018/06/29
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def Login_B(username,password):
    try:
        s = requests.session()

        s.headers['Content-Type'] = 'application/json'
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        s.headers['Referer'] = 'http://192.168.1.232/login'

        ## 经过测试这两个字段可以不传,不影响调用
        # s.cookies['csrftoken'] = 'YuxpJCncI6WCUP5HqaS2cGp2rH211ffxs0IdXXgPzwc1aQ12emCsAc4z1qWkXssR'
        # s.cookies['userId'] = '146'

        url = "http://192.168.1.232/api/account/login/"

        data = {"employeeno": username, "password": password}

        r = s.post(url=url, json=data)

        return r.cookies['token']

    except BaseException as msg:
        log = InsertLog_P()
        log.error(msg)



if __name__ == '__main__':
    print(Login_B('wb','000000'))

