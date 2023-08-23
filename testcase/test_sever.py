import json

import pytest

from utils import excelclient
from utils.httpclient import send_request



def test_s1():
    re = send_request("post", "http://192.168.31.70:5000/login", {"username": "user1", "password": "password1"})
    print(re.json())
# {"username": "user1", "password": "password"}

@pytest.mark.parametrize('case',excelclient.read_excel())
def test_loginWithExcel(case):
    me = case['method']
    url = case['url']
    body = json.loads(case['body'])
    result = send_request(me, url, body)
    print(result.json())
    print(case['expected'])
    # 将Python字典转换为JSON字符串，并保留原始引号
    expected_json = json.dumps(result.json(), ensure_ascii=False)
    assert expected_json == case['expected']


