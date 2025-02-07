import web

from controllers.index import Index as Index
from controllers.agregar import Agregar as Agregar

urls = (
    '/', 'Index',
    '/insertar', 'Agregar'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()