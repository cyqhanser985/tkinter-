from tkinter import *
from tkinter import messagebox

# 自定义输入对话框类，继承自Toplevel
class InputDialog(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("输入姓名")  # 设置窗口标题
        
        # 创建输入框组件
        self.entry = Entry(self)
        self.entry.pack()  # 将输入框布局到窗口
        
        # 创建确认按钮组件
        self.btn = Button(self, text="确定", command=self.get_input)
        self.btn.pack()  # 将按钮布局到窗口
        self.btn.focus_set()  # 设置焦点在按钮上
        
        # 绑定回车键事件到按钮
        self.btn.bind("<Return>", lambda e: self.get_input())

    # 获取输入内容的回调函数
    def get_input(self):
        if self.entry.get():
            print(self.entry.get())  # 在控制台输出输入内容
            self.destroy()  # 关闭对话框
        else:
            messagebox.showwarning("警告", "输入不能为空！")  # 显示警告弹窗

# 创建主窗口
root = Tk()
# 实例化自定义对话框
dialog = InputDialog(root)
# 启动主事件循环
root.mainloop()