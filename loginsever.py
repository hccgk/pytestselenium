from flask import Flask, request, jsonify
import sys


# if sys.version_info.major < 3:
#     reload(sys)
# sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# 假设这是你的用户数据，实际中应该存储在数据库中
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        response = jsonify({"message": "缺少用户名或密码"})
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response, 400
    print(data)
    print(data['username'])
    username = data['username']
    password = data['password']

    if username in users and users[username] == password:
        response = jsonify({"message": "登录成功"})
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response, 200
    else:
        response = jsonify({"message": "用户名或密码错误"})
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


