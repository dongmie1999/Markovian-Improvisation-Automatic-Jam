import tkinter as tk
from tkinter.messagebox import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
# import tkmysql


class goodsubmitc(object):  # 注：这里的LoginPage类继承了object类，是一种新式类（其实在python3中你写不写它都默认继承object类）
    def __init__(self, master=None):  # 传入master的参数为root
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (500, 300))  # 设置窗口大小
        self.good = tk.StringVar()
        self.supplier = None
        self.StockID = tk.StringVar()
        self.createPage()  # 在LoginPage中调用CreatePage函数，以创建一个页面

    def createPage(self):
        self.page = tk.Frame(self.root) # 创建Frame
        self.page.pack()  # 放置Frame
        tk.Label(self.page).grid(row=0, stick=tk.W)
        # 这里的控件（标签Lable、输入框Entry按钮Button）全都放在self.page即Frame下，而不是master=root下
        tk.Label(self.page, text='Key: ').grid(row=0, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.good).grid(row=0, column=1, stick=tk.E)
        tk.Label(self.page, text='Mode: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.StockID).grid(row=1, column=1, stick=tk.E)
        tk.Button(self.page, text='录入', command=self.sqlsubmimt).grid(row=3,column=1,pady=10)
        # # 创建一个下拉列表
        # number = tk.StringVar()
        # numberChosen = ttk.Combobox(self.root, width=12, textvariable=number)
        # numberChosen['values'] = (1, 2, 4, 42, 100)  # 设置下拉列表的值
        # numberChosen.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        # numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        '''
        button0=tk.Button(self.page,text='供应商编号1',command=self.f1)
        button0.grid(row=5, column=0)
        button1=tk.Button(self.page,text='供应商编号2',command=self.f2)
        button1.grid(row=5, column=1)
        button2=tk.Button(self.page,text='供应商编号3',command=self.f3)
        button2.grid(row=5, column=2)
        '''
        # PID=tkmysql.select()
        self.cmb=ttk.Combobox(self.root)
        self.cmb.pack()
        print("cmb pack")
        # a=[]
        # for i in range(len(PID)):
        #     a.append(str(PID[i]))
        # a=tuple(a)
        # self.cmb['value']=a
        # self.cmb["state"]="readonly"
        # #self.cmb.current(2)
        # self.cmb.bind("<<ComboboxSelected>>",self.cb)
        
        #self.text=tk.Text(self.root)
        #self.text.pack()

    def cb(self, event):
        #self.text.insert('insert',self.cmb.get()+"\n")
        self.supplier = self.cmb.get()
            
    def sqlsubmimt(self):
        #print("type of self.good:",type(self.good))
        #if(type(self.good == <class 'tkinter.StringVar'>)):
        #    print(self.good)
        #else:
        #if(type(self.good == str or self.good == tk.StringVar)):
        #    print(self.good)
        #else:
        #    print(self.good.get())
        #self.page.destroy()
        if(not self.StockID.get()):
            showinfo(title='提示', message='请输入进货编码')
            return
        if(not self.good.get()):
            showinfo(title='提示', message='请输入商品编号')
            return
        print("StockID:",self.StockID.get(),"type:",type(self.StockID))
        print("ProductID:",self.good.get(),"type:",type(self.good.get()))
        print("ProviderID:",self.supplier,"type:",type(self.supplier))
        # tkmysql.submit(self.StockID.get(),self.good.get(),self.supplier)
        showinfo(title='录入成功', message='录入成功')
    
    def f1(self):
        self.supplier=1
        showinfo(title='确认', message='供应商编号：1')
        
    def f2(self):
        self.supplier=2
        showinfo(title='确认', message='供应商编号：2')
        
    def f3(self):
        self.supplier=3
        showinfo(title='确认', message='供应商编号：3')