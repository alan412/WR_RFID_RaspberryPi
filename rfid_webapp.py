import cherrypy
import os
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket
from ws4py.messaging import TextMessage

from keyboard_alike import reader
import datetime
import csv
from phant import Phant

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class WebSocketHandler(WebSocket):
    def opened(self):
        print "Socket Opened------"
    def closed(self, code, reason="A client left the room without a proper explanation."):
        print "Socket Closed---------------------2"
        
class rfid(object):
   @cherrypy.expose
   def index(self):
      return open('web/index.html')
   @cherrypy.expose
   def ws(self):
      # you can access the class instance through
      handler = cherrypy.request.ws_handler

class rfidGeneratorWebService(object):
   exposed = True
   @cherrypy.tools.accept(media='text/plain')

   def GET(self):    
       return cherrypy.session['session_id']

if __name__ == '__main__':
   rfidapp = rfid()
   rfidapp.generator = rfidGeneratorWebService()


   file_path = os.getcwd() + '/web'

# This is the configuration and starting of the service
   cherrypy.config.update({'server.socket_host' : "0.0.0.0",
                           'server.socket_port' : 9090})
   cherrypy.quickstart(rfid(),'/', 
      {
        '/':
        {
            'tools.staticdir.root' : file_path,
        },
        '/style.css':
        {
            'tools.staticfile.on' : True,
            'tools.staticfile.filename' : file_path + '/style.css'
        },
        '/attendance.js':
        {
            'tools.staticfile.on' : True,
            'tools.staticfile.filename' : file_path + '/attendance.js'
        },
        '/ws':
        {
            'tools.websocket.on' : True,
            'tools.websocket.handler_cls' : WebSocketHandler   
        }
      }
   )
   ##### CODE NEVER GETS HERE!!
   
   reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID
   reader.initialize()
   while(1):
      print "waiting for card"
      card = reader.read().strip()    # get the card number
      print card
      cherrypy.engine.publish('websocket-broadcast', TextMessage(card))