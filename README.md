 🎓 Student Information System (Python + MySQL)

 📘 Overview

The **Student Information System (SIS)** is a desktop-based application built using **Python (Tkinter)** and **MySQL**.
It allows users to manage and view student records through an interactive **Graphical User Interface (GUI)** with a visually appealing **image background**.

---

 🚀 Features

* 🧑‍💻 **Enroll new students**
* 🧾 **Add academic records**
* 📅 **Schedule classes**
* 📣 **Add announcements**
* 💰 **Manage fee records**
* 🔍 **View and search existing student information**
* 🖼️ **Interactive GUI with background image**

---

🧩 Technologies Used

| Component          | Technology               |
| ------------------ | ------------------------ |
| **Frontend (GUI)** | Python Tkinter           |
| **Backend**        | Python                   |
| **Database**       | MySQL                    |
| **Connector**      | `mysql-connector-python` |
| **Background**     | Static Image (PNG/JPG)   |

---

 ⚙️ Setup Instructions

1️⃣ Install Dependencies

Make sure Python and MySQL are installed on your system, then open your terminal or PowerShell and run:

---------------------------------------
pip install mysql-connector-python
pip install pillow
---------------------------------------

> `Pillow` is used to display images in the Tkinter GUI.

 2️⃣ Create the Database

Open MySQL Command Line or Workbench and run the following SQL commands:

---------------------------------------------------------------------------
CREATE DATABASE student_system;
USE student_system;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    email VARCHAR(100) UNIQUE,
    course VARCHAR(100)
);

CREATE TABLE academic_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(100),
    grade VARCHAR(10),
    semester VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course VARCHAR(100),
    subject VARCHAR(100),
    teacher VARCHAR(100),
    day VARCHAR(20),
    time_slot VARCHAR(50)
);

CREATE TABLE announcements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    message TEXT
);

CREATE TABLE fees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10,2),
    due_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
-----------------------------------------------------------------------------------------

---
 3️⃣ Run the Application

Navigate to your project folder and execute:


[python student_system.py]


Once launched, you’ll see:

* A **Tkinter window** with a custom **image background**
* Interactive buttons and input fields
* Functionality for each feature (Add/View/Update Records, etc.)

---

🧠 How It Works

1. The application connects to your **MySQL database**.
2. GUI menus let you:

   * Enroll new students
   * Add academic or fee details
   * View existing student information
3. Background image enhances the visual design while maintaining full functionality.

---

🔒 Constraints Used

| Constraint         | Description                                         |
| ------------------ | --------------------------------------------------- |
| **PRIMARY KEY**    | Ensures each record (e.g., student_id) is unique    |
| **FOREIGN KEY**    | Links student records with their fees and academics |
| **AUTO_INCREMENT** | Automatically generates record IDs                  |
| **UNIQUE**         | Prevents duplicate emails                           |
| **NOT NULL**       | Ensures required fields are filled                  |

---

🪄 Future Enhancements

* 📊 Add reporting (attendance, marksheet)
* 🧾 Export student data to Excel or PDF
* 🔐 Admin authentication system
* 🖥️ Dashboard analytics
  



