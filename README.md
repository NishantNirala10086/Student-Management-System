# Student-Management-System
The Student Information System (SIS) is a software application designed to manage and organize student-related data in a digital format. It helps schools, colleges, and universities to store, track, and update student records efficiently.  

**Language:** Python
**Database:** MySQL
---

## Project Overview

A simple console-based **Student Information System (SIS)** built with **Python** and **MySQL**. The application allows administrators to enroll students, add academic records, schedule classes, post announcements, manage fee records, and view student information via a text-based menu.

This project demonstrates how to connect Python to a MySQL database, perform CRUD operations, and follow basic security practices like using parameterized queries.

---

## Key Features

* Enroll new students (student ID, name, DOB, email, course)
* Add academic records (subject, grade, semester)
* Schedule classes (course, subject, teacher, day, time slot)
* Post announcements (title, message)
* Record fees (student ID, amount, due date)
* View student information by student ID

---

## Technology Stack

* Python 3.8+ (or newer)
* MySQL / MariaDB
* `mysql-connector-python` library

---

## Prerequisites

1. Install Python (3.8+).
2. Install MySQL or MariaDB and create a server user.
3. Install Python package:

```bash
pip install mysql-connector-python
```

---

## Database Setup

1. Open MySQL command line (or Workbench) and run:

```sql
CREATE DATABASE student_system;
USE student_system;

CREATE TABLE students (
    student_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    course VARCHAR(50)
);

CREATE TABLE academic_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20),
    subject VARCHAR(50),
    grade VARCHAR(5),
    semester VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course VARCHAR(50),
    subject VARCHAR(50),
    teacher VARCHAR(50),
    day VARCHAR(20),
    time_slot VARCHAR(20)
);

CREATE TABLE announcements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    message TEXT
);

CREATE TABLE fees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20),
    amount DECIMAL(10,2),
    due_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

2. (Optional) Insert sample data for testing:

```sql
INSERT INTO students (student_id, name, dob, email, course)
VALUES ('S001', 'John Doe', '2005-05-12', 'john@example.com', 'Computer Science');
```

---

## Configuration

In the Python script, update your MySQL connection credentials inside the `create_connection()` function:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_system"
)
```

Replace `YOUR_PASSWORD` with your MySQL password.


## How to Run

1. Ensure MySQL server is running and the `student_system` database exists.
2. Run the Python program from the terminal:

```bash
python student_system.py
```

3. Use the numbered menu to interact with the application (enroll, add records, view info, etc.).


## Code Structure (high level)

* `create_connection()` — connects to MySQL and returns a connection object.
* Menu loop (`main()`) — displays options and calls the corresponding functions.
* Functions for each feature:

  * `enroll_student()`
  * `add_academic_record()`
  * `schedule_class()`
  * `add_announcement()`
  * `add_fee()`
  * `view_student_info()`
* Each function opens a DB connection, creates a cursor, executes parameterized SQL queries, commits (if needed), and closes the connection.

## Security Notes

* All SQL statements use **parameterized queries** (placeholders like `%s`) to prevent SQL injection.
* Use a database user with **least privileges** for production deployments.
* Validate user input (dates, numeric values, email format) before sending to DB where possible.

## Troubleshooting

* `Access denied`: Check your MySQL username/password and host.
* `Unknown database`: Make sure `student_system` exists (`SHOW DATABASES;`).
* `Table doesn't exist`: Ensure the SQL schema was executed successfully.
* Connection timeouts: Confirm MySQL is running and listening on the expected port (default 3306).

## Future Improvements

* Add a GUI (Tkinter, PyQt, or web frontend with Flask/Django).
* Add authentication and role-based access (admin vs staff).
* Add update/delete operations and better error handling.
* Migrate to an ORM (SQLAlchemy) for cleaner code and easier migrations.
* Add logging, input validation, and automated tests.
