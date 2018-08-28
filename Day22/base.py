"""
Use this as the base for your websocket servers
"""


import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
import tornado.options

LISTEN_PORT = 8000
LISTEN_ADDRESS = '127.0.0.1'

class ChannelHandler(tornado.websocket.WebSocketHandler):
    """
    Handler that handles a websocket channel
    """
    @classmethod
    def urls(cls):
        return [
            (r'/web-socket/', cls, {}), #Route/handler/kwargs
        ]
    def initialize(self):
        self.channel = None

#Check why not working
    # def open(self, channel):
    #     """
    #     Client opens a websocket
    #     """
    #     # self.channel = channel

    def on_message(self, message):
        """
        Message recieved on channel
        """
        #print(f"This message was sent: {message}") # Writes to the console window (server side)
        self.write_message(f"This message was sent: {message}") # Writes message to sender

    def on_close(self):
        """
        Channel is closed
        """
    def check_origin(self, origin):
        """
        Override the origin check if needed
        """
        return True

def main(opts):
    # Create tornado application and supply URL routes
    app = tornado.web.Application(ChannelHandler.urls())

    # Setup http server
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(LISTEN_PORT, LISTEN_ADDRESS)

    # Start IO/Event loop
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main(1)

# using this webserver client side
"""
First you have to create a websocket connection 
//Note the prefix is ws (can be wss for secure)
var ws = new WebSocket("ws://localhost:8000/web-socket/")
//You then have to define the onmessage function
ws.onmessage = function(evt){
    console.log(evt.data);
} 
//You can then send data, that will be handled by the server
ws.send("Some data");
"""    