from requests_wework.api.address import Address


class TestAdress:
    def setup(self):
        self.address = Address()

    def test_create(self):
        print(self.address.create('zhangsan','张三','13599990000'))

    def test_update(self):
        print(self.address.update('zhangsan','李四','13355556666'))

    def test_delete(self):
        print(self.address.delete('zhangsan'))