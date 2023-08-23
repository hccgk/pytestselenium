import requests


def send_request(method, url, data, **kwargs):
    if method == 'get':
        res = requests.get(url=url, params=data)
    elif method == 'post':
        res = requests.post(url=url, json=data)
    elif method == 'delete':
        res = requests.delete(url=url, json=data)
    else:
        res = None
        print('不支持的请求方式')
    return res


