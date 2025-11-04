import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="student_system"
        )
        return conn
    except Error as e:
        messagebox.showerror("Database Error", str(e))
        return None

class StudentSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information System")
        self.root.geometry("700x500")
        self.root.config(bg="#f7f7f7")

        title = tk.Label(root, text="Student Information System", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white")
        title.pack(fill=tk.X)

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_enroll_tab()
        self.create_academic_tab()
        self.create_schedule_tab()
        self.create_announcement_tab()
        self.create_fee_tab()
        self.create_view_tab()

    def create_enroll_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Enroll Student")

        tk.Label(tab, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tab, text="Name").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(tab, text="DOB (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(tab, text="Email").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(tab, text="Course").grid(row=4, column=0, padx=10, pady=5)

        self.student_id = tk.Entry(tab)
        self.name = tk.Entry(tab)
        self.dob = tk.Entry(tab)
        self.email = tk.Entry(tab)
        self.course = tk.Entry(tab)

        self.student_id.grid(row=0, column=1)
        self.name.grid(row=1, column=1)
        self.dob.grid(row=2, column=1)
        self.email.grid(row=3, column=1)
        self.course.grid(row=4, column=1)

        tk.Button(tab, text="Enroll Student", bg="#4CAF50", fg="white",
                  command=self.enroll_student).grid(row=5, column=0, columnspan=2, pady=10)

    def enroll_student(self):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO students (student_id, name, dob, email, course) VALUES (%s, %s, %s, %s, %s)",
                (self.student_id.get(), self.name.get(), self.dob.get(), self.email.get(), self.course.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Student enrolled successfully!")
            self.student_id.delete(0, tk.END)
            self.name.delete(0, tk.END)
            self.dob.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.course.delete(0, tk.END)
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_academic_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Add Academic Record")

        tk.Label(tab, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tab, text="Subject").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(tab, text="Grade").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(tab, text="Semester").grid(row=3, column=0, padx=10, pady=5)

        self.a_id = tk.Entry(tab)
        self.subject = tk.Entry(tab)
        self.grade = tk.Entry(tab)
        self.semester = tk.Entry(tab)

        self.a_id.grid(row=0, column=1)
        self.subject.grid(row=1, column=1)
        self.grade.grid(row=2, column=1)
        self.semester.grid(row=3, column=1)

        tk.Button(tab, text="Add Record", bg="#4CAF50", fg="white",
                  command=self.add_academic_record).grid(row=4, column=0, columnspan=2, pady=10)

    def add_academic_record(self):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO academic_records (student_id, subject, grade, semester) VALUES (%s, %s, %s, %s)",
                (self.a_id.get(), self.subject.get(), self.grade.get(), self.semester.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Academic record added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_schedule_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Schedule Class")

        tk.Label(tab, text="Course").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tab, text="Subject").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(tab, text="Teacher").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(tab, text="Day").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(tab, text="Time Slot").grid(row=4, column=0, padx=10, pady=5)

        self.course_s = tk.Entry(tab)
        self.sub_s = tk.Entry(tab)
        self.teacher_s = tk.Entry(tab)
        self.day_s = tk.Entry(tab)
        self.time_s = tk.Entry(tab)

        self.course_s.grid(row=0, column=1)
        self.sub_s.grid(row=1, column=1)
        self.teacher_s.grid(row=2, column=1)
        self.day_s.grid(row=3, column=1)
        self.time_s.grid(row=4, column=1)

        tk.Button(tab, text="Add Schedule", bg="#4CAF50", fg="white",
                  command=self.schedule_class).grid(row=5, column=0, columnspan=2, pady=10)

    def schedule_class(self):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO schedule (course, subject, teacher, day, time_slot) VALUES (%s, %s, %s, %s, %s)",
                (self.course_s.get(), self.sub_s.get(), self.teacher_s.get(), self.day_s.get(), self.time_s.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Class scheduled successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_announcement_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Add Announcement")

        tk.Label(tab, text="Title").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tab, text="Message").grid(row=1, column=0, padx=10, pady=5)

        self.title_a = tk.Entry(tab)
        self.message_a = tk.Entry(tab, width=50)

        self.title_a.grid(row=0, column=1)
        self.message_a.grid(row=1, column=1)

        tk.Button(tab, text="Add Announcement", bg="#4CAF50", fg="white",
                  command=self.add_announcement).grid(row=2, column=0, columnspan=2, pady=10)

    def add_announcement(self):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO announcements (title, message) VALUES (%s, %s)",
                (self.title_a.get(), self.message_a.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Announcement added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_fee_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Add Fee Record")

        tk.Label(tab, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(tab, text="Amount").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(tab, text="Due Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)

        self.fee_id = tk.Entry(tab)
        self.amount = tk.Entry(tab)
        self.due_date = tk.Entry(tab)

        self.fee_id.grid(row=0, column=1)
        self.amount.grid(row=1, column=1)
        self.due_date.grid(row=2, column=1)

        tk.Button(tab, text="Add Fee", bg="#4CAF50", fg="white",
                  command=self.add_fee).grid(row=3, column=0, columnspan=2, pady=10)

    def add_fee(self):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO fees (student_id, amount, due_date) VALUES (%s, %s, %s)",
                (self.fee_id.get(), self.amount.get(), self.due_date.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "Fee record added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_view_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="View Data")

        tk.Button(tab, text="View All Students", command=self.show_students, bg="#2196F3", fg="white").pack(pady=5)
        tk.Button(tab, text="View Academic Records", command=self.show_academic, bg="#2196F3", fg="white").pack(pady=5)
        tk.Button(tab, text="View Schedule", command=self.show_schedule, bg="#2196F3", fg="white").pack(pady=5)
        tk.Button(tab, text="View Announcements", command=self.show_announcement, bg="#2196F3", fg="white").pack(pady=5)
        tk.Button(tab, text="View Fees", command=self.show_fees, bg="#2196F3", fg="white").pack(pady=5)

    def show_students(self):
        self.show_data("SELECT * FROM students", ["ID", "Name", "DOB", "Email", "Course"], "Students")

    def show_academic(self):
        self.show_data("SELECT * FROM academic_records", ["Record ID", "Student ID", "Subject", "Grade", "Semester"], "Academic Records")

    def show_schedule(self):
        self.show_data("SELECT * FROM schedule", ["ID", "Course", "Subject", "Teacher", "Day", "Time"], "Schedule")

    def show_announcement(self):
        self.show_data("SELECT * FROM announcements", ["ID", "Title", "Message"], "Announcements")

    def show_fees(self):
        self.show_data("SELECT * FROM fees", ["ID", "Student ID", "Amount", "Due Date"], "Fees")

    def show_data(self, query, columns, title):
        conn = create_connection()
        if not conn: return
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                messagebox.showinfo("No Data", "No records found.")
                return

            win = tk.Toplevel(self.root)
            win.title(title)
            tree = ttk.Treeview(win, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150)
            for r in rows:
                tree.insert("", tk.END, values=r)
            tree.pack(fill=tk.BOTH, expand=True)
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSystemApp(root)
    root.mainloop()
