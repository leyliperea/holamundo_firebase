import web
from models.insertar import Personas

render = web.template.render("views", base = "master")

class Insertar_personas:
    def GET(self):
      try:
        personas = Personas()
        print(f"{personas.insetar_personas()}")
        return render.insetar_personas()
      except Exception as error: 
        print(error)
