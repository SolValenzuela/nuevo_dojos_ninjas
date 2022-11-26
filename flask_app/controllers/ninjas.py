from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas_index():
    todos_los_dojos=Dojo.get_all()
    return render_template('ninjas.html',todos_los_dojos=todos_los_dojos)



@app.route('/ninjas/process', methods=['POST'])
def process_new_ninja():
    #print(request.form)
    data={
        'first_name':request.form['first_name'],
        'last_name': request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    new_ninja=Ninja.create(data)
    print(new_ninja)
    return redirect(f"/dojos/{request.form['dojo_id']}")