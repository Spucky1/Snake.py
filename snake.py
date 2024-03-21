import turtle
import time 
import random

delay = 0.1
score = 0
highscore = 0

wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("blue")

wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
def goup():
 if head.direction != "down":
    head.direction ="up"
def goDown():
    if head.direction !="up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x =  head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segements = []

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor < -290:
       time.sleep(1)
       head.goto(0,0)
       head.direction = "Stop"
       colors = random.choice(['red', 'blue', 'green'])
       shapes = random.choice(['square', 'circle'])
       for segement in segements:
        segement.goto(1000, 1000)
        segements.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} highscore : {}".format (score,highscore), align = "center", font=("candara", 24, "bold"))


