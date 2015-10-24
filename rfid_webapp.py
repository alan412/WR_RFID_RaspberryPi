import cherrypy
import os
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket
from ws4py.messaging import TextMessage
from cherrypy.process import plugins

from rfid_handling import RFIDHandling

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

rfidHandler = RFIDHandling()

def doRFID():
     cherrypy.engine.publish("websocket-broadcast", TextMessage(rfidHandler.blockingRead()))

class WebSocketHandler(WebSocket):
    def opened(self):
        print "Socket Opened------"
    def closed(self, code, reason="unknown"):
        print "Socket Closed------2"
        
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
         
   plugins.BackgroundTask(0.1, doRFID).start()
   cherrypy.quickstart(rfid(),'/', 
      {
        '/':
        {
            'tools.staticdir.root' : file_path,
        },
        '/logaccess.csv':
        {
            'tools.staticfile.on' : True,
            'tools.staticfile.filename' : file_path + '/logaccess.csv'
        },
        '/users.txt':
        {
            'tools.staticfile.on' : True,
            'tools.staticfile.filename' : file_path + '/users.txt'            
        },
        '/js':
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : file_path + '/js'
        },

        '/static':
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : file_path + '/static'
        },
        '/ws':
        {
            'tools.websocket.on' : True,
            'tools.websocket.handler_cls' : WebSocketHandler   
        }
      }
   )  
   
