from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from utils import insert_to_database

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/add/building', methods=['GET', 'POST'])
@cross_origin()
def add_building():
    identify_number = request.json['in']
    address = request.json['address']
    owner = request.json['ownername']
    print(request.json)
    insert_to_database("INSERT INTO Building (identify_number, address, owner) \
VALUES (\'{0}\', \'{1}\', \'{2}\');".format(identify_number, address, owner))
    # TODO add code status
    return jsonify("Successful")






@app.route('/')
def hello_world():
    return 'Hello, World!'
