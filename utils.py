"""
provide classic utils function
"""

import pymysql


def create_connect():
    # TODO avoid hard-coded
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='BEMApplication')
    cur = conn.cursor()
    return conn, cur


def insert_to_database(query):
    create_connect()
    conn, cur = create_connect()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
