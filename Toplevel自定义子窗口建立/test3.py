import tkinter as tk

# 确认对话框类，继承自Toplevel窗口
class ConfirmDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("天狗调研")  # 设置对话框标题
        
        # 创建提示标签并布局
        self.label = tk.Label(self, text="请问你喜欢萝卜吗？")
        self.label.grid(row=0, column=0, columnspan=2, pady=(30, 30))
        
        # 创建"是"按钮并绑定确认事件
        self.yes_button = tk.Button(self, text="是", command=self.confirm_yes)
        self.yes_button.grid(row=1, column=0, padx=20, pady=(0, 30))
        
        # 创建"否"按钮并绑定取消事件
        self.no_button = tk.Button(self, text="否", command=self.confirm_no)
        self.no_button.grid(row=1, column=1, padx=20, pady=(0, 30))

        # 设置对话框为模态窗口
        self.transient(master)  # 关联主窗口
        self.grab_set()         # 独占输入焦点
        master.wait_window(self)  # 等待对话框关闭

    # 确认按钮回调函数
    def confirm_yes(self):
        print("柯乐确认喜欢萝卜")  # 输出确认信息
        self.destroy()          # 销毁对话框
    
    # 取消按钮回调函数
    def confirm_no(self):
        print("柯乐不喜欢萝卜")  # 输出取消信息
        self.destroy()          # 销毁对话框

# 主程序入口
root = tk.Tk()
dialog = ConfirmDialog(root)  # 创建对话框实例
root.mainloop()               # 启动主事件循环