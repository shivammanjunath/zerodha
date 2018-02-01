import cherrypy
import os, os.path
from rest import BhavcopyReader as bcr

PATH = os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(bcr(), '/', config = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': PATH
        }
    })


