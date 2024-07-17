from app import mysql
from flask import current_app
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_USER = os.getenv('BC_USER')
API_PASS = os.getenv('BC_PASS')

#       order buy

def fetch_order_by():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM orden_compra")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching order buy : {e}")
        return None
    finally:
        cursor.close()
        
def fetch_order_by_id(code):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM orden_compra WHERE orden_id = %s", (code,))
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        
        return data
    
    except Exception as e:
        current_app.logger.error(f"Error fetching order buy by code {code}: {e}")
        return None
    finally:
        cursor.close()
        
def create_order_by(order_data):
    cursor = mysql.connection.cursor()
    try:
        orders = (
            (
                order['usuario_id'],
                order['fecha_orden'],
                order['monto_total'],
                order['estado']
            )
            for order in order_data
        )
        cursor.executemany("""
            INSERT INTO orden_compra 
            (usuario_id, fecha_orden, monto_total, estado)
            VALUES (%s, %s, %s, %s)
        """, orders)
        
        mysql.connection.commit()
        return True
    
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error inserting order buy: {e}")
        return False
    finally:
        cursor.close()
        
def delete_order_by(order_data):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM orden_compra WHERE orden_id = %s",(order_data,))
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE orden_compra SET orden_id = @count := orden_id - 1 WHERE orden_id > %s;", (order_data,))
        max_id = 10000000 
        cursor.execute("ALTER TABLE orden_compra AUTO_INCREMENT = %s", (max_id + 1,))
        
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error deleting tool: {e}")
        return False
    finally:
        cursor.close()
    
#       tipos de herramientas

def fetch_tools_type_by_id(name):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM tools_type WHERE descriptions=%s", (name,))
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching tool by code {name}: {e}")
        return None
    finally:
        cursor.close()

def fetch_all_tools_type():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM tools_type")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching tools_type: {e}")
        return []
    finally:
        cursor.close()

#       herramientas

def fetch_all_tools():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM tools")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching tools: {e}")
        return []
    finally:
        cursor.close()

        
def fetch_tools_by_code(code):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM tools WHERE tools_type_id=%s", (code,))
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching tool by code {code}: {e}")
        return None
    finally:
        cursor.close()

def insert_tools(tools_data):
    cursor = mysql.connection.cursor()
    try:
        tool = ((
            tool['usuario_id'],
            tool['tools_type_id'],
            tool['costo'],
            tool['nombre'],
            tool['descripcion'],
            tool['stock'])
        for tool in tools_data
        )
        cursor.executemany("""
            INSERT INTO tools 
            ( usuario_id, tools_type_id, costo, nombre, descripcion, stock)
            VALUES ( %s, %s, %s, %s, %s, %s)
        """, tool)
        
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error inserting tool: {e}")
        return False
    finally:
        cursor.close()

def Delete_tools(tools_data):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM tools WHERE tools_id = %s",(tools_data,))
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE tools SET tools_id = @count := tools_id - 1 WHERE tools_id > %s;", (tools_data,))
        max_id =  100 
        cursor.execute("ALTER TABLE tools AUTO_INCREMENT = %s", (max_id ,))
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error deleting tool: {e}")
        return False
    finally:
        cursor.close()
        
def update_tools(tools_data,code):
    cursor = mysql.connection.cursor()
    try:
        tool = (
            tools_data['usuario_id'],
            tools_data['tools_type_id'],
            tools_data['costo'],
            tools_data['nombre'],
            tools_data['descripcion'],
            tools_data['stock'],
            code
            )
        cursor.execute(
            """UPDATE tools SET
            usuario_id = %s, tools_type_id = %s, costo = %s, nombre = %s,
            descripcion = %s, stock = %s where tools_id = %s""",
                      tool )
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error updating tools: {e}")
        return False
    finally:
        cursor.close()   
          
#       usuarios

def fetch_all_users():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM usuario")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return data
    except Exception as e:
        current_app.logger.error(f"Error fetching users: {e}")
        return []
    finally:
        cursor.close() 

def insert_users(user_data):
    cursor = mysql.connection.cursor()
    try:
        usr=((
            usr['nombre'],
            usr['apellido'],
            usr['direccion'],
            usr['num_cel'],
            usr['email']
            )for usr in user_data
            )
        cursor.executemany("INSERT INTO usuario ( nombre, apellido, direccion, num_cel, email) VALUES ( %s, %s, %s, %s, %s)",
                      usr )
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error inserting tool: {e}")
        return False
    finally:
        cursor.close()
        

def Delete_user(user_data):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM usuario WHERE email = %s",(user_data,))
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE usuario SET usuario_id = @count := usuario_id - 1 WHERE usuario_id > %s;", (user_data,))
        max_id =  1000 
        cursor.execute("ALTER TABLE usuario AUTO_INCREMENT = %s", (max_id ,))
        
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error deleting user: {e}")
        return False
    finally:
        cursor.close()
        
def delete_user_by_code(user_data):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM usuario WHERE  usuario_id = %s",(user_data,))
        cursor.execute("SET @count = 0;")
        cursor.execute("UPDATE usuario SET usuario_id = @count := usuario_id - 1 WHERE usuario_id > %s;", (user_data,))
        max_id =  1000 
        cursor.execute("ALTER TABLE usuario AUTO_INCREMENT = %s", (max_id ,))
        
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error deleting user: {e}")
        return False
    finally:
        cursor.close()            
        
def update_users(user_data,code):
    cursor = mysql.connection.cursor()
    try:
        usr=(
            user_data['nombre'],
            user_data['apellido'],
            user_data['direccion'],
            user_data['num_cel'],
            code
            )
        cursor.execute("UPDATE usuario SET nombre = %s, apellido = %s, direccion = %s, num_cel = %s where email= %s",
                       usr)
        mysql.connection.commit()
        return True
    except Exception as e:
        mysql.connection.rollback()
        current_app.logger.error(f"Error updating user: {e}")
        return False
    finally:
        cursor.close()
        
#cabeceras de transbank
        
def header_request_transbamk():
    headers = {
        "authorization" : "Token",
        "Tbk-Api-Key-Id" : "597055555532",
        "Tbk-Api-Key-Secret" : "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "Referrer-Policy" : "origin-when-cross-origin"
    }
    return headers

# cabecera Banco central
def header_banco():
    params = {
        'user': API_USER, 
        'pass': API_PASS,
        'firstdate': '2023-01-01',
        'timeseries': 'F073.TCO.PRE.Z.D' 
        }
    return params