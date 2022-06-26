from flask import Flask
from db.db import Db

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    db = Db()
    print(db.get_data_from_db())
    print(db.get_sum_of_price())
    app.run(debug=True)
