from tkinter import *

# 初始位置
initial_position = (10, 10, 10, 60, 50, 35)

def movetriangle(event):
    # 根据按键方向移动多边形
    if event.keysym == 'Up':
        canvas.move(triangle, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(triangle, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(triangle, -3, 0)
    elif event.keysym == 'Right':
        canvas.move(triangle, 3, 0)
    elif event.keysym == 'Return':  # 回车键复位
        # 获取当前多边形的位置
        current_coords = canvas.coords(triangle)
        # 计算需要移动的偏移量
        dx = initial_position[0] - current_coords[0]
        dy = initial_position[1] - current_coords[1]
        # 移动回初始位置
        canvas.move(triangle, dx, dy)

tk = Tk()
canvas = Canvas(tk, width=400, height=400, bg='blue')
canvas.pack()

# 创建多边形并获取它的 ID
triangle = canvas.create_polygon(*initial_position, fill='yellow')

# 绑定键盘事件
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Return>', movetriangle)  # 绑定回车键

tk.mainloop()

