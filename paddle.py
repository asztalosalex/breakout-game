from turtle import Turtle

X_MOVE_SPEED = 10
MAX_LEFT = -280
MAX_RIGHT = 280

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.left_pressed = False
        self.right_pressed = False

    def go_left(self):
        if self.xcor() < MAX_LEFT:
            new_x = self.xcor() + X_MOVE_SPEED
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() > MAX_RIGHT:
            new_x = self.xcor() - X_MOVE_SPEED
            self.goto(new_x, self.ycor())

    def check_move(self):
        if self.left_pressed:
            self.go_left()
        if self.right_pressed:
            self.go_right()

    def left_press(self):
        self.left_pressed = True

    def left_release(self):
        self.left_pressed = False

    def right_press(self):
        self.right_pressed = True

    def right_release(self):
        self.right_pressed = False
