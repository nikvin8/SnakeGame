from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()
        score.new_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        snake.head.goto((snake.head.xcor() * -1), snake.head.ycor())

    if snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), (snake.head.ycor() * -1))

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
