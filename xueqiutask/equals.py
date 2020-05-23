class Equal:
    def equal(self, data1, data2, demo,errortext):
        """断言Button """
        if data1 == demo[0]:
            assert data1 != data2, f'操作{demo[0]}没有成功'
        elif data1 == demo[1]:
            assert data1 != data2, f'操作取消{demo[1]}没有成功'
        else:
            raise (errortext)

    def equaltoast(self, data1, demo, demo1, text,errortext):
        """断言Toast"""
        if data1 == demo[0]:
            assert text == demo1[0], f'操作{demo1[0]}没有成功'
        elif data1 == demo[1]:
            assert text == demo1[1], f'操作取消{demo1[1]}没有成功'
        else:
            raise (errortext)
