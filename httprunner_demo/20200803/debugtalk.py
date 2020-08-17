import time
from api.public_api import PublicApi
from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def conf(param: str):
    # 获取配置文件信息
    return PublicApi().get_conf(param)


def url():
    # 获取测试地址
    return PublicApi().get_url()

class ApiData():
    def api_data(self,param: str):
        # 获取api结构数据
        return PublicApi().get_api_data(param)


if __name__ == '__main__':
    print(ApiData().api_data("headers_get"))
