import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import numpy as np

temp = np.random.rand(6, 6)
df = pd.DataFrame(temp)
df.columns = ['A', 'B', 'CCC', 'DDDD', 'EEEE', 'FDSSSSDSDSD']

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("学分制系统")

        # 设置窗口大小
        self.window_width = 800
        self.window_height = 600

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

        self.identities = {'admin': 0}

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
        for I in range(len(df)):
            if str(df.iloc[I, 0]) == username and str(df.iloc[I, 1]) == password:
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
        ttk.Button(self.root, text='课程管理', style='TButton', command=self.setup_course_management_ui).pack(pady=10)
        ttk.Button(self.root, text='学生管理', style='TButton', command=self.setup_student_management_ui).pack(pady=10)
        ttk.Button(self.root, text='教师管理', style='TButton', command=self.setup_teacher_management_ui).pack(pady=10)
        ttk.Button(self.root, text='考试安排', style='TButton', command=self.setup_exam_management_ui).pack(pady=10)
        ttk.Button(self.root, text='学生成绩管理', style='TButton', command=self.setup_grade_management_ui).pack(pady=10)
        ttk.Button(self.root, text='注销', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    def setup_student_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生界面", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='选课', style='TButton', command=self.setup_course_selection_ui).pack(pady=10)
        ttk.Button(self.root, text='课程查询', style='TButton', command=self.setup_course_query_ui).pack(pady=10)
        ttk.Button(self.root, text='考试查询', style='TButton', command=self.setup_exam_query_ui).pack(pady=10)
        ttk.Button(self.root, text='培养方案', style='TButton', command=self.setup_training_program_ui).pack(pady=10)
        ttk.Button(self.root, text='注销', style='TButton', command=self.setup_select_login_ui).pack(pady=10)

    def setup_course_management_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="课程管理", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='课程列表', style='TButton', command=self.course_list_ui).pack(pady=10)
        ttk.Button(self.root, text='添加课程', style='TButton', command=self.add_course_ui).pack(pady=10)
        ttk.Button(self.root, text='删除课程', style='TButton', command=self.delete_course_ui).pack(pady=10)
        ttk.Button(self.root, text='修改课程', style='TButton', command=self.modify_course_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_admin_ui).pack(pady=10)

    def setup_student_management_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生管理", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='学生列表', style='TButton', command=self.student_list_ui).pack(pady=10)
        ttk.Button(self.root, text='添加学生', style='TButton', command=self.add_student_ui).pack(pady=10)
        ttk.Button(self.root, text='删除学生', style='TButton', command=self.delete_student_ui).pack(pady=10)
        ttk.Button(self.root, text='修改学生', style='TButton', command=self.modify_student_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_admin_ui).pack(pady=10)

    def setup_teacher_management_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="教师管理", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='教师列表', style='TButton', command=self.teacher_list_ui).pack(pady=10)
        ttk.Button(self.root, text='添加教师', style='TButton', command=self.add_teacher_ui).pack(pady=10)
        ttk.Button(self.root, text='删除教师', style='TButton', command=self.delete_teacher_ui).pack(pady=10)
        ttk.Button(self.root, text='修改教师', style='TButton', command=self.modify_teacher_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_admin_ui).pack(pady=10)

    def setup_exam_management_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="考试安排", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='考试列表', style='TButton', command=self.exam_list_ui).pack(pady=10)
        ttk.Button(self.root, text='添加考试', style='TButton', command=self.add_exam_ui).pack(pady=10)
        ttk.Button(self.root, text='删除考试', style='TButton', command=self.delete_exam_ui).pack(pady=10)
        ttk.Button(self.root, text='修改考试', style='TButton', command=self.modify_exam_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_admin_ui).pack(pady=10)

    def setup_grade_management_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生成绩管理", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='学生成绩', style='TButton', command=self.student_grade_ui).pack(pady=10)
        ttk.Button(self.root, text='修改成绩', style='TButton', command=self.modify_grade_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_admin_ui).pack(pady=10)

    def setup_course_selection_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="选课", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='全部课程列表', style='TButton', command=self.course_list_ui).pack(pady=10)
        ttk.Button(self.root, text='已选课程查询', style='TButton', command=self.selected_courses_ui).pack(pady=10)
        ttk.Button(self.root, text='个人课程表', style='TButton', command=self.schedule_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_ui).pack(pady=10)

    def setup_course_query_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="课程查询", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='已选课程查询', style='TButton', command=self.selected_courses_ui).pack(pady=10)
        ttk.Button(self.root, text='个人课程表', style='TButton', command=self.schedule_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_ui).pack(pady=10)

    def setup_exam_query_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="考试查询", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='考试时间查询', style='TButton', command=self.exam_time_ui).pack(pady=10)
        ttk.Button(self.root, text='考试成绩查询', style='TButton', command=self.exam_grade_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_ui).pack(pady=10)

    def setup_training_program_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="培养方案", font=('Arial', 21)).pack(pady=20)
        ttk.Button(self.root, text='培养方案查询', style='TButton', command=self.training_program_ui).pack(pady=10)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_ui).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def goback_main_gui(self):
        self.setup_select_login_ui()

    def display_df(self, df):
        tree = ttk.Treeview(root)
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        # 获取屏幕宽度和列数
        window_width, window_height = self.root.winfo_width(), self.root.winfo_height()
        pady, padx = 20, 20
        num_columns = len(df.columns)
        column_width = (window_width-4*padx) // num_columns

        for column in df.columns:
            tree.heading(column, text=column)
            tree.column(column, width=column_width)

        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))

        # 将表格放置在窗口中心
        tree.pack(pady=pady, padx=padx)

        # 计算窗口居中位置
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def add_df(self, df):
        for col in df.columns:
            frame = tk.Frame(self.root)
            frame.pack()
            tk.Label(frame, text=col+":", font=('Arial', 18)).pack(side='left', pady=5)
            new_item_entry = ttk.Entry(frame, font=('Arial', 18))
            new_item_entry.pack(side='left', pady=5)
        # command 待实现
        # ttk.Button(self.root, text='添加', style='TButton', command='').pack(pady=20)

    def del_df(self):
        return

    def course_list_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="课程列表", font=('Arial', 21)).pack(pady=20)
        self.display_df(df)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_management_ui).pack(pady=10)

    def add_course_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="添加课程", font=('Arial', 21)).pack(pady=20)
        # self.add_df(df)
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_management_ui).pack(pady=10)

    def delete_course_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="删除课程", font=('Arial', 21)).pack(pady=20)
        # 在这里添加删除课程的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_management_ui).pack(pady=10)

    def modify_course_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="修改课程", font=('Arial', 21)).pack(pady=20)
        # 在这里添加修改课程的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_management_ui).pack(pady=10)

    def student_list_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生列表", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示学生列表的代码

        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_management_ui).pack(pady=10)

    def add_student_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="添加学生", font=('Arial', 21)).pack(pady=20)
        # 在这里添加添加学生的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_management_ui).pack(pady=10)

    def delete_student_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="删除学生", font=('Arial', 21)).pack(pady=20)
        # 在这里添加删除学生的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_management_ui).pack(pady=10)

    def modify_student_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="修改学生", font=('Arial', 21)).pack(pady=20)
        # 在这里添加修改学生的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_student_management_ui).pack(pady=10)

    def teacher_list_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="教师列表", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示教师列表的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_teacher_management_ui).pack(pady=10)

    def add_teacher_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="添加教师", font=('Arial', 21)).pack(pady=20)
        # 在这里添加添加教师的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_teacher_management_ui).pack(pady=10)

    def delete_teacher_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="删除教师", font=('Arial', 21)).pack(pady=20)
        # 在这里添加删除教师的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_teacher_management_ui).pack(pady=10)

    def modify_teacher_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="修改教师", font=('Arial', 21)).pack(pady=20)
        # 在这里添加修改教师的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_teacher_management_ui).pack(pady=10)

    def exam_list_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="考试列表", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示考试列表的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_management_ui).pack(pady=10)

    def add_exam_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="添加考试", font=('Arial', 21)).pack(pady=20)
        # 在这里添加添加考试的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_management_ui).pack(pady=10)

    def delete_exam_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="删除考试", font=('Arial', 21)).pack(pady=20)
        # 在这里添加删除考试的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_management_ui).pack(pady=10)

    def modify_exam_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="修改考试", font=('Arial', 21)).pack(pady=20)
        # 在这里添加修改考试的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_management_ui).pack(pady=10)

    def student_grade_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="学生成绩",font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示学生成绩的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_grade_management_ui).pack(pady=10)

    def modify_grade_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="修改成绩", font=('Arial', 21)).pack(pady=20)
        # 在这里添加修改成绩的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_grade_management_ui).pack(pady=10)

    def selected_courses_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="已选课程查询", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示已选课程的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_query_ui).pack(pady=10)

    def schedule_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="个人课程表", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示个人课程表的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_course_query_ui).pack(pady=10)

    def exam_time_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="考试时间查询", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示考试时间的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_query_ui).pack(pady=10)

    def exam_grade_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="考试成绩查询", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示考试成绩的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_exam_query_ui).pack(pady=10)

    def training_program_ui(self):
        self.clear_frame()
        tk.Label(self.root, text="培养方案查询", font=('Arial', 21)).pack(pady=20)
        # 在这里添加显示培养方案的代码
        ttk.Button(self.root, text='返回', style='TButton', command=self.setup_training_program_ui).pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
