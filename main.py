import turtle

wn = turtle.Screen()
wn.title("balls by Rushav")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0


# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("Yellow")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)



# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("Red")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("White")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.5
Ball.dy = -0.5


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))




# Fucntions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard Binding
wn.listen()
wn.onkey(paddle_1_up, "w")

wn.listen()
wn.onkey(paddle_1_down, "s")

wn.listen()
wn.onkey(paddle_2_up, "Up")

wn.listen()
wn.onkey(paddle_2_down, "Down")



# Main game code
while True:
    wn.update()

    # Move ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Boarder Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1



    if Ball.xcor() > 390:

        Ball.goto(0, 0)
        Ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))


    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))


    # Bounce
    if (Ball.xcor() > 340 and Ball.xcor() <  350) and (Ball.ycor() < paddle_2.ycor() + 40 and Ball.ycor() > paddle_2.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (
            Ball.ycor() < paddle_1.ycor() + 40 and Ball.ycor() > paddle_1.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1






