


import turtle
import random

list_of_turtles=[]#list to hold all the turtles


# Creating Race area 
t = turtle.Turtle()  
# To stop the screen to display  
  
t.goto(200, 0)
t.goto(200, -100)
t.goto(-200, -100)
t.goto(-200, 0)
t.goto(0, 0)



#obj.circle(50)#TESTING THE MOVEMENT OF CIRCLE
##
def setup():
    global turtles
    start_line=-201# Currently the starting position is incorrect! You need to fix it.
    screen=turtle.Screen()
    
    

    turtle_ycor=[-80,-60,-40,-20]
    turtle_color=['blue','red','green','yellow']

    for i in range(0,len(turtle_ycor)):
        new_turtle=turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(start_line,turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        list_of_turtles.append(new_turtle)
   
def race():
   global turtles
   winner=False
   finishLine=200
   
   while not winner:
       for current_turtle in list_of_turtles:
            move=random.randint(0,2)
            current_turtle.forward(move)

            xcor=current_turtle.xcor()
            ycor=current_turtle.ycor()
            
            if (xcor>=finishLine):#                #MISSING CODE#
                winner=True
                if ycor==-80:
                    win="blue"
                   
                
                if ycor==-60:
                    win="red"
                    
                
                if ycor==-40:
                    win="green"
                    
                
                if ycor==-20:
                    win="yellow"
                turtle.write("The winner is {0}".format(win), font=("Calibri", 25, "bold"))
                
                
def main():

    setup()
    race()
    turtle.mainloop()
##
##
main()
