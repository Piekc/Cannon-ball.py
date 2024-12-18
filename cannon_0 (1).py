"""Cannon, hitting targets with projectiles.

"""

from random import randrange
from turtle import *
from freegames import vector
import math

ball = vector(-200, -200)
v0 = vector(0, 0)
time = 0
targets = []
score = 0

def tap(mx, my):
    global time

    ball.x = -200
    ball.y = -200

    x = abs(-200 - mx) / 25
    y = abs(-200 - my) / 25
    v0.x = x
    v0.y = y

    time = 0


    

def inside(position):
    return -200 < position.x < 200 and -200 < position.y < 200

def draw():
    """Draw ball and targets."""
    clear()
    goto(ball.x, ball.y)
    dot(10,'red')

    for position in targets: 
        goto (position.x, position.y)
        dot(20, 'purple')

    for position in targets:
        position.x -= 3

    goto (-190, 180)
    write(f"Score: {score}", font = ("Arial", 18, "normal") )



    update()



def move():
    global time, score
    """Move ball and targets."""

    if randrange(0,20) == 0:
        x = 180
        y= randrange(-210, 210)
        targets.append(vector(x,y))


    pt_y = (1/2) * (-9.81) * time**2 + v0.y * time
    pt_x = v0.x * time

    ball.x += pt_x
    ball.y += pt_y

    time += 0.03

    for position in targets:
        position += vector(-1, 0)

        d= math.sqrt((position.y - ball.y)**2 + (position.x - ball.x)**2)

        r1 = 5
        r2 = 10


        if (r1 + r2) >= d:

            targets.remove(position)
            score += 1

    






    draw()

    ontimer(move, 30)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
