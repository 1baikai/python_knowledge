from socketserver import *
class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        #self.request===>accept返回的套接字
        print("connect from",self.request.getpeername())
        while True:
            data =self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'receive')

if __name__ == "__main__":
    server_addr = ("0.0.0.0",8888)
    #c穿件服务器对象
    server = Server(server_addr,Handler)

    server.serve_forever()