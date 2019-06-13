from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from utils import execute_query, create_connect

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
    execute_query("INSERT INTO Building (identify_number, address, owner) \
VALUES (\'{0}\', \'{1}\', \'{2}\');".format(identify_number, address, owner))
    # TODO add code status
    return jsonify("Successful")


@app.route('/api/add/em', methods=['GET', 'POST'])
@cross_origin()
def add_em():
    EM_identify_number = request.json['EM_in']
    EM_count = request.json['EM_count']
    EM_date = request.json['EM_date']
    EM_tot_max = request.json['EM_tot_max']
    EM_tot_min = request.json['EM_tot_min']

    print(request.json)
    execute_query("INSERT INTO EMeter  (EM_count,EM_date,EM_tot_max,EM_tot_min,EM_identify_number) \
                  values ('{0}','{1}','{2}','{3}','{4}') \
                  ".format(EM_count, EM_date, EM_tot_max, EM_tot_min,
                           EM_identify_number))
    # TODO add code status
    return jsonify("Successful")




# used to generate drop-down list
@app.route('/api/getall/building', methods=['GET', 'POST'])
@cross_origin()
def get_all_building():
    create_connect()
    conn, cur = create_connect()
    cur.execute("SELECT * FROM Building")
    conn.commit()
    cur.close()
    res = {}
    for r in cur:
        res[r[1]] = r[1]
    conn.close()
    return jsonify(res)


@app.route('/api/getall/em', methods=['GET', 'POST'])
@cross_origin()
def get_all_em():
    create_connect()
    conn, cur = create_connect()
    cur.execute("SELECT * FROM EMeter")
    conn.commit()
    cur.close()
    res = {}
    for r in cur:
        res[r[1]] = r[1]
    conn.close()
    return jsonify(res)


@app.route('/')
def hello_world():
    return 'Hello, World!'
