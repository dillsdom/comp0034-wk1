from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f"Hello {escape(name)}! and welcome to my paralympics app."

if __name__ == '__main__':
    app.run(port=5002)