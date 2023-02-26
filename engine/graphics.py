import turtle

class Graphics:
    @classmethod
    def text(cls, t: turtle.Turtle, x, y, text, size=10, color='black'):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor(color)
        t.write(text, align='center', font=('Arial', size, 'normal'))
        t.penup()

    @classmethod
    def dot(cls, t:turtle.Turtle, x, y, size, color='black'):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(size, color)
        t.penup()

    @classmethod
    def rect(cls, t:turtle.Turtle, x, y, width, height, color='black', fill='black'):
        t.penup()
        t.goto(x, y)
        t.pencolor(color)
        t.fillcolor(fill)
        t.pendown()
        t.begin_fill()
        t.goto(x + width, y)
        t.goto(x + width, y + height)
        t.goto(x, y + height)
        t.goto(x, y)
        t.end_fill()
        t.penup()

    @classmethod
    def line(cls, t:turtle.Turtle, start, end, width, color='black'):
        t.penup()
        t.goto(start[0], start[1])
        t.pencolor(color)
        t.pensize(width)
        t.pendown()
        t.goto(end[0], end[1])
        t.penup()