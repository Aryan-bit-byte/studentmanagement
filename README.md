# studentmanagement

# Student Management System

A simple **Student Management System** built using **Python** and **SQLite3**.
This project helps manage student records through a terminal-based menu system.

---

# Features

* Add Student
* View All Students
* Search Student by Roll Number
* Update Student Marks
* Update Student Attendance
* Delete Student Record
* SQLite Database Integration

---

# Technologies Used

* Python
* SQLite3

---

# Project Structure

```bash
studentmanagement/
│
├── studentmanagment.py
├── Student.db
└── README.md
```

---

# Database Schema

## Table: students

| Column Name | Data Type             |
| ----------- | --------------------- |
| Roll_No     | INTEGER (Primary Key) |
| Name        | TEXT                  |
| Marks       | INTEGER               |
| Attendence  | INTEGER               |

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/studentmanagement.git
```

## 2. Open Project Folder

```bash
cd studentmanagement
```

## 3. Run the Project

```bash
python studentmanagment.py
```

---

# Menu Options

```text
1. Add Student
2. View Student
3. Search Student
4. Update Marks
5. Update Attendence
6. Delete Student
7. Exit
```

---

# Example Output

```text
Welcome to STUDENT MANAGEMENT SYSTEM

1.Add Student
2.View Student
3.Search Student
4.Update Marks
5.Update Attendence
6.Delete Student
7.Exit

Enter your choice:
```

---

# Future Improvements

* GUI using Tkinter
* Login System
* Grade Calculator
* Search by Name
* Subject-wise Marks
* Percentage Calculator

---

# Author

Made by **Aryan-bit-byte**

  

#
