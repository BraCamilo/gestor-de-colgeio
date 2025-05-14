from flask import Flask, jsonify, request,render_template
import os
import json


from Modelos.estudiantes import Estudiante


app = Flask(__name__)

@app.route("/")
def index():
    descripcion = "Menú del Sistema Escolar"
    op1 = "Registrar estudiante"
    op2 = "Registrar profesor"
    op3 = "Registrar curso"
    op4 = "Buscar estudiante por ID"
    op5 = "Buscar profesor por ID"
    op6 = "Buscar curso por ID"
    op7 = "Guardar datos"
    op8 = "Salir"    
    return render_template("index.html", descripcion=descripcion, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6, op7=op7, op8=op8) #render_template es para renderizar el html, y le pasamos la variable descripcion para que se vea en el html

@app.route("/R-estudiante", methods=["GET", "POST"])
def registrar_estudiante():
    if request.method == "POST":
        # Obtener los datos del formulario
        Id = request.form["id"]
        nombre = request.form["nombre"]
        correo = request.form["email"]
        edad = request.form["edad"]
        Curso = request.form["curso"]

        # Crear un nuevo objeto Estudiante
        nuevo_estudiante = Estudiante(Id=Id, nombre=nombre, edad=edad, correo=correo, Curso=Curso)


        archivo = "estudiantes.json"
        datos = []

        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                try:
                    datos = json.load(f)
                except json.JSONDecodeError:
                    datos = []
        
        

        datos.append(nuevo_estudiante.to_dict())
        print(datos)

        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)


    return render_template("/registrar_estudiante.html")