from turtle import Screen, Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_square(pos)
    def add_square(self, pos):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(pos)
        self.snakes.append(square)

    def extend(self):
        self.add_square(self.snakes[-1].position())
    def move(self):
        for square_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[square_num - 1].xcor()
            new_y = self.snakes[square_num - 1].ycor()
            self.snakes[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




