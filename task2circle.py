

import turtle
import time
import random

turtle.setup(800,600)
board = turtle.Turtle()

 
circle_positions = [(-120,0,"blue"), (0,0,"black"), (120,0,"red"),
                    (-60,-100,"yellow"), (60,-100,"green")]
tut=["blue","black","red","yellow","green"]
i=0
fast=[0,0,0,0,0]
for pos in circle_positions:
  start=time.time()
  board.penup()
  board.setpos(pos[0],pos[1])
  board.pencolor(pos[2])
  board.pensize(5)
  board.pendown()
  board.circle(50)
  move=random.randint(0,2)
  board.forward(move)
  end=time.time()
  fast[i]=end-start
  i=i+1

win = fast.index(min(fast))
winner=tut[win]
print('The winner is',winner)
turtle.write("The winner is {0}".format(winner), font=("Calibri", 25, "bold"))
turtle.done()