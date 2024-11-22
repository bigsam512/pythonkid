import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("矩形和椭圆")

# 创建一个画布
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# 绘制200x100的矩形
rect_x1, rect_y1 = 50, 50
rect_x2, rect_y2 = 250, 150
canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="blue")

# 在矩形内绘制最大椭圆
canvas.create_oval(rect_x1, rect_y1, rect_x2, rect_y2, outline="red")

# 运行主循环
root.mainloop()

