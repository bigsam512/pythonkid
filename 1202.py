import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=500, bg='lightyellow')
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
aa=[[5,0],[0,5],[-5,0],[0,-5]]
for a in range(0,4):
    for x in range(0,30):
        canvas.move(1,aa[a][0],aa[a][1])
        tk.update()
        time.sleep(0.1)
