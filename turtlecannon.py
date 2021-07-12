import turtle as t
import random
import time

target = 0
t.title("turtle cannon")
angle = 0
isFiring = False

def init():
    global target
    t.clear()
    t.pensize(1)
    t.color("black")
    t.goto(-300, 0)
    t.down()
    t.goto(300, 0)
    target = random.randint(50,150)
    t.pensize(3)
    t.color("green")
    t.up()
    t.goto(target - 25, 2)
    t.down()
    t.goto(target + 25, 2)
    t.color("black")
    t.up()
    t.goto(-200, 10)
    t.setheading(20)

def turn_up():
    global angle
    if(angle < 90):
        angle+=2
        t.setheading(angle)


def turn_down():
    global angle
    angle-=2
    t.setheading(angle)
    


def fire():
    global isFiring
    if isFiring == False:
        isFiring = True
        ang = t.heading()
        while t.ycor() > 0:
            t.forward(15)
            t.right(5)

        d = t.distance(target, 0)
        t.sety(random.randint(10, 100))
        if d < 25:
            t.color("blue")
            t.write("Good!", False, "center", ("", 15))
            time.sleep(1)
            init()
        else:
            t.color("red")
            t.write("bad!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.setheading(ang)
        isFiring = False

init()



t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
