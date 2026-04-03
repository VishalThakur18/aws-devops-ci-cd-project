from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "User Service is running! form Vishal --Version 2"

@app.route('/hello')
def hello():
    return "Hello from User Service form Vishal --Version 2 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
