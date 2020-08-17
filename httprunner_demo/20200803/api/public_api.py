import configparser
import json
import os

import yaml


def get_path():
    #获取项目地址
    namepath=os.path.abspath(os.path.dirname(__file__))
    projectpath=namepath[:namepath.find("20200803\\")]+"20200803\\"
    return projectpath

config = configparser.ConfigParser()
config_path = get_path() + '\conf\conf.ini'
config.read(config_path, encoding='utf8')
api_data_path=get_path()+'\data\\api_data.yml'


class PublicApi():

    def get_conf(self,param:str):
        #获取配置文件信息
        try:
            value=config.get('conf',param)
        except :
            raise
        return value

    def get_url(self):
        with open(api_data_path) as f:
            _value=yaml.safe_load(f)['default']
        with open(api_data_path) as f:
            value=yaml.safe_load(f)['env'][_value]
            return value

    def get_api_data(self,param:str):
        with open(api_data_path) as f:
            value=yaml.safe_load(f)[param]
            return value


if __name__ == '__main__':
    p=PublicApi().get_url()
    print(p)

