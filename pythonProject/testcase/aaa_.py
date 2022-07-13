import pytest
import time


class Testlogin:
    @pytest.mark.run(order=5)
    def test_01_login(self):
        time.sleep(5)
        print('测试百里')

    @pytest.mark.run(order=1)
    def test_02_case(self):
        time.sleep(5)
        print('测试函数')

    @pytest.mark.run(order=3)
    def test_03_login(self):
        time.sleep(5)
        print('测试百里')

    @pytest.mark.run(order=2)
    def test_04_case(self):
        time.sleep(5)
        print('测试函数')




