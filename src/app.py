#Importaciones

from flask import Flask, request, render_template
from flask_mysqldb import MySQL

#Conexión a la BD

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'dbprueba'
mysql = MySQL(app)

#Recolección de Datos mediante POST, GET, PUT, DELETE

@app.route('/')
def Index():
    return render_template('index.html')

#POST

@app.route('/añadir', methods=['POST'])
def Añadir():
    return 'Añadiendo'

#PUT

@app.route('/editar', methods=['PUT'])
def Editar():
    return 'Editando'

#DELETE

@app.route('/eliminar', methods=['DELETE'])
def Eliminar():
    return 'Eliminando'
