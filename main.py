import turtle
from turtle import Screen ,Turtle,distance
import  time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mine Sname Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
wall =[(0,290),(0,-290),(290,0),(-290,0)]

game_is_on =True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increasscore()

    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()> 280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()

    for  part in snake.segments[1:]:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10 :
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

