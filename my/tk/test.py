import tkinter as tk
from tkinter import ttk


def keygo(*args):  # 处理事件，*args表示可变参数
    print(keyChosen.get())  # 打印选中的值


def modego(*args):  # 处理事件，*args表示可变参数
    print(modeChosen.get())  # 打印选中的值


def do_job():
    print("OK")


win = tk.Tk()
win.title("Python GUI")  # 添加标题
# win.geometry('%dx%d' % (500, 300))  # 设置窗口大小
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
ww = 500
wh = 300
x = (sw - ww) / 2
y = (sh - wh) / 2
win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

tk.Label(win, text='Key: ').grid(column=2, row=2, stick=tk.W, pady=10)
key = tk.StringVar()
keyChosen = ttk.Combobox(win, width=12, textvariable=key)
keyChosen['values'] = ('C', 'D', 'E', 'F', 'G', 'A', 'B')  # 设置下拉列表的值
keyChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
keyChosen.bind("<<ComboboxSelected>>", keygo)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
keyChosen.grid(column=3, row=2)

tk.Label(win, text='Mode: ').grid(column=2, row=3, stick=tk.W, pady=10)
mode = tk.StringVar()
modeChosen = ttk.Combobox(win, width=12, textvariable=mode)
modeChosen['values'] = ('major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'minor',
                        'locrian', 'major pentatonic', 'minor pentatonic')  # 设置下拉列表的值
modeChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
modeChosen.bind("<<ComboboxSelected>>", modego)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
modeChosen.grid(column=3, row=3)

# 文本框
tk.Label(win, text='time signature: ').grid(column=2, row=4, stick=tk.W, pady=10)
bpm = tk.StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
bpmEntered = ttk.Entry(win, width=12, textvariable=bpm)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
bpmEntered.grid(column=3, row=4)  # 设置其在界面中出现的位置  column代表列   row 代表行
bpmEntered.focus()  # 当程序运行时,光标默认会出现在该文本框中

menubar = tk.Menu(win)

# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)

# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加一条分隔线
filemenu.add_command(label='Exit', command=win.quit)  # 用tkinter里面自带的quit()函数

# 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit', menu=editmenu)

# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

# 第8步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import
submenu.add_command(label='Submenu_1', command=do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1


win.config(menu=menubar)

win.mainloop()  # 当调用mainloop()时,窗口才会显示出来

# ttk.Label(win, text="Chooes a number").grid(column=1, row=0)  # 添加一个标签，并将其列设置为1，行设置为0
# ttk.Label(win, text="Enter a name:").grid(column=0, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行


# # button被点击之后会被执行
# def clickMe():  # 当action被点击时,该函数则生效
#     action.configure(text='Hello ' + name.get())  # 设置button显示的内容
#     action.configure(state='disabled')  # 将按钮设置为灰色状态，不可使用状态
#
#
# # 按钮
# action = ttk.Button(win, text="Click Me!", command=clickMe)  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
# action.grid(column=2, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行

# # 文本框
# name = tk.StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
# nameEntered = ttk.Entry(win, width=12, textvariable=name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
# nameEntered.grid(column=0, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
# nameEntered.focus()  # 当程序运行时,光标默认会出现在该文本框中
