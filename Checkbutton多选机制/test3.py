# 导入tkinter模块
from tkinter import *
from tkinter import messagebox

def show_choice():
    # 使用列表推导式获取选中的语言选项
    result = [lang for lang,var in zip(language,check_var) if var.get()]
    if result:
        # 显示选中的结果
        messagebox.showinfo("选择结果","选中的课程："+",".join(result))
    else:
        # 当没有选中任何选项时弹出警告
        messagebox.showwarning("选择结果","请至少选择一门课程!")

# 创建主窗口
root = Tk()

# 定义选项列表和状态变量列表
language = ["C++","Python","Java","TypeScript"]
check_var=[]  # 存储每个选项的BooleanVar变量

# 动态创建复选框组件
for i in range(len(language)):
    var = BooleanVar()  # 创建BooleanVar实例
    check_var.append(var)  # 将变量添加到列表
    # 创建复选框并布局，绑定对应变量
    Checkbutton(root,text=language[i],variable=check_var[i]).pack()

# 创建提交按钮并绑定点击事件
Button(root,text="提交",command=show_choice).pack()

# 启动主事件循环
root.mainloop()
