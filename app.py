from flask import Flask, request, jsonify, make_response, send_file, send_from_directory
from flask_cors import CORS, cross_origin

import io, csv

from utils import execute_query, create_connect

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

temp_download_res = []


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


@app.route('/api/get/charts', methods=['GET', 'POST'])
@cross_origin()
def get_chart():
    em = request.json['em']
    create_connect()
    conn, cur = create_connect()
    cur.execute(
        "SELECT DATE_FORMAT(EM_date, '%Y/%m/%d'),EM_count,EM_tot_max,EM_tot_min FROM EMeter \
        where EM_identify_number={0}".format(em))
    cur.close()
    res = [[], [], [], []]
    for r in cur:
        res[0].append(r[0])
        res[1].append(r[1])
        res[2].append(r[2])
        res[3].append(r[3])
    conn.close()
    print(res)

    global temp_download_res
    temp_download_res = res
    return jsonify(res)


@app.route('/api/download', methods=['GET', 'POST'])
@cross_origin()
def download_csv():
    global temp_download_res
    print("temp_download_res is ")
    print(temp_download_res)
    print("------------------------------")
    with open("output.csv", "w+", newline='') as csv_file:
        # TODO optimize it by list-comprehension
        writer = csv.writer(csv_file, delimiter=',')

        for r in temp_download_res:
            writer.writerow(r)
    return send_from_directory("", "output.csv", as_attachment=True)
    # si = io.StringIO()
    # cw = csv.writer(si)
    # cw.writerows(zip(temp_download_res))
    # output = make_response(si.getvalue())
    # output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    # output.headers["Content-type"] = "text/csv"
    # return output

    # return send_file(io_, attachment_filename='xx.csv', as_attachment=True)


@app.route('/api/add/relationship', methods=['GET', 'POST'])
@cross_origin()
def add_relationship():
    building = request.json['building']
    em = request.json['em']

    """
    Overall the logic is :
    1. check whether EM already exists;if it exists ,return error
    2. check whether the record exists;if exists ,return error
    3. return successfully
    
    or we just need to return all available EMs
    """

    execute_query("INSERT INTO B_EM_Relationship (building_identify_number,EM_identify_number) \
VALUES ('{0}','{1}');".format(building, em))
    execute_query("INSERT INTO EMeter (EM_identify_number) values ('{0}')".format(em))
    return jsonify("success")

    # used to generate drop-down list


@app.route('/api/get/relationship', methods=['GET', 'POST'])
@cross_origin()
def get_relationship():
    """
    used to get all the related teable
    :return:
    """
    create_connect()
    conn, cur = create_connect()
    try:
        em_in = request.json['em_in']
        flag = 0
    except KeyError:
        building_in = request.json['building_in']
        flag = 1
    if flag:
        cur.execute("SELECT * FROM B_EM_Relationship where building_identify_number={0}".format(building_in))
    else:
        cur.execute("SELECT * FROM B_EM_Relationship where EM_identify_number={0}".format(em_in))

    res = [r[2] for r in cur]
    put = []
    for index in res:
        if flag:
            cur.execute(
                "SELECT  EM_identify_number,DATE_FORMAT(EM_date, '%Y/%m/%d'),EM_count, \
                EM_tot_max,EM_tot_min FROM EMeter where EM_identify_number={0}".format(
                    index))
        else:
            cur.execute("SELECT * FROM Building where identify_number={0}".format(index))
        for r in cur:
            print("r is:")
            print(r)
            put.append([])
            put[-1].extend(r[0:])
    print(put)
    print(res)
    conn.close()
    cur.close()

    return jsonify(put)


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


def get_em(query):
    create_connect()
    conn, cur = create_connect()
    cur.execute(query)
    conn.commit()
    cur.close()
    res = {}
    for r in cur:
        res[r[0]] = r[0]
    conn.close()
    return jsonify(res)


@app.route('/api/getall/em', methods=['GET', 'POST'])
@cross_origin()
def get_all_em():
    return get_em("SELECT id FROM AllEMeterIndex")


@app.route('/api/getall/available/em', methods=['GET', 'POST'])
@cross_origin()
def get_all_avialble_em():
    return get_em("SELECT * FROM AllEMeterIndex where id not in \
                  (select EM_identify_number from B_EM_Relationship)")


@app.route('/')
def hello_world():
    return 'Hello, World!'
