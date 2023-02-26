from engine.base import Base


class BaseScene(Base):
    NAME = 'unset'

    def __init__(self):
        super().__init__()
        # objects to be automatically drew
        self.draw_objects: list[Base] = []
        # objects to be automatically unloaded on scene exit
        self.unload_objects: list[Base] = []
        # objects to be automatically call on scene load
        self.load_objects: list[Base] = []
        self.shared = {}

        self.active = False

    def unload(self):
        self.active = False
        self.t.clear()
        for obj in self.unload_objects:
            obj.t.clear()

    def draw_objects(self):
        for obj in self.draw_objects:
            obj.draw()

    def load(self):
        self.active = True
        for obj in self.load_objects:
            obj.load()

    def draw(self):
        """
        :return: new scene name
        """
        return self.NAME