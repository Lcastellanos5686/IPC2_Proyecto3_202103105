from flask import Flask,request,jsonify
from funciones.funciones import*
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
from funciones.PrintColores import*


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello_world():
    return 'Prueba'

@app.route("/DatosEstudiante",methods=['GET'])
def DatosEstudiante():
    return '''<p>Alumno: Luis Daniel Castellanos Betancourt</p>
    <p>Curso: Introduccion a la programacion y computacion 2</p>
    <p>https://uedi.ingenieria.usac.edu.gt/campus/course/view.php?id=13016</p>'''


@app.route("/CrearPerfiles",methods=['POST'])
def CrearPerfiles():
    ObjetoXML = parseString(request.data.decode("utf-8"))
    return leerXmlPerfiles(ObjetoXML)

@app.route("/CrearMensajes",methods=['POST'])
def CrearMensajes():
    ObjetoXML = parseString(request.data.decode("utf-8"))
    return leerXmlMensaje(ObjetoXML)

@app.route("/ResetearDatos",methods=['GET'])
def ResetearDatos():
    resetear()
    return 'Se restauraron las bases de datos XML'

@app.route("/MensajesPorUsuario",methods=['GET'])
def MensajesPorUsuario():
    usuario = request.args.get('usuario')
    return tablaUsuario(usuario)