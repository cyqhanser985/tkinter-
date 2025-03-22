# 导入Tkinter模块（GUI开发库）
import tkinter as tk

# 创建主窗口对象
root = tk.Tk()

# 显示屏（输入框）
display = tk.Entry(root, font=("Arial", 16))  # 设置字体和字号
display.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)  # 跨4列，填充整个单元格

# 按钮布局（二维数组形式的按钮文字）
buttons = [
    "7", "8", "9", "/",    # 第一行运算符
    "4", "5", "6", "*",    # 第二行运算符
    "1", "2", "3", "-",    # 第三行运算符
    "0", ".", "=", "+"     # 第四行运算符
]

# 配置行列权重（使窗口缩放时按钮均匀缩放）
for i in range(4):
    root.grid_columnconfigure(i, weight=1)  # 每列权重为1
    root.grid_rowconfigure(i, weight=1)     # 每行权重为1

# 创建并布局按钮
for i, btn_text in enumerate(buttons):
    row = i // 4 + 1  # 计算行号（每行4个按钮）
    col = i % 4       # 计算列号
    # 创建按钮实例
    btn = tk.Button(root, text=btn_text, font=("Arial", 14))
    # 布局按钮并填充单元格
    btn.grid(row=row, column=col, sticky=tk.NSEW)

# 启动主事件循环（保持窗口显示）
root.mainloop()