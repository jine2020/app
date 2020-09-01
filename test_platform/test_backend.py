from unittest import TestCase

from backend import db, User
from backend import TestCase as tcase


class TestUser(TestCase):
    def test_user(self):
        user1 = User(username='jine', password='123', email='jine11@126.com')
        db.session.add(user1)
        db.session.commit()


class TestTestCase(TestCase):
    def test_testcase(self):
        case1=tcase(name='验证测试平台数据',desc='登录平台后能够正确展现出全量数据',data='步骤加预期',
                    uid=1)
        db.session.add(case1)
        db.session.commit()
