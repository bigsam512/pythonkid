from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=400)
canvas.pack()
my_image = PhotoImage(file='~/Pictures/small.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)

tk.mainloop()
