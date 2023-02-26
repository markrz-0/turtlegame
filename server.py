import threading
from _server import listener, matchmaking

class Server:
    def __init__(self):
        self.listener = listener.Listener()
        self.backend = matchmaking.Matchmaking()

    def run(self):
        threading.Thread(target=self.listener.start,
                         args=(self.backend.add_connection,)).start()

        threading.Thread(target=self.backend.start).start()


if __name__ == '__main__':
    server = Server()
    server.run()