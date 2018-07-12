import requests
from libs.ShareModules import InsertLog_P


def LoginAPI(username=None,password=None,*args, **kwargs):

    try:
        url = "http://192.168.1.232/api/account/login/"

        s = requests.session()

        s.headers['Content-Type'] = 'application/json'
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        s.headers['Referer'] = 'http://192.168.1.232/login'

        ## 经过测试这两个字段可以不传,不影响调用
        # s.cookies['csrftoken'] = 'YuxpJCncI6WCUP5HqaS2cGp2rH211ffxs0IdXXgPzwc1aQ12emCsAc4z1qWkXssR'
        # s.cookies['userId'] = '146'

        data_tmp = {}
        if username!=None:
            data_tmp['employeeno'] = username
        if password!=None:
            data_tmp['password'] = password

        data = dict(data_tmp)
        data.update(kwargs)

        r = s.post(url=url, json=data)

        return r.json()

    except BaseException as msg:
        log = InsertLog_P()
        log.error(msg)

        return msg

if __name__ == '__main__':
    print()