import pyrebase

config = {
  "apiKey": "AIzaSyDaDjIevsXP6iecOvUTfZ9eiHJdNdwea14",
  "authDomain": "bd-nube-d853b.firebaseapp.com",
  "databaseURL": "https://proyecto1-42fa3-default-rtdb.firebaseio.com/",
  "storageBucket": "bd-nube-d853b.firebasestorage.app"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

class Personas:
    def _init_(self):
        pass
    
    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response ={
                "status":200,
                "message":"Todo bien",
                "personas":dict(personas.val())
            }
            return response
        except Exception as error:
            print(f"{error.args[0]}")
            response ={
                "status":400,
                "message":"Error en el servidor",
                "personas":{}
                }
            return response
persona = Personas()
print(f"{persona.lista_personas()}")