import tkinter as tk

# 创建主窗口
root = tk.Tk()
# 配置第2列的宽度自适应（权重为1）
root.grid_columnconfigure(1, weight=1)

# 用户名区域
# 标签左对齐West，输入框水平拉伸（EW）
tk.Label(root, text="用户名").grid(row=0, column=0, sticky=tk.W)
tk.Entry(root).grid(row=0, column=1, sticky=tk.EW)

# 密码区域
# 密码输入显示*号，布局同用户名
tk.Label(root, text="密码").grid(row=1, column=0, sticky=tk.W)
tk.Entry(root, show="*").grid(row=1, column=1, sticky=tk.EW)

# 记住我复选框
# 跨两列，右对齐East
chk = tk.Checkbutton(root, text="记住我")
chk.grid(row=2, column=0, columnspan=2, sticky=tk.E)

# 登录按钮
# 跨两列水平拉伸，添加底部间距（pady）
btn = tk.Button(root, text="登录")
btn.grid(row=3, column=0, columnspan=2, sticky=tk.EW, pady=10)

# 启动主事件循环
root.mainloop()