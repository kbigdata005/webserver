from flask import Flask , request ,render_template ,redirect,session
import argparse
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import json
from functools import wraps

app = Flask(__name__)
app.secret_key='ubion8'

client = MongoClient('mongodb+srv://root:1234@mydb.vqrlsdn.mongodb.net/?retryWrites=true&w=majority')
#create schema 
db = client.mylist
# print("TEST2")

def is_logged_in(f):
    @wraps(f)
    def wrap(*args , **kwargs):
        if 'is_logged' in session:
            return f(*args , **kwargs)
        
        else:
            return redirect('/login')
    return wrap

@app.route("/", methods=['GET', 'POST'])
def main():
    name="김태경"
    return render_template('main.html', data = name )
    
@app.route("/auth", methods=['GET', 'POST'])
@is_logged_in
def auth():
    return "Success your Auth"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    elif request.method =='POST':
        #create document
        users = db.users
        username = request.form['username']
        email = request.form.get('email')
        password = request.form.get('password')
        password_hash = pbkdf2_sha256.hash(password)

        user = users.find_one({'email': email})
        if user:
            return redirect('/register')
        # print(username)
        else:
            users.insert_one({
                "username":username,
                "email" : email,
                "password":password_hash
            })
            return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])   
def login():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']

        # email 조회 및 password verify
        users = db.users
        result = users.find_one({'email': email})
        print(result)
        if result:
            pw = result['password']

            auth = pbkdf2_sha256.verify(password , pw )
            print(auth)
            if auth == True:
                session['username'] = result['username']
                session['is_logged'] = True
                return redirect('/')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
        
    elif request.method == "GET":
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/list')
@is_logged_in
def list():
    return render_template('list.html')

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

# 입력받을 인자값 등록
# parser.add_argument('--port', required=True, help='write your port')
# 입력받은 인자값을 args에 저장 (type: namespace)
# args = parser.parse_args()


if __name__ == '__main__':
    # print("TEST1")
    app.run(debug=True , port=8000)