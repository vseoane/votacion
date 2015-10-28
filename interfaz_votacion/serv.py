import SimpleHTTPServer
import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

port = 8000
while True:
    try:
        httpd = SocketServer.TCPServer(('', port), Handler)
        print ('Serving on port', port)
        httpd.serve_forever()
    except SocketServer.socket.error as exc:
        if exc.args[0] != 48:
            raise
        print ('Port', port, 'already in use')
        port += 1
    else:
        break