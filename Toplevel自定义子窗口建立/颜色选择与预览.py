import tkinter as tk

class ColorPicker(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("颜色选择")
        self.color = (0,0,0)

        # 红绿蓝滑块
        self.red = tk.Scale(self,from_=0,to=255,orient=tk.HORIZONTAL,
                            label="红",command=self.update_preview)
        self.red.pack()
        self.green=tk.Scale(self,from_=0,to=255,orient=tk.HORIZONTAL,
                            label="绿",command=self.update_preview)
        self.green.pack()
        self.blue=tk.Scale(self,from_=0,to=255,orient=tk.HORIZONTAL,
                            label="蓝",command=self.update_preview)
        self.blue.pack()

        # 颜色预览
        self.preview = tk.Label(self,width=20,height=5)
        self.preview.pack(pady=10)

        # 确定按钮
        tk.Button(self,text="确定",command=self.on_confirm).pack()

    def update_preview(self, _):
        r = self.red.get()
        g = self.green.get()
        b = self.blue.get()
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        self.preview.config(bg=color_hex)
        self.color = (r,g,b)
    
    def on_confirm(self):
        self.master.config(bg=f"#{self.color[0]:02x}{self.color[1]:02x}{self.color[2]:02x}")
        self.destroy()

root = tk.Tk()
root.geometry("300x200")
tk.Button(root,text="选择颜色",command=lambda: ColorPicker(root)).pack()
root.mainloop()
