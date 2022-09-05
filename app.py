from flask import Flask
app = Flask(__name__)


@app.route('/number', methods=['GET'])
def number():
    return 3


if __name__ == '__main__':
    app.run()
