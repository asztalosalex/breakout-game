from paddle import Paddle
from ball import Ball
from turtle import Screen

def main():
    paddle = Paddle((0, -250))
    ball = Ball()

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Brekaout")
    screen.tracer(0)
    screen.listen()
    screen.onkey(paddle.left_press, "A")
    screen.onkey(paddle.right_press, "D")
    screen.onkey(paddle.left_release, "A")
    screen.onkey(paddle.right_release, "D")



    game_is_on = True
    
    while game_is_on:
        screen.update()
        ball.move()
        paddle.check_move()

        screen.exitonclick()

if __name__ == "__main__":
    main()