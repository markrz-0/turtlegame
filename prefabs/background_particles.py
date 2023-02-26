import random
import turtle

from engine.base import Base
from engine.graphics import Graphics

def clamp(value, min_val, max_val):
    return min(max_val, max(value, min_val))

class Dot:
    def __init__(self, x, y, color, size, speed):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.velocity = (0, 0)
        self.change_velocity = 0

    def random_pos(self):
        max_x = turtle.window_width() // 2
        max_y = turtle.window_height() // 2

        self.x = random.randint(-max_x, max_x)
        self.y = random.randint(-max_y, max_y)

    def move(self):
        if self.change_velocity == 0:
            self.velocity = (
                random.randint(-self.speed, self.speed),
                random.randint(-self.speed, self.speed)
            )
            self.change_velocity = random.randint(15, 6000)

        self.x += self.velocity[0]
        self.y += self.velocity[1]

        max_x = turtle.window_width() // 2
        max_y = turtle.window_height() // 2

        if -max_x - self.size < self.x < max_x + self.size and -max_y - self.size < self.y < max_y + self.size:
            self.change_velocity -= 1
        else:
            self.random_pos()

class Particles(Base):
    def __init__(self):
        super().__init__()
        turtle.bgcolor('black')
        self.dots = []
        for _ in range(100):
            size = random.randint(2, 15)
            speed = random.randint(1, 2)
            color = random.choice(['red', 'magenta', 'yellow', 'blue', 'green', 'cyan'])
            self.dots.append(Dot(0, 0, color, size, speed))

    def load(self):
        for dot in self.dots:
            dot.random_pos()

    def draw(self):
        self.t.clear()
        for dot in self.dots:
            Graphics.dot(self.t, dot.x, dot.y, dot.size, dot.color)
            dot.move()
