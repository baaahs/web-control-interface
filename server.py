import cherrypy
import os

class WebControlInterface(object):

    @cherrypy.expose
    def index(self):
 
        olad_status = 'active' if os.system("systemctl is-active olad --quiet") == 0 else 'inactive'
        lights_status = 'active' if os.system("systemctl is-active lights --quiet") == 0 else 'inactive'
        whiteout_status = 'active' if os.system("systemctl is-active whiteout --quiet") == 0 else 'inactive'
        osc_layout_server_status = 'active' if os.system("systemctl is-active osc_layout_server --quiet") == 0 else 'inactive'

        olad_action_a_href = '<a href="stop_olad">make inactive</a>' if os.system("systemctl is-active olad --quiet") == 0 else '<a href="start_olad">make active</a>'
        lights_action_a_href = '<a href="stop_lights">make inactive</a>' if os.system("systemctl is-active lights --quiet") == 0 else '<a href="start_lights">make active</a>'
        whiteout_action_a_href = '<a href="stop_whiteout">make inactive</a>' if os.system("systemctl is-active whiteout --quiet") == 0 else '<a href="start_whiteout">make active</a>'
        osc_layout_server_status_action_a_href = '<a href="stop_osc_layout_server">make inactive</a>' if os.system("systemctl is-active osc_layout_server --quiet") == 0 else '<a href="start_osc_layout_server">make active</a>'

        response = "<html><head><title>BAAAHS Web Control</title></head><body><font size='7'>"        
        response += "lights service is " + lights_status + ", " + lights_action_a_href + ".<br><hr>"
        response += "whiteout service is " + whiteout_status + ", " + whiteout_action_a_href + ".<br><hr>"
        response += "olad service is " + olad_status + ", " + olad_action_a_href + ".<br><hr>"
        response += "osc_layout_server service is " + osc_layout_server_status + ", " + osc_layout_server_status_action_a_href + "."
        response += "</font></body></html>"
        return response

    @cherrypy.expose
    def start_olad(self):
        os.system("sudo systemctl start olad")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def stop_olad(self):
        os.system("sudo systemctl stop olad")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def start_lights(self):
        os.system("sudo systemctl start lights")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def stop_lights(self):
        os.system("sudo systemctl stop lights")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def start_whiteout(self):
        os.system("sudo systemctl start whiteout")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def stop_whiteout(self):
        os.system("sudo systemctl stop whiteout")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def start_osc_layout_server(self):
        os.system("sudo systemctl start osc_layout_server")
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def stop_osc_layout_server(self):
        os.system("sudo systemctl stop osc_layout_server")
        raise cherrypy.HTTPRedirect("/")
