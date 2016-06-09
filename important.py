from flask import Flask

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    return 'I\'m deployed! Thanks x 1000!'


if __name__ == '__main__':
    app.run()
