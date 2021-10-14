from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db

app = Flask(__name__)

@app.route("/cargos/<codigo>", methods=['GET'])
def get_cargo(codigo):
    con = db.get_connection()
    dbemp = con.dbempleados
    try:
        cargos = dbemp.cargos
        retorno = dumps(cargos.find_one({'_id': ObjectId(codigo)}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/cargos", methods=['GET'])
def get_cargos():
    con = db.get_connection()
    dbemp = con.dbempleados
    try:
        cargos = dbemp.cargos
        retorno = dumps(cargos.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/cargos", methods=['POST'])
def create():
    data = request.get_json()
    nombre = data['nombre']
    con = db.get_connection()
    dbemp = con.dbempleados
    try:
        cargos = dbemp.cargos
        cargos.insert({"nombre":nombre})
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/cargos/<codigo>", methods=['PUT'])
def update(codigo):
    data = request.get_json()
    nombre = data['nombre']
    con = db.get_connection()
    dbemp = con.dbempleados
    try:
        cargos = dbemp.cargos
        cargos.update({'_id': ObjectId(codigo)}, {"nombre": nombre}) 
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/cargos/<codigo>", methods=['DELETE'])
def delete(codigo):
    con = db.get_connection()
    dbemp = con.dbempleados
    try:
        cargos = dbemp.cargos
        cargos.delete_one({'_id': ObjectId(codigo)})
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")
