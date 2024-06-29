import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


def get_word():
    df = pd.read_excel('./外研社一起点英语单一.xlsx')

    def convert_to_units_format(df):
        units = {}
        for _, row in df.iterrows():
            dic = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6}
            dic2 = {'上册': 1, '下册': 2}
            grade = f"Grade {dic[row['年级'][0]]} Semester {dic2[row['分册']]}"
            if row['单元'][-1] == '0':
                unit = f"Unit {10}"
            else:
                unit = f"Unit {row['单元'][-1]}"
            chinese = row['中文']
            english = row['英文']

            if grade not in units:
                units[grade] = {}
            if unit not in units[grade]:
                units[grade][unit] = {}
            units[grade][unit][english] = chinese

        return units

    units_format = convert_to_units_format(df)
    return units_format


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

        self.units = get_word()

        self.current_grade = None
        self.current_unit = None
        self.words = None
        self.word_iter = None
        self.current_word = None
        self.correct_answers = 0
        self.total_questions = 0

        self.setup_select_grade_ui()
        # 创建 Style 对象并配置 TButton 样式
        self.style.configure('TButton', font=('Arial', 16), padding=10)  # 字体大小调整为14

    def setup_select_grade_ui(self):
        self.clear_frame()

        tk.Label(self.root, text="Select a grade:", font=('Arial', 21)).pack()

        for grade in self.units:
            ttk.Button(self.root, text=grade, style='TButton',
                       command=lambda grade=grade: self.select_grade(grade)).pack(pady=5)

    def select_grade(self, grade):
        self.current_grade = grade
        self.setup_select_unit_ui()

    def setup_select_unit_ui(self):
        self.clear_frame()

        # 创建一个Frame作为所有元素的容器
        unit_frame = tk.Frame(self.root)
        unit_frame.pack(expand=True, fill=tk.BOTH)

        # 创建一个内部Frame用于垂直居中所有元素
        center_frame = tk.Frame(unit_frame)
        center_frame.pack(expand=True)

        # 使用pack的side和anchor参数来垂直居中Frame内的元素
        tk.Label(center_frame, text=f"Select a unit in {self.current_grade}:", font=('Arial', 21)).pack(side='top',
                                                                                                        pady=10)

        for unit in self.units[self.current_grade]:
            ttk.Button(center_frame, text=unit, style='TButton', command=lambda unit=unit: self.select_unit(unit)).pack(
                side='top', pady=5)

        # 添加返回上一页的按钮
        ttk.Button(center_frame, text="Back to Grades", style='TButton', command=self.go_back_to_grade_selection).pack(
            side='top', pady=20)

    def select_unit(self, unit):
        self.current_unit = unit
        self.words = self.units[self.current_grade][self.current_unit]
        self.word_iter = iter(self.words.items())
        self.correct_answers = 0  # 重置正确答案的数量
        self.total_questions = len(self.words)  # 更新总问题数量
        self.next_word()

    def next_word(self):
        try:
            self.current_word, meaning = next(self.word_iter)
            self.setup_quiz_ui(meaning)
        except StopIteration:
            self.show_results()

    def setup_quiz_ui(self, meaning):
        self.clear_frame()

        # 创建一个Frame作为所有元素的容器
        quiz_frame = tk.Frame(self.root)
        # 扩展Frame以填充整个root窗口，同时设置expand和fill使其内容居中
        quiz_frame.pack(expand=True, fill=tk.BOTH)

        # 创建一个内部Frame用于垂直居中所有元素
        center_frame = tk.Frame(quiz_frame)
        center_frame.pack(expand=True)

        # 使用pack的side和anchor参数来垂直居中Frame内的元素
        tk.Label(center_frame, text=f"What is the English word for '{meaning}'?", font=('Arial', 19)).pack(side='top', pady=10)
        tk.Label(center_frame, text=f"Correct Answers: {self.correct_answers}/{self.total_questions}", font=('Arial', 16)).pack(side='top', pady=10)

        answer_entry = tk.Entry(center_frame, font=('Arial', 16))
        answer_entry.pack(side='top', pady=10)

        # 提交答案的按钮
        ttk.Button(center_frame, text="Submit", style='TButton',
                   command=lambda: self.check_answer(answer_entry.get())).pack(side='top', pady=10)

        # 添加返回上一页的按钮
        ttk.Button(center_frame, text="Back", style='TButton', command=self.go_back_to_unit_selection).pack(side='top', pady=10)

        # 设置焦点到输入框
        answer_entry.focus_set()

    def check_answer(self, answer):
        if answer.lower() == self.current_word:
            messagebox.showinfo("Result", "Correct!")
            self.correct_answers += 1
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer is '{self.current_word}'.")
        self.next_word()

    def show_results(self):
        messagebox.showinfo("Quiz Finished", f"You got {self.correct_answers} out of {self.total_questions} correct.")
        self.setup_select_grade_ui()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def go_back_to_unit_selection(self):
        self.setup_select_unit_ui()

    def go_back_to_grade_selection(self):
        self.setup_select_grade_ui()


def custom_messagebox(title, message):
    # 创建新窗口
    message_window = tk.Toplevel()
    message_window.title(title)

    # 设置窗口大小和位置
    message_window.geometry("300x100")  # 可以根据需要调整大小

    # 在新窗口中添加一个Label显示消息，可以自定义字体大小
    tk.Label(message_window, text=message, font=('Arial', 14)).pack(pady=20)

    # 添加一个按钮用于关闭窗口
    ttk.Button(message_window, text="OK", command=message_window.destroy).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
