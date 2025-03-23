# 导入Tkinter模块（Python标准GUI库）
from tkinter import *

# 定义复选框状态切换函数
def toggle_subscribe():
    if agree_var.get():  # 当协议同意复选框被选中时
        subscribe_cb.config(state=NORMAL)  # 启用订阅复选框
    else:  # 当协议同意复选框取消选中时
        subscribe_cb.config(state=DISABLED)  # 禁用订阅复选框
        subscribe_var.set(False)  # 重置订阅复选框的值

# 创建主窗口
root = Tk()

# 创建控制变量
agree_var = BooleanVar(value=False) # 默认选中协议（控制协议同意复选框）
subscribe_var = BooleanVar()        # 控制订阅复选框

# 创建协议同意复选框（带状态切换命令绑定）
Checkbutton(root, text="同意协议", variable=agree_var, command=toggle_subscribe).pack()
# 创建订阅邮件复选框（初始状态为禁用）
subscribe_cb = Checkbutton(root, text="订阅邮件", variable=subscribe_var, state=DISABLED)
subscribe_cb.pack()

# 启动主事件循环
root.mainloop()
