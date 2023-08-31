import os

import pytest

if __name__ == '__main__':
    # 输出普通pytest自带的 html报告
    pytest.main(['-vs','./testcase/test_sever.py','--reruns=2','--html=./report/service_pytest_original_report.html'])
    # 输出allure报告
    # pytest.main(['-vs','./testcase/test_sever.py','--reruns=2','--alluredir','./report/allure-result'])
    # os.system('allure generate ./report/allure-result -o ./report/allure-report --clean')