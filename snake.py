from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        for length in range(0, 3):
            if len(self.snake_body) == 0:
                self.snake_body.append(self.get_part())
            else:
                self.snake_body.append(self.get_part())
        self.head = self.snake_body[0]

    def get_part(self):
        a_part_of_body = Turtle("square")
        a_part_of_body.penup()
        a_part_of_body.color("black")
        a_part_of_body.hideturtle()
        if len(self.snake_body) > 0:
            a_part_of_body.goto(x=self.snake_body[0].xcor() - (len(self.snake_body) * 20), y=self.snake_body[0].ycor())

        return a_part_of_body

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
            self.snake_body[seg_num].showturtle()
        self.snake_body[0].forward(MOVE_DISTANCE)

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

    def collides_with_tail(self):
        for part in self.snake_body[1:]:
            if self.head.distance(part) < 5:
                return True

        return False
