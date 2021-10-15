from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db

app = Flask(__name__)

@app.route("/ingreso-paciente/<codigo>", methods=['GET'])
def get_paciente(codigo):
    con = db.get_connection()
    dbpac = con.dbpacientes
    try:
        pacientes = dbpac.pacientes
        retorno = dumps(pacientes.find_one({'_id': ObjectId(codigo)}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/ingreso-paciente", methods=['GET'])
def get_pacientes():
    con = db.get_connection()
    dbpac = con.dbpacientes
    try:
        pacientes = dbpac.pacientes
        retorno = dumps(pacientes.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/ingreso-paciente", methods=['POST'])
def create():
    data = request.get_json()
    con = db.get_connection()
    dbpac = con.dbpacientes
    try:
        pacientes = dbpac.pacientes
        pacientes.insert(data)
        
        return jsonify({"Paciente":"Creado exitosamente"})
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/ingreso-paciente/<codigo>", methods=['PUT'])
def update(codigo):
    data = request.get_json()
    #nombre = data['nombre']
    con = db.get_connection()
    dbpac = con.dbpacientes
    try:
        pacientes = dbpac.pacientes
        pacientes.update({'_id': ObjectId(codigo)}, data) 
        return jsonify({"Paciente":"Actualizado exitosamente"})
    finally:
        con.close()
        print("Conexion cerrada")

@app.route("/ingreso-paciente/<codigo>", methods=['DELETE'])
def delete(codigo):
    con = db.get_connection()
    dbpac = con.dbpacientes
    try:
        pacientes = dbpac.pacientes
        pacientes.delete_one({'_id': ObjectId(codigo)})
        return jsonify({"Paciente":"Eliminado exitosamente"})
    finally:
        con.close()
        print("Conexion cerrada")

###################################################################################
