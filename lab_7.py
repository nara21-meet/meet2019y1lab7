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
    new_stamp()

snake.direction="up"
TOP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

turtle.onkeypress("up")
turtle.onkeypress("down")
turtle.onkeypress("left")
turtle.onkeypress("right")




def remove_tail():
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

def up():
    snake.direction="up"
    
    print["you pressed the 'up' key"]

def down():
    snake.direction="down"
    
    print["you pressed the 'down' key"]

def left():
    snake.direction="left"
    
    print["you pressed the 'left' key"]

def right():
    snake.direction="right"
    
    print["you pressed the 'right' key"]

def move_snake():
    if snake.direction=="Up":
        snake.goto(x_pos_y_pos+SQUARE_SIZE)
        print("you moved up")
    elif snake.direction=="Down" :
        snake.goto(x_pos_y_pos+SQUARE_SIZE)
        print("you moved down")
    elif snake.direction=="Left":
        snake.goto(x_pos_y_pos+SQUARE_SIZE)
        print("you moved left")
    elif snake.direction=="Right":
        snake.goto(x_pos_y_pos+SQUARE_SIZE)
        print("you moved right")    
    
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_Y_pos=new_pos[1]
    if new_x_pos<=LEFT_EDGE:
       print('you hit the left edge! Game over!')
    if new_x_pos<=RIGHT_EDGE:
       print('you hit the right edge! Game over!')
    if new_x_pos<=TOP_EDGE:
      print ('you hit the top edge! Game over!')
    if new_x_pos<=DOWN_EDGE:
      print ('you hit the bottom edge! Game over!')
    remove_tail()
    new_stamp()
    turtle.ontimer(move_snake,time_step)
move_snake()
turtle.listen()
turtle.mainloop()
