import tkinter as tk
from tkinter import scrolledtext

# 消息发送函数
def send_message():
    msg = entry.get()  # 获取输入框内容
    if msg:
        message_area.insert(tk.END, f"用户:{msg}\n")  # 将消息添加到聊天区域
        entry.delete(0, tk.END)  # 清空输入框

# 创建主窗口
root = tk.Tk()

# 消息显示区域（带滚动条）
message_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)  # 自动换行组件
message_area.pack(fill=tk.BOTH, expand=True)  # 填充整个可用空间

# 输入区域（底部固定）
input_frame = tk.Frame(root)  # 底部框架容器
input_frame.pack(fill=tk.X, side=tk.BOTTOM)  # 水平填充，固定在底部

# 输入框组件
entry = tk.Entry(input_frame)
entry.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)  # 网格布局，横向拉伸

# 发送按钮
send_btn = tk.Button(input_frame, text="发送", command=send_message)
send_btn.grid(row=0, column=1, padx=5, pady=5)  # 右侧固定位置

# 设置输入框随窗口扩展
input_frame.grid_columnconfigure(0, weight=1)  # 第一列自动扩展

# 启动主循环
root.mainloop()