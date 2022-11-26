from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    db_name='esquema_dojos_y_ninjas'

    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.age= data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

        

    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s,NOW(),NOW())"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (first_name,last_name,age,dojo_id,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s,NOW(),NOW())"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)





    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        dojos =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojo =[]
        for b in dojos:
            dojo.append(cls(b))
        return dojo

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE esquema_dojos_y_ninjas.id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return cls(results[0])
    


    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s, age=%(age)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)