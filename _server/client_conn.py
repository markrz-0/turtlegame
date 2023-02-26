import socket
import time

class ClientConnection:
    def __init__(self, conn: socket.socket, addr):
        self.conn: socket.socket = conn
        self.addr = addr
        self.space_pressed = False
        self.last_recv = time.time()