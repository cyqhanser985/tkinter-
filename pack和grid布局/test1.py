import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 左侧框架容器（垂直排列按钮）
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.Y)  # 贴左填充Y轴方向
# 添加两个红色按钮（横向填充）
tk.Button(left_frame, text="RED", bg="red").pack(fill=tk.X)  # X轴方向填满
tk.Button(left_frame, text="RED", bg="red").pack(fill=tk.X)

# 右侧框架容器（垂直排列按钮）
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)  # 贴右填充Y轴方向
# 添加两个绿色按钮（横向填充）
tk.Button(right_frame, text="Green", bg="green").pack(fill=tk.X)
tk.Button(right_frame, text="Green", bg="green").pack(fill=tk.X)

# 底部独立按钮（直接放在根窗口）
tk.Button(root, text="Blue", bg="blue").pack(side=tk.BOTTOM, fill=tk.X)  # 贴底填充X轴方向

# 启动主事件循环
root.mainloop()
