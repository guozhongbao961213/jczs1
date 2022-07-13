import time

import pytest

if __name__ == '__main__':
    pytest.main(['--reruns=2', '--maxfail=2', f'--html=../report/request{str(int(time.time()))}.html', '-m=smoke'])

    # 参数详解:
    # -S :表示输出调试信息,包括print打印的信息
    # -V :显示更详细的信息
    # -VS :这两个参数一起用
    # -n x :支持多线程或者分布式运行测试用例。（x=线程数）； 如: pytest -VS ./testcase/test_ login.py -n 2
    # --reruns x :失败用例重跑x次 （x=重跑次数）
    # -x:表示只要要一-一个用例报错,那么测试停止。
    # --maxfail x ：出现x个用例失败就停止。（x=失败用例数）
    # -k "函数中包括的字符" : 根据测试用例的部分字符串指定测试用例；如: pytest -VS ./testcase -K "函数中包括的字符"
    # -m "模块名称" ：执行函数前加 @pytest.mark.模块名称的用例
    # --html path（路径）：生成html格式的测试报告
    #
    # 函数前标记使用方法：
    # @pytest.mark.run(order=x) : 修改用例执行规则 x=顺序数
    # @pytest.mark.标签名 ：执行函数前加 @pytest.mark.模块名称的用例 运行代码时pytest后添加 -r '标签名'
    #
    # def setup(self):
    #     print('每个用例执行前执行')
    #
    # def teardown(self):
    #     print('每个用例执行后执行')
    #
    # def setup_class(self):
    #     print('每一类用例执行前执行')
    #
    # def teardown_class(self):
    #     print('每一类用例执行后执行')
    #

    #
    #
    #
