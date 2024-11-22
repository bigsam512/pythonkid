from tkinter import *
import random
import time

tk = Tk()
canvas=Canvas(tk, width=500, height=500,bg='lightyellow')
canvas.pack()

def triangle(width, height):
    x1,y1=random.randrange(width),random.randrange(height)
    x2,y2=random.randrange(width),random.randrange(height)
    x3,y3=random.randrange(width),random.randrange(height)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill="", outline="red")

for x in range(1,551):
    triangle(500,500)
    canvas.update()
    time.sleep(0.01)

tk.mainloop()
