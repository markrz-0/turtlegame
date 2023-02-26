import json
import math
import threading
import time
import random

from config import *
from _server.client_conn import ClientConnection

def clamp(value, min_val, max_val):
    return min(max_val, max(min_val, value))

def dist(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx * dx + dy * dy)

class Dot:
    def __init__(self, color, size, x, y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.enabled = True

    def to_json(self):
        return [
            self.x, self.y, self.size, self.color
        ]

class Player:
    def __init__(self, client_conn: ClientConnection, x, y, rot, team, index):
        self.client_conn = client_conn
        self.x = x
        self.y = y
        self.rot = rot
        self.team = team
        self.index = index

    def to_json(self, team, player):
        out = {
            'x': self.x,
            'y': self.y,
            'angle': self.rot,
        }
        if team == self.team:
            if self.index == player:
                out['color'] = 'green'
            else:
                out['color'] = 'blue'
        else:
            out['color'] = 'red'

        return out

class Game:
    def __init__(self):
        self.team_1: list[ClientConnection] = []
        self.team_2: list[ClientConnection] = []
        self.active = False
        self.team1_score = 0
        self.team2_score = 0
        self.players: list[Player] = []
        self.dots = []
        self.dot_data = []


    def calc_dot_data(self):
        self.dot_data = [d.to_json() for d in self.dots if d.enabled]

    def handle_client(self, player: Player):
        client_conn = player.client_conn
        last_send = True
        while self.active or last_send:

            if not self.active:
                last_send = False


            player_data = [p.to_json(player.team, player.index) for p in self.players]

            to_send = {
                'code': Signals.GAME_UPDATE,
                'p': player_data,
                'd': self.dot_data,
                'y': self.team1_score if player.team == 1 else self.team2_score,
                'e': self.team1_score if player.team == 2 else self.team2_score
            }

            client_conn.conn.send(json.dumps(to_send).encode('utf-8'))

            data = json.loads(client_conn.conn.recv(BUF_SIZE).decode('utf-8'))
            if data['code'] == Signals.MOVE_UP:
                player.y += PLAYER_SPEED
                player.rot = 90
            elif data['code'] == Signals.MOVE_DOWN:
                player.y -= PLAYER_SPEED
                player.rot = 270
            elif data['code'] == Signals.MOVE_LEFT:
                player.x -= PLAYER_SPEED
                player.rot = 180
            elif data['code'] == Signals.MOVE_RIGHT:
                player.x += PLAYER_SPEED
                player.rot = 0

            dx = SIZE[0] // 2
            dy = SIZE[1] // 2
            player.x = clamp(player.x, -dx, dx)
            player.y = clamp(player.y, -dy, dy)

            client_conn.last_recv = time.time()

        has_won = (self.team1_score > self.team2_score) if player.team == 1 else (self.team2_score > self.team1_score)

        client_conn.conn.send(json.dumps({
            'code': Signals.WIN if has_won else Signals.LOST
        }).encode('utf-8'))

    def add_random_dot(self):
        dx = SIZE[0] // 2
        dy = SIZE[1] // 2

        x = 0
        y = 0
        regenerate = True
        while regenerate:
            regenerate = False
            x = random.randint(-dx, dx)
            y = random.randint(-dy, dy)
            for player in self.players:
                if dist(player.x, player.y, x, y) < 3 * PLAYER_SPEED:
                    regenerate = True


        d = Dot(random.randint(0, 3), random.randint(3, 7), x, y)
        self.dots.append(d)

    def spawn_dots(self):
        for _ in range(10 * PLAYERS_PER_GAME):
            self.add_random_dot()
        self.calc_dot_data()
        while self.active:
            time.sleep(random.randint(2, 5))
            self.add_random_dot()
            self.calc_dot_data()

    def create(self, team_1:  list[ClientConnection], team_2:  list[ClientConnection]):
        self.active = True
        self.team_1 = team_1
        self.team_2 = team_2

        threading.Thread(target=self.spawn_dots).start()

        for cl in [*self.team_1, *self.team_2]:
            cl.conn.send(json.dumps({'code': Signals.READY}).encode('utf-8'))

        whois_playing1 = ''
        for cl in self.team_1:
            data = json.loads(cl.conn.recv(BUF_SIZE).decode('utf-8'))
            name = data['name']
            whois_playing1 += name + ", "

        # removing last ', '
        whois_playing1 = whois_playing1[:-2]

        whois_playing2 = ''
        for cl in self.team_2:
            data = json.loads(cl.conn.recv(BUF_SIZE).decode('utf-8'))
            name = data['name']
            whois_playing2 += name + ", "
        whois_playing2 = whois_playing2[:-2]


        whois_playing1, whois_playing2 =\
            whois_playing1 + "   VS   " + whois_playing2,\
            whois_playing2 + "   VS   " + whois_playing1

        y_offset = int((SIZE[1] - PLAYER_INIT_Y_OFFSET) // (PLAYERS_PER_GAME // 2))
        y_start = -SIZE[1] // 2 + PLAYER_INIT_Y_OFFSET

        player_index = 0
        for i, cl in enumerate(self.team_1):

            p = Player(cl, -PLAYER_INIT_X, y_start + y_offset * i, 90, 1, player_index)
            self.players.append(p)

            cl.conn.send(json.dumps({'code': Signals.GAME_INIT, 'name': whois_playing1}).encode('utf-8'))
            threading.Thread(target=self.handle_client, args=(p, )).start()
            player_index += 1

        for i, cl in enumerate(self.team_2):

            p = Player(cl, PLAYER_INIT_X, y_start + y_offset * i, -90, 2, player_index)
            self.players.append(p)

            cl.conn.send(json.dumps({'code': Signals.GAME_INIT, 'name': whois_playing2}).encode('utf-8'))
            player_index += 1
            t = threading.Thread(target=self.handle_client, args=(p, ))
            t.start()

            player_index += 1


        while self.active:
            dot_deletions = 0
            for player in self.players:
                for dot in self.dots:
                    if dot.enabled and dist(player.x, player.y, dot.x, dot.y) <= dot.size + PLAYER_SPEED:
                        if player.team == 1:
                            self.team1_score += dot.size
                        else:
                            self.team2_score += dot.size

                        dot.enabled = False
                        dot_deletions += 1

            if dot_deletions > 0:
                for _ in range(dot_deletions):
                    self.add_random_dot()
                self.calc_dot_data()


            # TODO: refactor
            if self.team2_score < GOAL and self.team1_score < GOAL:
                pass
            else:
                self.active = False
                break

            time.sleep(1/60)