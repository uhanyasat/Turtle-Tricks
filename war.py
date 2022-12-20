# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:10:23 2021

@author: Sathish
"""




import turtle
import random

list_of_turtles=[]#list to hold all the turtles


# Creating Race area 
t = turtle.Turtle()  
# To stop the screen to display  
  



#obj.circle(50)#TESTING THE MOVEMENT OF CIRCLE
##
def setup():
    global turtles,new_turtle1,new_turtle
    start_line=0# Currently the starting position is incorrect! You need to fix it.
    screen=turtle.Screen()
    
    

    
    

   
    new_turtle=turtle.Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.setpos(-200,0)
    new_turtle.color('blue')
    new_turtle.pendown()
        
    new_turtle1=turtle.Turtle()
    new_turtle1.shape('turtle')
    new_turtle1.penup()
    new_turtle1.setpos(200,0)
    new_turtle1.color('red')
    new_turtle1.pendown()
        
   
def race():
   global turtle, new_turtle1,new_turtle
   winner=False
   finishLine=200
   
   while not winner:
       
            move=random.randint(0,2)
            new_turtle.forward(move)
            move2=random.randint(0,2)
            new_turtle1.backward(move2)

           
            
            if (new_turtle1.xcor() < 0) and (new_turtle.xcor() < 0):
                winner=True
                turtlee=new_turtle
                wtur='red'
                turtle.write("The winner is red", font=("Calibri", 25, "bold"))
            if (new_turtle1.xcor() > 0) and (new_turtle.xcor() > 0):
                winner=True
                wtur='blue'
                turtlee=new_turtle1
                turtle.write("The winner is blue", font=("Calibri", 25, "bold"))
            
   turtlee.clear()
                
                
def main():

    setup()
    race()
    turtle.mainloop()
##
##
main()
