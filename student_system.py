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
        print("Error connecting to MySQL:", e)
        return None
def main():
    while True:
        print("\n===== Student Information System =====")
        print("1. Enroll Student")
        print("2. Add Academic Record")
        print("3. Schedule Class")
        print("4. Add Announcement")
        print("5. Add Fee Record")
        print("6. View Student Information")
        print("7. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            enroll_student()
        elif choice == "2":
            add_academic_record()
        elif choice == "3":
            schedule_class()
        elif choice == "4":
            add_announcement()
        elif choice == "5":
            add_fee()
        elif choice == "6":
            view_student_info()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option!")
def enroll_student():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    student_id = input("Student ID: ")
    name = input("Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    email = input("Email: ")
    course = input("Course: ")

    try:
        cursor.execute(
            "INSERT INTO students (student_id, name, dob, email, course) VALUES (%s, %s, %s, %s, %s)",
            (student_id, name, dob, email, course)
        )
        conn.commit()
        print("Student enrolled successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def add_academic_record():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    student_id = input("Student ID: ")
    subject = input("Subject: ")
    grade = input("Grade: ")
    semester = input("Semester: ")

    try:
        cursor.execute(
            "INSERT INTO academic_records (student_id, subject, grade, semester) VALUES (%s, %s, %s, %s)",
            (student_id, subject, grade, semester)
        )
        conn.commit()
        print("Academic record added successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def schedule_class():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    course = input("Course: ")
    subject = input("Subject: ")
    teacher = input("Teacher: ")
    day = input("Day: ")
    time_slot = input("Time Slot: ")

    try:
        cursor.execute(
            "INSERT INTO schedule (course, subject, teacher, day, time_slot) VALUES (%s, %s, %s, %s, %s)",
            (course, subject, teacher, day, time_slot)
        )
        conn.commit()
        print("Class scheduled successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def add_announcement():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    title = input("Title: ")
    message = input("Message: ")

    try:
        cursor.execute(
            "INSERT INTO announcements (title, message) VALUES (%s, %s)",
            (title, message)
        )
        conn.commit()
        print("Announcement added successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def add_fee():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    student_id = input("Student ID: ")
    amount = input("Amount: ")
    due_date = input("Due Date (YYYY-MM-DD): ")

    try:
        cursor.execute(
            "INSERT INTO fees (student_id, amount, due_date) VALUES (%s, %s, %s)",
            (student_id, amount, due_date)
        )
        conn.commit()
        print("Fee record added successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def view_student_info():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()

    student_id = input("Enter Student ID: ")

    try:
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        student = cursor.fetchone()
        if student:
            print("Student Info:", student)
        else:
            print("Student not found.")
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    main()
