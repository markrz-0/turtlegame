import socket
from _server import client_conn
from config import *

class Listener:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', PORT))

    def start(self, on_connect):
        """
        :param on_connect: callback with arg (_server.client.Client)
        :return:
        """
        print("LISTENING ON PORT", PORT)
        self.s.listen()
        while True:
            conn, addr = self.s.accept()
            print("Accepted connection from", addr)
            on_connect(client_conn.ClientConnection(conn, addr))