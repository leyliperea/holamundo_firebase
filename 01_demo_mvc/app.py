import web
import requests
import json

uri = "https://bd-nube-d853b-default-rtdb.firebaseio.com/personas.json"

uris = (
    "/",'Index'
        )

app = web.application(uris,globals())
render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()
    def POST(self):
        form = web.input()
        nombre = form.nombre
        email = form.email

        data ={
            "nombre": nombre,
            "email": email,
        }
        requests.post(uri,json.dumps(data))
        return render.index()

if __name__ == "__main__":
    app.run()