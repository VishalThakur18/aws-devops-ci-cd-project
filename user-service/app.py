from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "User Service is running!"

@app.route('/hello')
def hello():
    return "Hello from User Service 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
