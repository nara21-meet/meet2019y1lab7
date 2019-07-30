import turtle
import random

turtle.tracer(1,0)

size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=6
time_step=100

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")
turtle.hideturtle()

def new_stamp():
    snake_pos=snake.pos()
    pos_list.append(snake_pos)
    stamp_list=snake.stamp()
    
for counter in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=(SQUARE_SIZE)
    snake.goto(x_pos,y_pos)


def remove_tail():
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

def up():
    snake.direction="up"
    move.snake()
    print["you pressed the 'up' key"]

def down:
    snake.direction="down"
    move.snake()
    print["you pressed the 'down' key"]

def left:
    snake.direction="left"
    move.snake()
    print["you pressed the 'left' key']

def right;
    snake.direction="right"
    move.snake()
    print["you pressed the 'right' key"]


turtle.mainloop()
