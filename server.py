import cherrypy
import os

class WebControlInterface(object):

    @cherrypy.expose
    def start_white_out(self):
        os.system("sudo systemctl start whiteout")
        os.system("sudo systemctl stop lights")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def start_lights(self):
        os.system("sudo systemctl stop whiteout")
        os.system("sudo systemctl start lights")
        raise cherrypy.HTTPRedirect("/")
