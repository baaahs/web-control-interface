import cherrypy
import os
import zipfile

class WebControlInterface(object):

    @cherrypy.expose
    def index(self):
        return "<a href=\"start_white_out\" class=\"button\">Start White Out</a><br><a href=\"start_lights\" class=\"button\">Start Lights</a>"

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
