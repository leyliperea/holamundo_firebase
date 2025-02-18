import web

from controllers.index import Index as Index
from controllers.lista_personas import Lista_personas as Lista_personas
from controllers.agregar import Agregar as Agregar

urls = (
    '/', 'Index',
    '/agregar', 'Agregar',
    '/lista_personas', 'Lista_personas'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()