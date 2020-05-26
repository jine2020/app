import pytest,yaml
from qyweixin.public.initialization import Start


class TestAddmember():
    """企业微信添加/删除成员测试"""
    def setup_class(self):
        self.app = Start()
        self.main = self.app.start().main()
    def setup(self):
        pass
    def teardown(self):
        try:
            self.app.go_back()
        except:
            pass
    def teardown_class(self):
        self.app.close()

    @pytest.mark.parametrize('name,email,address',yaml.safe_load(open("../data/data.yml",encoding='utf-8'))['data'])
    def test_add_member(self,name,email,address):
        """测试添加成员"""
        text = self.main.news().mainlist().add_member().inputname(name=name).choicesex().inputemail(email=email) \
            .choiceaddress().choiceaddress(address=address).choiceidentity().identity().add_manually().toast_text()
        assert '添加成功' in text

    @pytest.mark.parametrize('name', yaml.safe_load(open("../data/data.yml", encoding='utf-8'))['deldata'])
    def test_del_member(self,name):
        """测试删除成员"""
        textlist=self.main.news().findandclickmenber(name=name).information().editmember().delmenber().fiandmenber(name=name)
        assert "True" in textlist


if __name__ == '__main__':
    pytest.main(['-vs'])
