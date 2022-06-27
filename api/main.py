from flask import Flask, jsonify, make_response
from db.db import Db
import json

app = Flask(__name__)
db = Db()

@app.route('/todo/api/v1.0/sum', methods=['GET'])
def sum_of_orders():
    response = make_response(jsonify({'sum': db.get_sum_of_price()}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/todo/api/v1.0/all_data', methods=['GET'])
def index():
    response = make_response(jsonify(db.get_data_from_db()))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/todo/api/v1.0/ordered_data', methods=['GET'])
def ordered():
    response = make_response(jsonify(db.get_ordered_data()))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
