import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=700, height=500, bg='lightyellow')
canvas.pack()

# 创建多边形并获取 ID
poly1 = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='blue')
poly2 = canvas.create_polygon(20, 10, 20, 60, 60, 35, fill='red')

# 移动两个多边形
for x in range(60):
    canvas.move(poly1, 5, 6)
    canvas.move(poly2, 5, 4)  # 反方向移动
    tk.update()
    time.sleep(0.024)

tk.mainloop()

