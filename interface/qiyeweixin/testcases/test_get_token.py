import pytest
import yaml

from interface.qiyeweixin.api.get_token import GetToken


class TestToken:
    def setup(self):
        self.gettoken=GetToken()
    @pytest.mark.parametrize('data',yaml.safe_load(open('../api/get_token_data.yml')))
    def test_get_token(self,data):
        assert self.gettoken.get_token(data).json()['errcode']==0
