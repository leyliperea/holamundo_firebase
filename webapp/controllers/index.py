import web

render = web.template.render("views", base = "master")

class Index:
    def GET(self):
        return render.index()