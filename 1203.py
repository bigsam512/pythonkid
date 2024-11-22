import time
from tkinter import *
tk= Tk()
canvas = Canvas(tk,width=400, height=400,bg='lightyellow')
canvas.pack()
sam_image=PhotoImage(file='~/Pictures/small.gif')
canvas.create_image(0,0,anchor=NW, image=sam_image)
aa=[[5,0],[0,5],[-5,0],[0,-5]]
for a in range(0,4):
    for x in range(0,30):
        canvas.move(1,aa[a][0],aa[a][1])
        tk.update()
        time.sleep(0.1)
tk.mainloop()

