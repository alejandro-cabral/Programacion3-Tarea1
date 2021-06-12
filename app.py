#Importaciones
from flask import Flask, request
from flask_mysqldb import MySQL

#Conexión a la BD
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'dbprueba'
mysql = MySQL()

#Recolección de Datos mediante POST, GET, PUT, DELETE
@app.route('/')
def Index():
    return 'Esto es una prueba'

@app.route('/añadir')
def Añadir():
    return 'Añadiendo'

@app.route('/editar')
def Editar():
    return 'Editando'

@app.route('/eliminar')
def Eliminar():
    return 'Eliminando'
