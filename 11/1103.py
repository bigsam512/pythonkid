import turtle

t=turtle.Pen()
def draw_star(size,points):
    
    for x in range(points):
        t.forward(size)
        t.left(144)
    

draw_star(100,5)
turtle.done()
