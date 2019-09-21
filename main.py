from app import app
import os
import cherrypy
import sys
import collections
import time
import datetime
import queue

if __name__ == '__main__':

    class Swagger(object): pass
    
    # Mount the application

    cherrypy.tree.graft(app, "/")

    # Add static file serving to enable swagger GUI
    PATH = os.path.abspath(os.path.dirname(__file__))
    cherrypy.tree.mount(Swagger(), '/html', config={
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': PATH + '/html',
            'tools.staticdir.index': 'index.html',
        }
    })

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 30

    # Subscribe this server
    server.subscribe()


    # Start the server engine (Option 1 *and* 2)
    cherrypy.engine.start()
    cherrypy.engine.block()