import turtle
import random
from Bird_player import Player


class Map:
    def __init__(self):

        self.height = 20

        self.pipeTop = turtle.Turtle()
        self.pipeTop.color("green")
        self.pipeTop.shape("square")
        self.pipeTop.dx = -5


        self.pipeBot = turtle.Turtle()
        self.pipeBot.color("green")
        self.pipeBot.shape("square")
        self.pipeBot.dx = -5


    def draw_pipe(self):
        r = random.randint(0,40)
        self.pipeBot.penup()
        self.pipeTop.penup()
        self.pipeBot.setx(800)
        self.pipeBot.sety(-400)
        self.pipeTop.goto(800,400)
        self.pipeTop.height = self.height + r
        self.pipeBot.height = 65 - 15 - r
        self.pipeTop.shapesize(stretch_wid=(self.pipeTop.height),stretch_len=3,outline= None)
        self.pipeBot.shapesize(stretch_wid=(self.pipeBot.height),stretch_len=3,outline= None)

    def movePipe(self):

        x = self.pipeTop.xcor()
        x += self.pipeTop.dx
        self.pipeTop.setx(x)

        x1 = self.pipeBot.xcor()
        x1 += self.pipeBot.dx
        self.pipeBot.setx(x1)

    def undraw_column(self):
        self.pipeBot.clear()
        self.pipeTop.clear()
    
    def collision(self,p):
        if (p.xcor() + 30 > self.pipeTop.xcor() - 30) and (p.xcor() - 30 < self.pipeTop.xcor() + 30):
            if (p.ycor() > 400 - self.pipeTop.height * 10) or (p.ycor() <  -400 + self.pipeBot.height * 10):
                return True
            else:
                return False
