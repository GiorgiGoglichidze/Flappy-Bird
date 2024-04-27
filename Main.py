import turtle
import time
import random
from Bird_player import Player
from Bird_map import Map
from Bird_score import Score

def game():

    window = turtle.Screen()
    window.bgcolor("skyblue")
    window.title("Flappy Bird")
    window.setup(width=800,height=800)
    window.tracer(0, 0)

    GRAVITY = -0.5

    player = Player()

    sc = Score()

    window.listen()
    window.onkeypress(player.jump, "space")

    while True:
        column = Map()
        column.draw_pipe()
        time.sleep(0.02)
        flag = True
        while column.pipeTop.xcor() > -430:

            time.sleep(0.002) 

            #Gravity
            player.dy += GRAVITY 

            #player jumping
            player.move()


            #Map moving
            column.movePipe()

            #Check for Collisions

            if column.collision(player):
                sc.update_score()
                sc.game_over()
                time.sleep(3)
                window.clear()
                game()
                flag = False

                window.update()

            #Check for Score
            if column.pipeTop.xcor() + 30 < player.xcor() - 10:
                if flag:
                    sc.increase_score()
                    flag = False



            sc.update_score()

            window.update()



game()
