import turtle

def moveR():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def moveL():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def moveU():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def moveD():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')



turtle.listen()
turtle.onkey(moveR,'d')
turtle.onkey(moveL,'a')
turtle.onkey(moveU,'w')
turtle.onkey(moveD,'s')
turtle.onkey(restart,'Escape')

    
    
