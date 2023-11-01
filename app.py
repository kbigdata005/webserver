from flask import Flask , request
import argparse
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

client = MongoClient('mongodb+srv://root:1234@mydb.vqrlsdn.mongodb.net/?retryWrites=true&w=majority')
#create schema 
db = client.mylist
# print("TEST2")



@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return "Hello"
    elif request.method =='POST':
        return "안녕"


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        #create document
        # users = db.users
        # username = request.args['username']
        # email = request.args.get('email')
        # password = request.args.get('password')
        # password_hash = pbkdf2_sha256.hash(password)
        # # print(username)
        # users.insert_one({
        #     "username":username,
        #     "email" : email,
        #     "password":password_hash
        # })
        return "Hello"
    elif request.method =='POST':
        #create document
        users = db.users
        username = request.form['username']
        email = request.form.get('email')
        password = request.form.get('password')
        password_hash = pbkdf2_sha256.hash(password)
        # print(username)
        users.insert_one({
            "username":username,
            "email" : email,
            "password":password_hash
        })
        return "안녕"
    


# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

# 입력받을 인자값 등록
# parser.add_argument('--port', required=True, help='write your port')
# 입력받은 인자값을 args에 저장 (type: namespace)
# args = parser.parse_args()


if __name__ == '__main__':
    # print("TEST1")
    app.run(debug=True , port=8000)