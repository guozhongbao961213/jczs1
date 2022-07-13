import pytest


class Testlogin:

    def setup(self):
        print('每次执行前打开')

    def teardown(self):
        print('每次执行用例结束关闭')

    def setup_class(self):
        print('每一类用例执行前执行')

    def teardown_class(self):
        print('每一类用例执行后执行')

    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    def test_01_login(self, datebase_sql):
        print('测试百里')
        assert 2 == 2

    @pytest.mark.run(order=1)
    def test_02_login(self):
        print('测试函数')

    @pytest.mark.run(order=3)
    def test_03_login(self):
        print('测试小宝')

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_04_login(self):
        print('测试小邓')


if __name__ == '__main__':
    pytest.main([])
