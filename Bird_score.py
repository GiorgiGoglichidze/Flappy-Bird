import turtle

class Score:
        def __init__(self):
            self.score = 0
            self.title = turtle.Turtle()
            self.title.color("black")
            self.title.speed(0)
            self.title.hideturtle()
            self.title.goto(0, 260)
            self.update_score()

        def update_score(self):
            self.title.clear()
            self.title.write( self.score ,  align="center", font=("Courier", 24, "normal"))

        def increase_score(self):
            self.score += 1
            self.update_score()

        def game_over(self):
            self.title.penup()
            self.title.goto(0, 0)
            self.title.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
