import json
import socket
import threading
import turtle

from config import *
from engine.graphics import Graphics
from engine.basescene import BaseScene

class Status:
    WAITING = 'Waiting for players...'
    PLAYING = ''
    WIN = 'VICTORY'
    LOST = 'DEFEAT'

class Dot:
    def __init__(self, color, size, x, y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

class PlayScene(BaseScene):
    NAME = 'play'

    def __init__(self):
        super().__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = Status.WAITING

        self.your_score = 0
        self.enemy_score = 0

        self.whois_playing = ""

        self.key_stack = []

        self.players = []
        for _ in range(PLAYERS_PER_GAME):
            t = turtle.Turtle()
            t.penup()
            t.shape('turtle')
            self.players.append(t)


    def load(self):
        super().load()

        start_x = -(SIZE[0] // 2)
        start_y = -(SIZE[1] // 2)

        Graphics.rect(self.t2, start_x, start_y, SIZE[0], SIZE[1], color='white', fill='black')

        self.s: socket.socket = self.shared['socket']

        self.s.send(json.dumps({'code': Signals.READY, 'name': self.shared['nickname']}).encode('utf-8'))

        # GAME READY SIGNAL
        data = json.loads(self.s.recv(BUF_SIZE).decode('utf-8'))
        self.whois_playing = data['name']

        self.status = Status.PLAYING

        turtle.onkey(self.up, 'w')
        turtle.onkey(self.left, 'a')
        turtle.onkey(self.down, 's')
        turtle.onkey(self.right, 'd')
        turtle.listen()


    def up(self):
        print("UP")
        self.key_stack.append(Signals.MOVE_UP)

    def down(self):
        print("DOWN")
        self.key_stack.append(Signals.MOVE_DOWN)

    def right(self):
        print("RIGHT")
        self.key_stack.append(Signals.MOVE_RIGHT)

    def left(self):
        print("LEFT")
        self.key_stack.append(Signals.MOVE_LEFT)


    def unload(self):
        super().unload()
        # noinspection PyTypeChecker
        turtle.onkey(None, 'w')
        # noinspection PyTypeChecker
        turtle.onkey(None, 'a')
        # noinspection PyTypeChecker
        turtle.onkey(None, 's')
        # noinspection PyTypeChecker
        turtle.onkey(None, 'd')
        turtle.listen()

    def draw(self):
        self.t.clear()

        edge_y = turtle.window_height() // 2 - 100

        Graphics.text(self.t, 0, edge_y, f"Your score: {self.your_score} Enemy score: {self.enemy_score}", 40, 'white')
        Graphics.text(self.t, 0, edge_y - 50, self.whois_playing, 12, 'white')
        Graphics.text(self.t, 0, -edge_y, self.status, 40, 'white')

        if self.status == Status.PLAYING:
            data = json.loads(self.s.recv(BUF_SIZE).decode('utf-8'))
            if data['code'] == Signals.GAME_UPDATE:

                players = data['p']
                for p, p_data in zip(self.players, players):
                    p.color(p_data['color'])
                    p.goto(p_data['x'], p_data['y'])
                    p.setheading(p_data['angle'])

                self.your_score = data['y']
                self.enemy_score = data['e']

                self.t3.clear()

                for d_data in data['d']:
                    Graphics.dot(self.t3, d_data[0], d_data[1], d_data[2], ['magenta', 'yellow', 'cyan', 'white'][d_data[3]])

            elif data['code'] == Signals.WIN:
                self.status = Status.WIN
            elif data['code'] == Signals.LOST:
                self.status = Status.LOST

            if len(self.key_stack) == 0:
                self.s.send(json.dumps({'code': Signals.READY}).encode('utf-8'))
            else:
                self.s.send(json.dumps({'code': self.key_stack.pop(0)}).encode('utf-8'))

        return self.NAME