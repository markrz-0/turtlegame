import string
import turtle

from engine.graphics import Graphics
from prefabs.background_particles import Particles
from random_name import random_name
from engine.basescene import BaseScene
from scenes.matchmaking import MatchmakingScreen


class MainMenuScene(BaseScene):
    NAME = 'menu'

    def __init__(self):
        super().__init__()
        self.particles = Particles()
        self.unload_objects.append(self.particles)
        self.load_objects.append(self.particles)
        self.clicked_play = False
        self.nickname = random_name()

    def key_press(self, key):
        self.nickname += key

    def backspace(self):
        self.nickname = self.nickname[:-1]

    def play(self):
        if not self.clicked_play:
            self.shared['nickname'] = self.nickname
            self.clicked_play = True

    def load(self):
        super().load()
        for k in (string.ascii_letters + string.digits + "-_"):
            exec(f"turtle.onkey(lambda: self.key_press('{k}'), '{k}')", {'turtle': turtle, 'self': self}, {})
        turtle.onkey(lambda: self.key_press(' '), 'space')
        turtle.onkey(self.backspace, 'BackSpace')
        turtle.onkey(self.play, 'Return')
        turtle.listen()

    def unload(self):
        super().unload()

        for k in (string.ascii_lowercase + string.digits):
            # noinspection PyTypeChecker
            turtle.onkey(None, k)
        # noinspection PyTypeChecker
        turtle.onkey(None, 'space')
        # noinspection PyTypeChecker
        turtle.onkey(None, 'BackSpace')
        # noinspection PyTypeChecker
        turtle.onkey(None, 'Return')

    def draw(self):
        self.t.clear()

        self.particles.draw()

        edge_y = turtle.window_height() // 2 - 100

        Graphics.text(self.t, 0, edge_y, "Type your nickname", 40, 'white')
        Graphics.text(self.t, 0, 0, "Nickname: " + self.nickname, 40, 'white')
        Graphics.text(self.t, 0, -edge_y, "Press ENTER to play", 40, 'white')

        if self.clicked_play:
            return MatchmakingScreen.NAME

        return self.NAME