import turtle
from engine.graphics import Graphics
from prefabs.background_particles import Particles
from engine.basescene import BaseScene


class ErrorScene(BaseScene):
    NAME = 'error'

    def __init__(self):
        super().__init__()
        self.particles = Particles()
        self.unload_objects.append(self.particles)
        self.load_objects.append(self.particles)

    def draw(self):
        self.t.clear()

        self.particles.draw()

        Graphics.text(self.t, 0, 0, f"ERR {self.shared['err']}\n", 40, 'white')
        Graphics.text(self.t, 0, 0, f"\nrestart the game", 40, 'white')

        return self.NAME