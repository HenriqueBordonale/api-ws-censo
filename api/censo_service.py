from flask import Flask, Blueprint, request, jsonify
import sqlite3

censo = Blueprint('censo', __name__)


def conectar():
    return sqlite3.connect('database/db_censoapi.db')


@censo.route('/', methods=['GET'])
def get_all():
    censo = []

    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_regioes")

        for i in cur.fetchall():
            censo = {}
            censo["num"] = i["num"]
            censo["nome"] = i["nome"]
            censo["idh"] = i["idh"]
            censo["cid_populosa"] = i["cid_populosa"]
            censo.append(censo)
    except Exception as e:
        print(e)
        censo = []

    return jsonify(censo)