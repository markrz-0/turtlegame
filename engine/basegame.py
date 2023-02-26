import time
import turtle
from engine.basescene import BaseScene


class BaseGame:
    def __init__(self):
        turtle.tracer(0, 0)
        self.t = turtle.Turtle()
        self.t.shape('blank')
        self.scenes: dict[str, BaseScene] = {}
        self.active_scene = ''
        self.shared = {}

    def title(self, name):
        turtle.title(name)

    def start(self):
        self.scenes[self.active_scene].load()

    def add_scene(self, scene):
        if self.active_scene == '':
            self.active_scene = scene.NAME
        if scene.NAME not in self.scenes.keys():
            self.scenes[scene.NAME] = scene()

    def update(self):
        self.t.clear()

        new_scene = self.scenes[self.active_scene].draw()
        if new_scene != self.active_scene:
            self.shared = self.scenes[self.active_scene].shared
            self.scenes[self.active_scene].unload()

            self.active_scene = new_scene

            self.scenes[self.active_scene].shared = self.shared
            self.scenes[self.active_scene].load()


    def loop(self):
        self.start()
        while True:
            self.update()
            turtle.update()

            time.sleep(1/30)