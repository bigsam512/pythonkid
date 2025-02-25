from tkinter import *

def movetriangle1(envent):
    canvas.move(1,5,0)

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)

tk = Tk()
canvas=Canvas(tk, width=400, height=400, bg='blue')
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)

# canvas.bind_all('<KeyPress-Return>', movetriangle)
tk.mainloop()
