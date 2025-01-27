import tkinter as tk
from tkinter import Toplevel, Button, Label

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("500x500")

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=50)

        # COURSE DETAILS BUTTON
        def course_win():
            self.root.destroy()  # Close current window
            new_window = tk.Tk()  # Create a new main window
            course_window(new_window)

        btn2 = Button(btn_frame, text="COURSE DETAILS", command=course_win, cursor="hand2",
                      font="lucida 16 bold", bg="black", fg="gold", width=20)
        btn2.grid(row=0, column=2, padx=54, pady=25)

        # TEACHER DETAILS BUTTON
        def teacher_site():
            self.root.destroy()  # Close current window
            new_window = tk.Tk()  # Create a new main window
            teacher_win(new_window)

        btn3 = Button(btn_frame, text="TEACHER DETAILS", command=teacher_site, cursor="hand2",
                      font="lucida 16 bold", bg="black", fg="gold", width=20)
        btn3.grid(row=0, column=3, padx=54, pady=25)

        # STUDENT DETAILS BUTTON
        def student_site():
            self.root.destroy()  # Close current window
            new_window = tk.Tk()  # Create a new main window
            student_page(new_window)

        btn4 = Button(btn_frame, text="STUDENT DETAILS", command=student_site, cursor="hand2",
                      font="lucida 16 bold", bg="black", fg="gold", width=20)
        btn4.grid(row=0, column=4, padx=54, pady=25)


# New window for course details
def course_window(new_window):
    new_window.title("Course Details")
    new_window.geometry("300x200")
    Label(new_window, text="This is the Course Details page").pack(pady=50)


# New window for teacher details
def teacher_win(new_window):
    new_window.title("Teacher Details")
    new_window.geometry("300x200")
    Label(new_window, text="This is the Teacher Details page").pack(pady=50)


# New window for student details
def student_page(new_window):
    new_window.title("Student Details")
    new_window.geometry("300x200")
    Label(new_window, text="This is the Student Details page").pack(pady=50)


# Create the root window for the main app
root = tk.Tk()
app = MainApp(root)
root.mainloop()
