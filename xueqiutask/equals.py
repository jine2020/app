def equal(data1, data2, demo):
    if data1 == demo[0]:
        assert data1 != data2, f'操作{demo[0]}没有成功'
    elif data1 == demo[1]:
        assert data1 != data2, f'操作取消{demo[1]}没有成功'
