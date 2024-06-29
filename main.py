import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("学分制系统")

        # 设置窗口大小
        self.window_width = 600
        self.window_height = 800

        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 计算 x 和 y 坐标
        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)

        self.root.geometry(f'{self.window_width}x{self.window_height}+{int(x)}+{int(y)}')

        # 创建 Style 对象并配置 TButton 样式
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=10)

        self.current_identity = None
        self.setup_select_login_ui()
        self.style.configure('TButton', font=('Arial', 18), padding=16)

        # 初始化用户数据文件
        self.user_data_file = 'user_data.csv'
        if not os.path.exists(self.user_data_file):
            self.init_user_data()

        self.identities = {'123456': 0}

    def init_user_data(self):
        df = pd.DataFrame(columns=['username', 'password'])
        df.to_csv(self.user_data_file, index=False)

    def setup_select_login_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="请登录您的用户:", font=('Arial', 21)).pack()
        ttk.Button(self.root, text='登陆', style='TButton', command=self.setup_login_ui).pack(pady=6)
        ttk.Button(self.root, text='注册', style='TButton', command=self.setup_register_ui).pack(pady=6)



    # 登陆界面
    def setup_login_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="登录", font=('Arial', 21)).pack(pady=20)
        tk.Label(self.root, text="用户名:", font=('Arial', 18)).pack(pady=5)
        self.username_entry = ttk.Entry(self.root, font=('Arial', 18))
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="密码:", font=('Arial', 18)).pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show='*', font=('Arial', 18))
        self.password_entry.pack(pady=5)
        ttk.Button(self.root, text='登录', style='TButton', command=self.login).pack(pady=20)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    # 注册界面
    def setup_register_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="注册", font=('Arial', 21)).pack(pady=20)
        tk.Label(self.root, text="用户名:", font=('Arial', 18)).pack(pady=5)
        self.new_username_entry = ttk.Entry(self.root, font=('Arial', 18))
        self.new_username_entry.pack(pady=5)
        tk.Label(self.root, text="密码:", font=('Arial', 18)).pack(pady=5)
        self.new_password_entry = ttk.Entry(self.root, show='*', font=('Arial', 18))
        self.new_password_entry.pack(pady=5)
        ttk.Button(self.root, text='注册', style='TButton', command=self.register).pack(pady=20)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    # 登陆界面实现逻辑
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        df = pd.read_csv(self.user_data_file)
        for i in range(len(df)):
            if str(df.iloc[i, 0]) == username and str(df.iloc[i, 1]) == password:
                messagebox.showinfo("登录成功", "欢迎，" + username)
                self.select_identity(username)
                return
        messagebox.showerror("登录失败", "用户名或密码错误")

    # 注册界面实现逻辑
    def register(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        df = pd.read_csv(self.user_data_file)

        if username in df['username'].values:
            messagebox.showerror("注册失败", "用户名已存在")
        else:
            new_user = pd.DataFrame([[username, password]], columns=['username', 'password'])
            new_user.to_csv(self.user_data_file, mode='a', header=False, index=False)
            messagebox.showinfo("注册成功", "注册成功，请登录")
            self.setup_login_ui()

    def select_identity(self, username):
        if username in self.identities:
            self.setup_admin_ui()
        else:
            self.setup_student_ui()

    def setup_admin_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="管理员界面", font=('Arial', 21)).pack(pady=20)

        ttk.Button(self.root, text='注销', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    def setup_student_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生界面", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='选课', style='TButton', command=self.setup_login_ui).pack(pady=10)
        ttk.Button(self.root, text='课程查询', style='TButton', command=self.setup_login_ui).pack(pady=10)
        ttk.Button(self.root, text='考试查询', style='TButton', command=self.setup_login_ui).pack(pady=10)
        ttk.Button(self.root, text='培养方案', style='TButton', command=self.setup_login_ui).pack(pady=10)
        ttk.Button(self.root, text='注销', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def goback_main_gui(self):
        self.setup_select_login_ui()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()