from socketserver import *
class Server(ThreadingMixIn,UDPServer):
    pass
class Handler(DatagramRequestHandler):
    def handle(self):
        #self.request===>accept返回的套接字
       
        while True:
            data=self.rfile.readline()
            print(self.client_address)
            if not data:
                break
            print(data)
            self.wfile.write(b'receive')

if __name__ == "__main__":
    server_addr = ("0.0.0.0",8888)
    #c穿件服务器对象
    server = Server(server_addr,Handler)

    server.serve_forever()