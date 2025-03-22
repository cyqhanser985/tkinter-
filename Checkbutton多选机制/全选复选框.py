from tkinter import *

class CheckbuttonGroup:
    """复选框组管理类，实现全选/反选功能"""
    def __init__(self, root):
        self.root = root
        self.all_var = BooleanVar()  # 控制全选状态的变量
        self.check_var = []          # 存储子复选框状态变量的列表

        # 主控复选框（全选/反选）
        Checkbutton(root, text="全选", variable=self.all_var, 
                  command=self.toggle_all).pack(side=BOTTOM)

        # 创建4个子复选框
        for i in range(1,5):
            var = BooleanVar()
            Checkbutton(root, text=f"选项{i}", variable=var,
                      command=self.check_all).pack()  # 绑定状态检查回调
            self.check_var.append(var)  # 将变量对象存入列表

    def toggle_all(self):
        """全选/反选所有子复选框"""
        state = self.all_var.get()
        for var in self.check_var:  # 遍历所有子复选框变量
            var.set(state)          # 同步设置选中状态

    def check_all(self):
        """检查子复选框的选中状态，自动更新全选复选框"""
        # 使用all()判断所有子项是否都被选中
        if all(var.get() for var in self.check_var):
            self.all_var.set(True)   # 全选状态置为True
        else:
            self.all_var.set(False)  # 任意未选中则取消全选状态

# 创建主窗口
root = Tk()
CheckbuttonGroup(root)  # 实例化复选框组
root.mainloop()