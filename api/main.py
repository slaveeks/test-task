from flask import Flask
from db.db import Db

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    db = Db()
    db.check_version()
    app.run(debug=True)
