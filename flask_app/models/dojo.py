from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    db_name='esquema_dojos_y_ninjas'

    def __init__(self,data):
        self.id = data['id']
        self.nombre= data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]

        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (nombre,created_at,updated_at) VALUES (%(nombre)s,NOW(),NOW())"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojo =[]
        for b in dojos:
            dojo.append(cls(b))
        return dojo

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return cls(results[0])
    


    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET nombre=%(nombre)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
    

    # @classmethod
    # def get_dojos_ninjas( cls , data ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL('esquema_dojos_y_ninjas').query_db( query , data )
        
    #     dojo = cls( results[0] )
    #     for ninja in results:
    #         # ahora parseamos los datos de ninjas para crear instancias de ninjas y agregarlas a nuestra lista
    #         ninja_data = {
    #             "id" : ninja["ninjas.id"],
    #             "first_name" : ninja["first_name"],
    #             "last_name" : ninja["last_name"],
    #             "age" : ninja["age"],
    #             "dojo_id" : ninja["dojo_id"],
    #             "created_at" : ninja["ninjas.created_at"],
    #             "updated_at" : ninja["ninjas.updated_at"]
    #         }
    #         dojo.ninjas.append( ninja.Ninja(ninja_data))
    #     return dojo
    

    @classmethod
    def get_dojos_y_ninjas(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(dojo_id)s"
        results=connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)    
        print(results)
        dojo_data=results[0]
        dojo=Dojo(dojo_data)
        todos_los_ninjas=[]
        for data in results:
            ninja_data={
                'id':data['ninjas.id'],
                'first_name':data['first_name'],
                'last_name':data['last_name'],
                'age':data['age'],
                'created_at':data['ninjas.created_at'],
                'updated_at':data['ninjas.updated_at']
            }
            nuevo_ninja=Ninja(ninja_data)
            todos_los_ninjas.append(nuevo_ninja)
        dojo.ninjas=todos_los_ninjas
        return dojo



    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)