import turtle

t=turtle.Pen()
def mystar(size,filled):
    if filled == True:
        t.begin_fill()
    
    for x in range(1,9):
        t.forward(50)
        t.left(45)
    
    if filled == True:
        t.end_fill()

mystar(100,True)
turtle.done()
