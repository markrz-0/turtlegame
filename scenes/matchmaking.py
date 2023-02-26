import threading
import turtle
import json
import socket

from engine.graphics import Graphics
from engine.basescene import BaseScene
from prefabs.background_particles import Particles
from config import *
from scenes.play import PlayScene


class MatchmakingScreen(BaseScene):
    NAME = 'matchmaking'

    def __init__(self):
        super().__init__()
        self.particles = Particles()
        self.unload_objects.append(self.particles)
        self.load_objects.append(self.particles)
        self.waiting = True
        self.error = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg = 'Connecting to server...'

    def wait_for_match(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.shared['socket'] = self.s
            self.s.connect((SERVER_IP, PORT))
            self.msg = 'Matchmaking...'
            while self.waiting:
                data = self.s.recv(BUF_SIZE).decode('utf-8')
                data = json.loads(data)
                if data['code'] == Signals.WAITING:
                    self.msg = f"Matchmaking ({data['clients']}/{data['max']})"
                elif data['code'] == Signals.FULL:
                    self.msg = f"Matchmaking..."
                elif data['code'] == Signals.READY:
                    self.waiting = False
                    self.msg = "Ready"
        except ConnectionRefusedError:
            self.shared['err'] = 'CONN_REFUSED'
            self.error = True

    def load(self):
        super().load()
        turtle.title(f"Playing as {self.shared['nickname']} - matchmaking")

        threading.Thread(target=self.wait_for_match).start()

    def draw(self):
        self.t.clear()

        self.particles.draw()

        Graphics.text(self.t, 0, 0, self.msg, 40, 'white')

        if self.error:
            return 'error'

        if not self.waiting:
            return PlayScene.NAME

        return self.NAME