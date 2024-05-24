import turtle
import random

# Set up the sc
screen = turtle.Screen()
screen.title("Two Cars Game")
screen.bgcolor("white")
screen.setup(width=600, height=400)

# Player 1 car
car1 = turtle.Turtle()
car1.shape("square")
car1.color("blue")
car1.shapesize(stretch_wid=1, stretch_len=2)
car1.penup()
car1.goto(0, -150)

# Player 2 car
car2 = turtle.Turtle()
car2.shape("square")
car2.color("red")
car2.shapesize(stretch_wid=1, stretch_len=2)
car2.penup()
car2.goto(0, 150)

# Score variables
score1 = 0
score2 = 0

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 170)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 12, "normal"))

# Move the cars
def move_car1_left():
    x = car1.xcor()
    x -= 20
    car1.setx(x)

def move_car1_right():
    x = car1.xcor()
    x += 20
    car1.setx(x)

def move_car2_left():
    x = car2.xcor()
    x -= 20
    car2.setx(x)

def move_car2_right():
    x = car2.xcor()
    x += 20
    car2.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_car1_left, "Left")
screen.onkey(move_car1_right, "Right")
screen.onkey(move_car2_left, "a")
screen.onkey(move_car2_right, "d")

# Main game loop
while True:
    # Check for collision
    if car1.distance(car2) < 20:
        print("Collision! Game Over!")
        break

    # Move an obstacle (you can customize this part)
    car2.sety(car2.ycor() - 10)

    # Check if the obstacle is out of the screen
    if car2.ycor() < -200:
        car2.goto(random.randint(-280, 280), 150)

    # Updat
