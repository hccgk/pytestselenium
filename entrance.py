import pytest

if __name__ == '__main__':
    pytest.main(['-vs','./testcase','--reruns=2','--html=./report/report.html'])