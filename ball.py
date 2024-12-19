from turtle import Turtle


BALL_SPEED = 0.009
X_MOVE = 2.5
Y_MOVE = 2.5

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = X_MOVE
        self.y_move = Y_MOVE
        self.move_speed = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = BALL_SPEED
        self.bounce_x()