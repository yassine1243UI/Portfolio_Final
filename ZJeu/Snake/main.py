#import
import turtle
import random
import time

# Fichier python avec votre jeu Snake

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

# Crée la fenêtre graphique

screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

#Crée la bordure

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.pendown()
turtle.goto(-310, 250)
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()


# score

score = 0;
delay = 0.1;

# snake

snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'


#food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(30, 30)

old_food = []

# tableau de score

tbscore = turtle.Turtle()
tbscore.speed(0)
tbscore.color("white")
tbscore.penup()
tbscore.hideturtle()
tbscore.goto(0, 30)
tbscore.write("Score ", align="center", font=("Courier", 24, "bold"))

# Définition mouvement

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

# détecter les touches

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_right, "Right")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")


while True:
    screen.update()

    #Snake & fruit colision
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        tbscore.clear()
        score += 1
        tbscore.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -=0.001

        #New FOOD
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("red")
        new_food.penup()
        old_food.append(new_food)


    #agrandire le corps du serpent
    for index in range (len(old_food) -1, 0, -1):
        a = old_food[index-1].xcor()
        b = old_food[index-1].ycor()

        old_food[index].goto(a,b)
    
    if len(old_food) > 0: 
        a = snake.xcor()
        b = snake.ycor()
        snake.penup()

        old_food[0].goto(a,b)

    snake_move()

    #Colision bordure
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240 :
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        tbscore.goto(0,0)
        tbscore.write("    GAME OVER \n Your score is {}: {}".format(score, ""), align="center", font=("Courier", 24, "bold"))



    #snake colision 

    for old_food_piece in old_food:
        if old_food_piece.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            tbscore.goto(0, 0)
            tbscore.write("    GAME OVER \n Your score is: {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

turtle.Terminator