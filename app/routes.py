from flask import request, jsonify, json
import requests 
from app import app
from .models import *
#integracion con el banco central
@app.route('/api/tipo_cambio')
def tipo_cambio():
    params = header_banco()
    url = 'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?'
    response =requests.get(url,params=params)
    data = response.json()
    return jsonify(data)

#integracion con transbank
@app.route('/api/v1/transbank/transaction/create',methods=['POST'])
def transbank_create():
    data=request.json
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    headers = header_request_transbamk()
    response = requests.post(url, json=data, headers=headers)
    return response.json()
    
#endpoints de la api ferremas
#Bd order buy
@app.route('/order_buy/<code>', methods=['GET'])
def get_order_buy_by_id(code):
    fetch=fetch_order_by_id(code)
    return jsonify(fetch)
    
@app.route('/order_buy', methods=['GET'])
def get_order_buy():
    fetch=fetch_order_by()
    return jsonify(fetch)

@app.route('/order_buy', methods=['POST'])
def set_order_buy():
    response=request.json
    create_order_by(response)
    fetch=fetch_order_by()
    return jsonify(fetch)   

@app.route('/order_buy/<code>', methods=['DELETE'])
def del_order_buy(code):
    delete_order_by(code)
    fetch=fetch_order_by()
    return jsonify(fetch)    

#Bd tools type

@app.route('/tools_type/<name>', methods=['GET'])
def get_tool_type_by_name(name):
    toolsty=fetch_tools_type_by_id(name)
    return jsonify(toolsty)

@app.route('/tools_type', methods=['GET'])
def get_tools_type():
    toolsty = fetch_all_tools_type()
    return jsonify(toolsty)

#Bd tools

@app.route('/tools', methods=['GET'])
def get_tools():
    tools = fetch_all_tools()
    return jsonify(tools)

@app.route('/tools/<code>', methods=['GET'])
def get_tool(code):
    tool = fetch_tools_by_code(code)
    return jsonify(tool)

@app.route('/tools/<code>', methods=['DELETE'])
def dlt_tool(code):
    Delete_tools(code)
    tools = fetch_all_tools()
    return jsonify(tools)
    
@app.route('/tools', methods=['POST'])
def create_tools():
    tool_data = request.json
    insert_tools(tool_data)
    tools = fetch_all_tools()
    return jsonify(tools)

@app.route('/tools/<code>', methods=['PUT'])
def upd_tools(code):
    tls=request.get_json()
    update_tools(tls,code)
    tools = fetch_all_tools()
    return jsonify(tools)

#Bd user

@app.route('/user', methods=['GET'])
def get_user():
    usr = fetch_all_users()
    return jsonify(usr)

@app.route('/user', methods=['POST'])
def create_user():
    usr = request.json
    insert_users(usr)
    usr = fetch_all_users()
    return jsonify(usr)

@app.route('/user/<code>', methods=['DELETE'])
def dlt_user(code):
    Delete_user(code)
    tools = fetch_all_users()
    return jsonify(tools)

@app.route('/user/<code>', methods=['PUT'])
def upd_user(code):
    usr = request.json
    update_users(usr,code)
    tools = fetch_all_users()
    return jsonify(tools)
