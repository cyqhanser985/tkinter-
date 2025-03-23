from tkinter import *
from tkinter import messagebox

class LoginDialog(Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("登录界面")
        self.geometry("200x100")
        self.label1 = Label(self,text="用户名")
        self.label1.grid(row=0,column=0)
        self.label2 = Label(self,text="密码")
        self.label2.grid(row=1,column=0)
        self.entry1 = Entry(self)
        self.entry1.grid(row=0,column=1,sticky="ew",padx=10)
        self.entry2 = Entry(self)
        self.entry2.grid(row=1,column=1,sticky="ew",padx=10)
        self.button1 = Button(self,text="登录",command=self.login)
        self.button1.grid(row=2,column=0,columnspan=2)

        self.columnconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)

        self.transient(master)
        self.grab_set()
        master.wait_window(self)


    def login(self):
        if self.entry1.get() != "admin":
            ms1 = messagebox.showerror("错误","该用户没有注册！")
            self.entry1.delete(0,END)
            ms1.transient(self)
            ms1.grab_set()
            self.wait_window(ms1)
        elif self.entry2.get() != "123456":
            ms2 = messagebox.showerror("错误","密码错误！")
            self.entry2.delete(0,END)
            ms2.transient(self)
            ms2.grab_set()
            self.wait_window(ms2)
        else:
            messagebox.showinfo("成功","登录成功！")
            self.destroy()

root = Tk()
dialog = LoginDialog(root)
root.mainloop()