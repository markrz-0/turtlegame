import threading
import time
import json
from _server.client_conn import ClientConnection
from _server import game
from config import *

class Matchmaking:
    def __init__(self):
        # using list as stack
        self.connected: list[ClientConnection] = []

    def add_connection(self, client: ClientConnection) -> None:
        self.connected.append(client)

    def start(self):
        while True:
            time.sleep(1/60)
            if len(self.connected) >= PLAYERS_PER_GAME:
                team_1 = []
                for _ in range(PLAYERS_PER_GAME // 2):
                    cl = self.connected.pop(0)
                    team_1.append(cl)
                team_2 = []
                for _ in range(PLAYERS_PER_GAME // 2):
                    cl = self.connected.pop(0)
                    team_2.append(cl)

                g = game.Game()
                threading.Thread(target=g.create, args=(team_1, team_2)).start()
            else:
                for cl in self.connected:
                    cl.conn.send(
                        json.dumps({
                            'code': Signals.WAITING,
                            'clients': len(self.connected),
                            'max': PLAYERS_PER_GAME
                        }).encode('utf-8')
                    )