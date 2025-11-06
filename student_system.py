import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk

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
        self.root.title("🎓 Student Information System")
        self.root.geometry("950x620")
        self.root.config(bg="#F5F7FA")

        try:
            self.bg_image = Image.open("pp.avif")
            self.bg_image = self.bg_image.resize((950, 620))
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            self.root.configure(bg="#E8F5E9")

        title = tk.Label(
            self.root,
            text="🎓 Student Information System 🎓",
            font=("Segoe UI", 24, "bold"),
            bg="#2E8B57",
            fg="white",
            pady=10
        )
        title.pack(fill=tk.X)

      
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        style = ttk.Style()
        style.configure("TNotebook", background="#E8F5E9", borderwidth=0)
        style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[10, 5])
        style.map("TNotebook.Tab", background=[("selected", "#4CAF50")], foreground=[("selected", "red")])

        
        self.create_enroll_tab()
        self.create_academic_tab()
        self.create_schedule_tab()
        self.create_announcement_tab()
        self.create_fee_tab()
        self.create_view_tab()
        self.create_delete_tab()  

    def custom_button(self, parent, text, command, bg="#4CAF50"):
        return tk.Button(
            parent, text=text, bg=bg, fg="white", font=("Segoe UI", 10, "bold"),
            relief="flat", padx=10, pady=5, cursor="hand2", activebackground="#45A049",
            activeforeground="red", command=command
        )

    def create_enroll_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Enroll Student")

        form_frame = tk.Frame(tab, bg="white", bd=1, relief="solid")
        form_frame.pack(padx=40, pady=40, fill=tk.BOTH, expand=True)

        tk.Label(form_frame, text="Enroll Student", font=("Segoe UI", 16, "bold"), bg="white", fg="#2E8B57").grid(
            row=0, column=0, columnspan=2, pady=10)

        labels = ["Student ID", "Name", "DOB (YYYY-MM-DD)", "Email", "Course"]
        self.entries = []

        for i, label_text in enumerate(labels):
            tk.Label(form_frame, text=label_text, bg="white", font=("Segoe UI", 11)).grid(row=i + 1, column=0, padx=15,
                                                                                          pady=8, sticky="e")
            entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=30, bd=2, relief="groove")
            entry.grid(row=i + 1, column=1, padx=15, pady=8)
            self.entries.append(entry)

        self.custom_button(form_frame, "Enroll Student", self.enroll_student).grid(row=len(labels) + 1, column=0,
                                                                                   columnspan=2, pady=15)

    def enroll_student(self):
        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO students (student_id, name, dob, email, course) VALUES (%s, %s, %s, %s, %s)",
                tuple(entry.get() for entry in self.entries)
            )
            conn.commit()
            messagebox.showinfo("Success", "✅ Student enrolled successfully!")
            for entry in self.entries:
                entry.delete(0, tk.END)
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_academic_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Academic Record")

        self.create_form(tab, "Add Academic Record", [
            ("Student ID", "a_id"),
            ("Subject", "subject"),
            ("Grade", "grade"),
            ("Semester", "semester")
        ], self.add_academic_record)

    def add_academic_record(self):
        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO academic_records (student_id, subject, grade, semester) VALUES (%s, %s, %s, %s)",
                (self.a_id.get(), self.subject.get(), self.grade.get(), self.semester.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "📘 Academic record added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_schedule_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Class Schedule")

        self.create_form(tab, "Add Class Schedule", [
            ("Course", "course_s"),
            ("Subject", "sub_s"),
            ("Teacher", "teacher_s"),
            ("Day", "day_s"),
            ("Time Slot", "time_s")
        ], self.schedule_class)

    def schedule_class(self):
        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO schedule (course, subject, teacher, day, time_slot) VALUES (%s, %s, %s, %s, %s)",
                (self.course_s.get(), self.sub_s.get(), self.teacher_s.get(), self.day_s.get(), self.time_s.get())
            )
            conn.commit()
            messagebox.showinfo("Success", "📅 Class scheduled successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_announcement_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Announcements")

        self.create_form(tab, "Post Announcement", [
            ("Title", "title_a"),
            ("Message", "message_a")
        ], self.add_announcement)

    def add_announcement(self):
        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO announcements (title, message) VALUES (%s, %s)",
                           (self.title_a.get(), self.message_a.get()))
            conn.commit()
            messagebox.showinfo("Success", "📢 Announcement added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_fee_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Fee Record")

        self.create_form(tab, "Add Fee Record", [
            ("Student ID", "fee_id"),
            ("Amount", "amount"),
            ("Due Date (YYYY-MM-DD)", "due_date")
        ], self.add_fee)

    def add_fee(self):
        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO fees (student_id, amount, due_date) VALUES (%s, %s, %s)",
                           (self.fee_id.get(), self.amount.get(), self.due_date.get()))
            conn.commit()
            messagebox.showinfo("Success", "💰 Fee record added successfully!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def create_view_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="View Data")

        buttons = [
            ("View All Students", "SELECT * FROM students", ["ID", "Name", "DOB", "Email", "Course"], "Students"),
            ("View Academic Records", "SELECT * FROM academic_records",
             ["Record ID", "Student ID", "Subject", "Grade", "Semester"], "Academic Records"),
            ("View Schedule", "SELECT * FROM schedule", ["ID", "Course", "Subject", "Teacher", "Day", "Time"], "Schedule"),
            ("View Announcements", "SELECT * FROM announcements", ["ID", "Title", "Message"], "Announcements"),
            ("View Fees", "SELECT * FROM fees", ["ID", "Student ID", "Amount", "Due Date"], "Fees"),
        ]

        for i, (text, query, cols, title) in enumerate(buttons):
            self.custom_button(tab, text, lambda q=query, c=cols, t=title: self.show_data(q, c, t),
                               bg="#2196F3").pack(pady=8)

    def show_data(self, query, columns, title):
        conn = create_connection()
        if not conn:
            return
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

    def create_delete_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Delete Record")

        frame = tk.Frame(tab, bg="white", bd=1, relief="solid")
        frame.pack(padx=50, pady=50, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="🗑️ Delete Record", font=("Segoe UI", 16, "bold"),
                 bg="white", fg="#B71C1C").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Select Table:", bg="white", font=("Segoe UI", 11)).grid(row=1, column=0, pady=8, sticky="e")
        self.table_choice = ttk.Combobox(frame, values=["students", "academic_records", "schedule", "announcements", "fees"],
                                         font=("Segoe UI", 10), width=28, state="readonly")
        self.table_choice.grid(row=1, column=1, pady=8)

        tk.Label(frame, text="Enter Record ID:", bg="white", font=("Segoe UI", 11)).grid(row=2, column=0, pady=8, sticky="e")
        self.delete_id = tk.Entry(frame, font=("Segoe UI", 10), width=30, bd=2, relief="groove")
        self.delete_id.grid(row=2, column=1, pady=8)

        self.custom_button(frame, "Delete Record", self.delete_record, bg="#D32F2F").grid(row=3, column=0, columnspan=2, pady=20)

    def delete_record(self):
        table = self.table_choice.get()
        record_id = self.delete_id.get()

        if not table or not record_id:
            messagebox.showwarning("Input Error", "Please select a table and enter a valid record ID.")
            return

        if not messagebox.askyesno("Confirm", f"Are you sure you want to delete record ID {record_id} from '{table}'?"):
            return

        conn = create_connection()
        if not conn:
            return
        cursor = conn.cursor()

        try:
            cursor.execute(f"DELETE FROM {table} WHERE id = %s", (record_id,))
            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showinfo("Info", "No record found with that ID.")
            else:
                messagebox.showinfo("Success", f"✅ Record ID {record_id} deleted successfully from '{table}'!")
        except Error as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()


    def create_form(self, parent, title_text, fields, submit_command):
        frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
        frame.pack(padx=40, pady=40, fill=tk.BOTH, expand=True)
        tk.Label(frame, text=title_text, font=("Segoe UI", 16, "bold"), bg="white", fg="#2E8B57").grid(
            row=0, column=0, columnspan=2, pady=10)
        for i, (label, var) in enumerate(fields):
            tk.Label(frame, text=label, bg="white", font=("Segoe UI", 11)).grid(row=i + 1, column=0, padx=15, pady=8,
                                                                               sticky="e")
            entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bd=2, relief="groove")
            entry.grid(row=i + 1, column=1, padx=15, pady=8)
            setattr(self, var, entry)
        self.custom_button(frame, "Submit", submit_command).grid(row=len(fields) + 1, column=0, columnspan=2, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSystemApp(root)
    root.mainloop()
