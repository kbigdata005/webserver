from flask import Flask
import argparse

app = Flask(__name__)

# print("TEST2")



@app.route("/", methods=['GET', 'POST'])
def main():
    return "Hello"

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

# 입력받을 인자값 등록
parser.add_argument('--port', required=True, help='write your port')
# 입력받은 인자값을 args에 저장 (type: namespace)
args = parser.parse_args()


if __name__ == '__main__':
    # print("TEST1")
    app.run(debug=True , port=args.port)