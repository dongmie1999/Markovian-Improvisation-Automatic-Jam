# -*- coding: utf-8 -*-
import tkinter as tk
import goodsubmit

root = tk.Tk()  # tkinter.Tk() 这是“根”容器 即创建了一个什么都没有的窗口
root.title('商品录入界面-main')  # 设置窗口名称
goodsubmit.goodsubmitc(root)  # 实例化LoginPage中的对象，将这个窗口作为其他页面的父容器，通过参数root传递
root.mainloop()  # 要让这个“根”窗口一直显示
