#!/usr/bin/env python2.7
import cherrypy
from server import OSCLayoutServer

port = 9658

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': port,
        'server.thread_pool': 1
    }
}

cherrypy.quickstart(WebControlInterface, config=config)
