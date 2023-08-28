import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-vs','./testcase/test_sever.py','--reruns=2','--html=./report/service_pytest_original_report.html'])
    pytest.main(['-vs','./testcase/test_sever.py','--reruns=2','--alluredir','./report/allure-result'])
    os.system('allure generate ./report/allure-result -o ./report/allure-report --clean')