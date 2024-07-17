API Ferremas

Esta es una API desarrollada con Flask para la integración con el Banco Central y Transbank, así como la gestión de órdenes de compra, tipos de herramientas, herramientas y usuarios en la base de datos de Ferremas.

Requisitos

- Python Python 3.10.12
- Flask
- requests
- MySQL

Instalación

1. Clona el repositorio:
    git clone https://github.com/tu_usuario/ferremas-api.git
    cd ferremas-api

2. Instala las dependencias:
    pip install -r requirements.txt

3. Configura tu base de datos en config.py.

4. Ejecuta la aplicación:
    flask run

Endpoints

Integración con el Banco Central

- GET /api/tipo_cambio
  - Obtiene el tipo de cambio desde el Banco Central.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/api/tipo_cambio

Integración con Transbank

- POST /api/v1/transbank/transaction/create
  - Crea una transacción en Transbank.
  - Cuerpo de la solicitud:
    {
      "amount": 1000,
      "session_id": "123456",
      "buy_order": "orden123",
      "return_url": "http://www.comercio.cl/webpay/retorno"
    }
  - Ejemplo de uso:
    curl -X POST http://localhost:5000/api/v1/transbank/transaction/create -H "Content-Type: application/json" -d '{"amount": 1000, "session_id": "123456", "buy_order": "orden123", "return_url": "http://www.comercio.cl/webpay/retorno"}'

Gestión de órdenes de compra

- GET /order_buy/<code>
  - Obtiene una orden de compra por su ID.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/order_buy/10000001

- GET /order_buy
  - Obtiene todas las órdenes de compra.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/order_buy

- POST /order_buy
  - Crea una nueva orden de compra.
  - Cuerpo de la solicitud:
    {
      "usuario_id": 1000,
      "fecha_orden": "2024-07-17 00:00:00",
      "monto_total": 10000.00,
      "estado": "pendiente"
    }
  - Ejemplo de uso:
    curl -X POST http://localhost:5000/order_buy -H "Content-Type: application/json" -d '{"usuario_id": 1000, "fecha_orden": "2024-07-17 00:00:00", "monto_total": 10000.00, "estado": "pendiente"}'

- DELETE /order_buy/<code>
  - Elimina una orden de compra por su ID.
  - Ejemplo de uso:
    curl -X DELETE http://localhost:5000/order_buy/10000001

Gestión de tipos de herramientas

- GET /tools_type/<name>
  - Obtiene un tipo de herramienta por su nombre.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/tools_type/martillo

- GET /tools_type
  - Obtiene todos los tipos de herramientas.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/tools_type

Gestión de herramientas

- GET /tools
  - Obtiene todas las herramientas.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/tools

- GET /tools/<code>
  - Obtiene una herramienta por su código.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/tools/1001

- DELETE /tools/<code>
  - Elimina una herramienta por su código.
  - Ejemplo de uso:
    curl -X DELETE http://localhost:5000/tools/1001

- POST /tools
  - Crea una nueva herramienta.
  - Cuerpo de la solicitud:
    {
      "nombre": "Martillo",
      "tipo": "Herramienta manual",
      "precio": 5000.00
    }
  - Ejemplo de uso:
    curl -X POST http://localhost:5000/tools -H "Content-Type: application/json" -d '{"nombre": "Martillo", "tipo": "Herramienta manual", "precio": 5000.00}'

- PUT /tools/<code>
  - Actualiza una herramienta por su código.
  - Cuerpo de la solicitud:
    {
      "nombre": "Martillo",
      "tipo": "Herramienta manual",
      "precio": 6000.00
    }
  - Ejemplo de uso:
    curl -X PUT http://localhost:5000/tools/1001 -H "Content-Type: application/json" -d '{"nombre": "Martillo", "tipo": "Herramienta manual", "precio": 6000.00}'

Gestión de usuarios

- GET /user
  - Obtiene todos los usuarios.
  - Ejemplo de uso:
    curl -X GET http://localhost:5000/user

- POST /user
  - Crea un nuevo usuario.
  - Cuerpo de la solicitud:
    {
      "nombre": "Juan",
      "apellido": "Pérez",
      "direccion": "Calle Falsa 123",
      "num_cel": 987654321,
      "email": "juan.perez@example.com"
    }
  - Ejemplo de uso:
    curl -X POST http://localhost:5000/user -H "Content-Type: application/json" -d '{"nombre": "Juan", "apellido": "Pérez", "direccion": "Calle Falsa 123", "num_cel": 987654321, "email": "juan.perez@example.com"}'

- DELETE /user/<code>
  - Elimina un usuario por su ID.
  - Ejemplo de uso:
    curl -X DELETE http://localhost:5000/user/1000

- PUT /user/<code>
  - Actualiza un usuario por su ID.
  - Cuerpo de la solicitud:
    {
      "nombre": "Juan",
      "apellido": "Pérez",
      "direccion": "Calle Falsa 123",
      "num_cel": 987654321,
      "email": "juan.perez@example.com"
    }
  - Ejemplo de uso:
    curl -X PUT http://localhost:5000/user/1000 -H "Content-Type: application/json" -d '{"nombre": "Juan", "apellido": "Pérez", "direccion": "Calle Falsa 123", "num_cel": 987654321, "email": "juan.perez@example.com"}'
