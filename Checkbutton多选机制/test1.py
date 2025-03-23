# 导入Tkinter GUI库
from tkinter import *
from tkinter import messagebox

# 定义选项显示函数
def show_selection():
    selected = []
    if var1.get(): selected.append("Python")
    if var2.get(): selected.append("Java")
    if var3.get(): selected.append("C++")
    # 弹出消息框显示选择结果
    messagebox.showinfo("选择结果", f"您选择的编程语言是：{', '.join(selected)}")

# 创建主窗口
root = Tk()
# 定义三个布尔变量用于存储复选框状态
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()

# 创建三个复选框组件
Checkbutton(root, text="Python", variable=var1).pack()
Checkbutton(root, text="Java", variable=var2).pack()
Checkbutton(root, text="C++", variable=var3).pack()

# 创建提交按钮，绑定点击事件
Button(root, text="提交", command=show_selection).pack()

# 启动主事件循环
root.mainloop()
