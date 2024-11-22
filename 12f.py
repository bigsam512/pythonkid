import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=500, bg='lightyellow')
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
canvas.create_polygon(20,10,20,60,60,35)
for x in range(0,60):
    canvas.move(1,5,6)
    tk.update()
    time.sleep(0.024)
tk.mainloop()
