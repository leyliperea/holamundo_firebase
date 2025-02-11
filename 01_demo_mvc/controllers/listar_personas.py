import web

import pyrebase

config = {
  "apiKey": "AIzaSyDaDjIevsXP6iecOvUTfZ9eiHJdNdwea14",
  "authDomain": "bd-nube-d853b.firebaseapp.com",
  "databaseURL": "https://proyecto1-42fa3-default-rtdb.firebaseio.com/",
  "storageBucket": "bd-nube-d853b.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)

print(f"Configuration: {firebase}")
db = firebase.database()

render = web.template.render("views", base = "master")

class Listar_personas:
    def GET(self):
        return render.listar_personas()