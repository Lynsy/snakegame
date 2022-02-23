from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
COLLISION_DISTANCE_WALL = 300
EDGE = 20


def reset_game():
    global snake
    global food
    global scoreboard
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("DarkOliveGreen4")
screen.title("Snake, Snake, Snaaake!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_body.append(snake.get_part())
        scoreboard.add_score()

    if snake.head.xcor() > COLLISION_DISTANCE_WALL or snake.head.xcor() < (-1 * (COLLISION_DISTANCE_WALL + EDGE)) or \
            snake.head.ycor() > (COLLISION_DISTANCE_WALL + EDGE) or snake.head.ycor() < (
            -1 * COLLISION_DISTANCE_WALL):
        game_on = False
        scoreboard.game_over()

    if snake.collides_with_tail():
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
