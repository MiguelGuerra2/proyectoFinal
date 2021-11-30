from logging import DEBUG
import os, socket, threading
from flask import Flask
from flask.ctx import AppContext
from flask_cors import CORS
from db import get_db
from flask.cli import with_appcontext

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_mapping(
    SECRET_KEY= 'mikey',
    DATABASE_HOST=os.getenv("FLASK_DATABASE_HOST"),
    DATABASE_PASSWORD=os.getenv("FLASK_DATABASE_PASSWORD"),
    DATABASE_USER=os.getenv("FLASK_DATABASE_USER"),
    DATABASE=os.getenv("FLASK_DATABASE")
)

import db

db.init_app(app)

import routes
import level

app.register_blueprint(routes.bp)
app.register_blueprint(level.bp)

# Create a socket

def tcp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    well_known_port = 8881
    sock.bind(('', well_known_port))

    sock.listen(5)
    print('Intentando conectar con cliente')
    try:
        while 1:
            newSocket, address = sock.accept(  )
            print ("Connected from", address)
            while 1:
                receivedData = newSocket.recv(1024) #informacion recibida
                if not receivedData: break
                data = float(receivedData) #Se convierte a float
                data = data/100 #Se pasa de centimetros a metros
                with app.app_context():
                    db, c = get_db()
                    c.execute(
                        'insert into datalevel (data) value (%s)',
                        (data,)
                    ) #Se inserta la informacion recibida en la tabla
                    db.commit()
            newSocket.close()
            print ("Disconnected from", address)
    finally:
        sock.close()

server_tcp = threading.Thread(target=tcp)
server_tcp.start()
app.run(host='0.0.0.0', debug=True, port=80)
