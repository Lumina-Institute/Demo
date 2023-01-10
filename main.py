from flask import Flask
import constants as C

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test/')
def test():
    return C.MSG


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


