from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def ruta_inicio():
    return redirect('/dojos')


@app.route('/process', methods=['POST'])
def procesar_dojo():
    data={
        "nombre":request.form['nombre']
    }
    dojos=Dojo.save(data)
    return redirect('/dojos')



@app.route('/dojos')
def todos():
    dojos=Dojo.get_all()
    print(dojos)
    return render_template('nuevo_dojo.html',dojos=dojos)


@app.route('/dojos/<int:id>')
def detalles_dojo(id):
    data_dojo={
        'dojo_id':id
    }
    dojo_ninjas=Dojo.get_dojos_y_ninjas(data_dojo)
    return render_template('dojo_ninjas.html' , dojo=dojo_ninjas )









