import turtle


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("yellow")
        self.speed = 3
        
        self.dy = 0

    def jump(self):
        self.dy = 9

    def move(self):
        y = self.ycor()
        y += self.dy
        self.sety(y)
