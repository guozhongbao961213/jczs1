import pytest


@pytest.fixture(scope='function')
def datebase_sql():
    print('数据库查询')
    yield
    print('数据库关闭')

    # fixtrue 装饰器使用方法：

    # 固件写入conftest.py文件中
    # @pytest.fixture(scope='function', autoues= , ids='',name= '')  # ：指定部分用例前后执行，
    # def x():                                 # scope传参：function：函数 class：类 module：模块 package/session:会话
    #     print('数据库查询')                         # 需要在所有的函数前后执行：autoues传参中添加 autoues=True
    #     yield    # yield后为结束后执行              # ids:'数据驱动重命名参数名'
    #     print('数据库关闭')                        # name= '给fixture左右的函数重命名'

    # 作用于函数：
    # class Testlogin:
    #     def test_01_login(self, x):       # 固件名写在用例的传参中
    #         print('测试百里')
    #         assert 2 == 2

    # 作用于类：
    # @pytest.mark.uesfixtrues(x)           #函数前加装饰器，固件名写入传参中
    # class Testlogin:
    #     def test_01_login(self):
    #         print('测试百里')
    #         assert 2 == 2
    #
    #
