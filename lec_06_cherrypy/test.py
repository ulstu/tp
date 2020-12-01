import cherrypy

class HelloWorld(object):

    @cherrypy.expose
    def indexes(self):
        return "Hello World!"

    @cherrypy.expose
    def domagic(self):
        return "Magic happens!"

cherrypy.quickstart(HelloWorld())