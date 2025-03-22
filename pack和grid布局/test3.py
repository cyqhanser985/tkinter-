import tkinter as tk  # 导入tkinter模块

# 创建主窗口
root = tk.Tk()

# 左侧通讯录
# 创建浅灰色背景的Frame容器
left_frame = tk.Frame(root, bg="lightgray")
# 左侧布局：靠左对齐，填充整个剩余空间
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 使用grid布局创建联系人列表
for i in range(5):
    # 创建联系人标签（居左对齐）
    tk.Label(left_frame, text=f"联系人{i+1}").grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
    # 创建详情按钮（右侧对齐）
    tk.Button(left_frame, text="详情").grid(row=i, column=1, padx=5, pady=5)

# 右侧按钮组(pack布局)
# 创建浅蓝色背景的Frame容器
right_frame = tk.Frame(root, bg="lightblue")
# 右侧布局：靠右对齐，垂直填满
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# 使用pack布局创建垂直按钮组
tk.Button(right_frame, text="添加").pack(fill=tk.X, pady=2)  # 添加按钮（水平填充）
tk.Button(right_frame, text="删除").pack(fill=tk.X, pady=2)  # 删除按钮
tk.Button(right_frame, text="刷新").pack(fill=tk.X, pady=2)  # 刷新按钮

# 启动主循环
root.mainloop()