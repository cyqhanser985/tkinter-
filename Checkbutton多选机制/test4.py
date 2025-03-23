# 导入tkinter模块
from tkinter import *
from tkinter import messagebox

# 复选框状态改变时的回调函数
def on_check(var):
    # 统计已选中的复选框数量
    selected = sum(1 for v in choice_var if v.get())
    if selected > 3:  # 超过3个选择时
        var.set(False)  # 撤销当前选择
        messagebox.showwarning("警告","最多只能选三项！")  # 弹出警告
    update_counter()  # 更新计数器显示

# 更新选择计数器的显示
def update_counter():
    selected = sum(1 for v in choice_var if v.get())
    counter_label.config(text=f"{selected}/3 已选择")  # 更新标签文本

# 创建主窗口
root = Tk()

# 存储复选框变量的列表
choice_var=[]

# 创建5个复选框
for i in range(5):
    var = BooleanVar()  # 创建布尔变量
    choice_var.append(var)  # 添加到变量列表
    # 创建复选框并设置命令回调
    Checkbutton(root,text=f"选项{i+1}",variable=var,command=lambda v=var : on_check(v)).pack()

# 创建显示已选数量的标签
counter_label = Label(root,text="0/3 已选择")
counter_label.pack()

# 启动主循环
root.mainloop()
