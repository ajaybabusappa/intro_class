import turtle  
Turtle = turtle.Turtle() 
Window = turtle.Screen() 
  
# Turtle to draw a spiral 
def drawSpiral(myTurtle, linelen): 
    Turtle.forward(linelen) 
    Turtle.right(90) 
    drawSpiral(Turtle, linelen - 10) 

drawSpiral(Turtle, 80) 
Window.exitonclick()
