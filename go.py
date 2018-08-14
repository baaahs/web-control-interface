#!/usr/bin/env python2.7
import cherrypy
from server import WebControlInterface

port = 8080

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': port,
        'server.thread_pool': 1
    },
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': '/home/baaahs/web_control/static',
        'tools.staticdir.index': 'index.html'
    }
}

cherrypy.quickstart(WebControlInterface(), config=config)
