import pyrebase

config = {
  "apiKey": "AIzaSyDaDjIevsXP6iecOvUTfZ9eiHJdNdwea14",
  "authDomain": "bd-nube-d853b.firebaseapp.com",
  "databaseURL": "https://proyecto1-42fa3-default-rtdb.firebaseio.com/",
  "storageBucket": "bd-nube-d853b.firebasestorage.app",
}

firebase = pyrebase.initialize_app(config)

db=firebase.database()

class Personas:
   def __init__(self):
      pass
    def lista_personas(self):
        try:
            personas= db.child("personas").get()
            response ={"status":200, JSON
                "message":"excelente",
                "personas":{"001":
                                    {"nombre":"Dejah"}
                                    {"nombre":"Jonh"}
                            }
                }
       datos=db.child("personas").get()
       return datos
    def insertar_persona()

