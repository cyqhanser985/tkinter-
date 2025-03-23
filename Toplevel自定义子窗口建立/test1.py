import tkinter as tk

class AboutDialog(tk.Toplevel):
    """自定义关于对话框的顶层窗口类"""
    def __init__(self,master):
        """初始化对话框
        Args:
            master: 父窗口实例
        """
        super().__init__(master) # 初始化父类
        self.title("关于")       # 设置对话框标题
        # 添加标签和按钮
        tk.Label(self,text="这是一个关于对话框").pack()  # 信息展示标签
        tk.Button(self,text="关闭",command=self.destroy).pack()  # 绑定销毁方法的按钮

root = tk.Tk()
dialog = AboutDialog(root)
root.mainloop()
