class Equal:
    def equal(self, data1:list, demo:list):
        """断言Button """
        if data1[0] == demo[0]:
            assert data1[0] != demo[1], f'操作{demo[0]}没有成功'
        elif data1[0] == demo[1]:
            assert data1[0] != demo[0], f'操作取消{demo[1]}没有成功'
        else:
            raise

    def equaltoast(self, data1:list, demo:list, toast, text):
        """断言Toast"""
        if data1[0] == demo[0]:
            assert text[0] == toast[1], f'操作{toast[1]}没有成功'
        elif data1[0] == demo[1]:
            assert text[0] == toast[0], f'操作取消{toast[0]}没有成功'
        else:
            raise
