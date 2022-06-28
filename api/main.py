from flask import Flask
from db.db import Db
from utils.utils import Utils
from settings import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD, SERVER_HOST

app = Flask(__name__)

# Initiate database module
db = Db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)


# Route to get total sum
@app.route('/test-task/api/v1.0/sum', methods=['GET'])
def sum_of_orders():
    # Make response to client
    response = Utils.make_response_to_client({'sum': db.get_sum_of_price()})

    return response


# Route to get all data
@app.route('/test-task/api/v1.0/all_data', methods=['GET'])
def all_data():
    # Make response to client
    response = Utils.make_response_to_client(db.get_data_from_db())

    return response


# Route to get grouped by some data with dates
@app.route('/test-task/api/v1.0/ordered_data', methods=['GET'])
def ordered_data():
    response = Utils.make_response_to_client(db.get_ordered_data())

    return response


if __name__ == '__main__':
    # Run flask app
    app.run(host=SERVER_HOST, debug=True)
