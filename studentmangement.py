import sqlite3

conn=sqlite3.connect("Student.db")
cursor=conn.cursor()

cursor.execute("""
      CREATE TABLE IF NOT EXISTS students( 
               Roll_No INTEGER PRIMARY KEY,
               Name TEXT,
               Marks INTEGER,
               Attendence INTEGER
               )
             """)
print("Table created successfully")
conn.commit()

def add_student():
    roll_number=int(input("Enter your roll number:"))
    name=(input("Enter Students name:"))
    marks=float(input("Enter Students marks:"))

    cursor.execute(
          "INSERT INTO students VALUES(?,?,?,?)" # ?=checks automatically type
          ,(roll_number,name,marks,0)       
                )
    conn.commit()
    print("Student added sucessfully.")

def view_student():
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    if len(students)==0:
       print("Student not found")
       return
    for student in students:
     print("STUDENTS DETAILS ARE:")
     print(f"Roll number: {student[0]}")
     print(f"Name: {student[1]}")
     print(f"Marks: {student[2]}")
     print(f"Attendence: {student[3]}")
     print("-"*30)

def search_student():
    search=int(input("Enter roll number:"))
    cursor.execute(
        "SELECT * FROM students WHERE Roll_No=?",
    (search,)
    )
    student=cursor.fetchone()
    if(student):
         print("STUDENTS DETAILS ARE:")
         print(f"Roll number: {student[0]}")
         print(f"Name: {student[1]}")
         print(f"Marks: {student[2]}")
         print(f"Attendence: {student[3]}%")
    else:
        print("Details not found. Please try again.")
        
def update_marks():
    roll=int(input("Enter Roll number:"))
    new_marks=int(input("Enter new marks:"))
    cursor.execute(
        "UPDATE students SET marks=? WHERE Roll_No=?",
        (new_marks,roll)
    ) 
    conn.commit()
    if (cursor.rowcount>0):
        print("Marks updated sucessfully.")
    else:
        print("Marks not updated")

def update_attendence():
    roll=int(input("Enter your roll number:"))
    new_attendence=int(input("Enter new attendance:"))
    cursor.execute(
        "UPDATE students SET attendence =? WHERE Roll_No=?",
        (new_attendence,roll)
    )
    conn.commit()
    if (cursor.rowcount>0):
        print("Attendence updated sucessfully.")
    else:
        print("Attendence not updated")

def delete_students():
    roll=int(input("Enter students roll number:")) 
    cursor.execute(
        "DELETE FROM students WHERE Roll_No=?",
        (roll,)
    )
    conn.commit()
    if (cursor.rowcount>0):
        print("Student deleted sucessfully.")
    else:
        print("Student not found.")


print("Table created successfully")
conn.commit()

while True:
    print("Welcome to STUDENT MANAGEMENT SYSTEM")
    print("1.Add Student")
    print("2.View all Students")
    print("3.Search Student")
    print("4.Update Marks")
    print("5.Update Attendence")
    print("6.Delete Student")
    print("7.Exit")

    choice=int(input("Enter your choice:"))
    if(choice==1):
      add_student()
    elif(choice==2):
        view_student()
    elif(choice==3):    
        search_student()
    elif(choice==4):
        update_marks()
    elif(choice==5):
        update_attendence()
    elif(choice==6):
        delete_students()
    elif(choice==7):
        print("Thank You.")
        break
    else:
        print("Invalid choice. Please try again.")
conn.close()        