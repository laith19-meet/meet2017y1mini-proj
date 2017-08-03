import turtle
import random  
turtle.tracer(1,0)
#window size
SIZE_X=815
SIZE_Y=540
turtle.setup(SIZE_X, SIZE_Y) 

turtle.penup()
#snake size
SQUARE_SIZE = 20
START_LENGTH = 6
#lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#snake color and shape
snake = turtle.clone()
snake.shape("circle")
snake.color("red")
turtle.hideturtle()

for num in range (START_LENGTH) :
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos = x_pos + SQUARE_SIZE

    my_pos= (x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    my_stamp = snake.stamp()
    stamp_list.append(my_stamp)
# arrows
UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
time_step = 100
SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction = UP
    print("you pressed the up key !")
    
def left():
    global direction
    direction = LEFT
    print("you pressed the left key !")
    
def down(): 
    global direction
    direction = DOWN
    print("you pressed the down key !")

def right():    
    global direction
    direction = RIGHT
    print("you pressed the right key !")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
#moving the snake
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
        
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
        
    elif direction==UP:
        snake.goto(x_pos , y_pos + SQUARE_SIZE)
        print("you moved up!")

    elif direction==DOWN:
        snake.goto(x_pos , y_pos - SQUARE_SIZE)
        print("you moved down!")
        
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eatent the food!")
        make_food()
        add_numbers() 
        

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)



    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("you hit the rtight edge! game over !")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over !")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("you hit the top edge! game over !")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("you hit the bottom edge! game over !")
        quit()

    if snake.pos() in pos_list[:-2] :
        print ("you hit your self! bye !")
        quit()
    turtle.ontimer(move_snake,time_step)

move_snake()

turtle.register_shape("1234.gif")
food_pos = [(100,100) , (-100,100) , (-100,-100) , (100,-100)]
food = turtle.clone()
food.shape("1234.gif")
# to let the snake grow when you eat
def grow_snake():
    stamp3 = snake.stamp()
    stamp_list.append(stamp3)
    pos_list.append(stamp3)


for this_food_pos in food_pos :
    food.goto (this_food_pos)
    stampo=food.stamp()
    food_stamps.append(stampo)
# to make the turtle make food
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto (food_x,food_y)
    stamp1 = food.stamp()
    food_stamps.append(stamp1)
    food_pos.append(food.pos())
    grow_snake()

score_turtle = turtle.clone()
C=0
def add_numbers() :        #to make turtle count
    global C
    C = C + 1
    score_turtle.clear()
    score_turtle.write(C)
    score_turtle.goto(370,230)

# make the borders
turtle_border = turtle.clone()
    
turtle_border.goto(400,280)
turtle_border.pensize(7)
turtle_border.color("brown")
turtle_border.pendown()
turtle_border.goto(400,-260)
turtle_border.goto(-400,-260)
turtle_border.goto(-400,260)
turtle_border.goto(400,260)

#change the background color
bgpic("123.gif")




































































































