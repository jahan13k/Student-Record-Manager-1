import tkinter as tk
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
 student_id INTEGER PRIMARY KEY,
 name TEXT,
 course TEXT,
 email TEXT
)
""")
connection.commit()

def add_student():
 student_id = id_entry.get()
 name = name_entry.get()
 course = course_entry.get()
 email = email_entry.get()
 if student_id == "" or name == "" or course == "" or email == "": messagebox.showwarning(
 "Warning",
 "Please fill all fields."
 )
 return
 try:
     cursor.execute(
     """
     INSERT INTO students
     (student_id, name, course, email)
     VALUES (?, ?, ?, ?)
     """,
     (student_id, name, course, email)
     )
     connection.commit()
     messagebox.showinfo(
     "Success",
     "Student record added successfully."
     )
     clear_fields()
 except sqlite3.IntegrityError:
     messagebox.showerror(
     "Error",
     "Student ID already exists."
     )
def display_students():
 text_area.delete("1.0", tk.END)
 cursor.execute("SELECT * FROM students")
 records = cursor.fetchall()
 if len(records) == 0:
     text_area.insert(
     tk.END,
     "No student records found."
 )
 else:
     for record in records:
         text_area.insert(
         tk.END,
         "Student ID: " + str(record[0]) +
         "\nName: " + record[1] +
         "\nCourse: " + record[2] +
         "\nEmail: " + record[3] +
         "\n-----------------------------\n"
         )
def update_student():
 student_id = id_entry.get()
 name = name_entry.get()
 course = course_entry.get()
 email = email_entry.get()
 if student_id == "":
     messagebox.showwarning(
     "Warning",
     "Enter Student ID."
     )
     return
     cursor.execute(
     """
     UPDATE students
     SET name=?, course=?, email=?
     WHERE student_id=?
     """,
     (name, course, email, student_id)
     )
     connection.commit()
 if cursor.rowcount > 0:
     messagebox.showinfo(
     "Success",
     "Student record updated successfully."
     )
 else:
     messagebox.showwarning(
     "Warning",
     "Student ID not found."
     )
     clear_fields()
def delete_student():
 student_id = id_entry.get()
 if student_id == "":
     messagebox.showwarning(
     "Warning",
     "Enter Student ID."
     )
     return
     cursor.execute(
     "DELETE FROM students WHERE student_id=?",
     (student_id,)
     )
     connection.commit()
 if cursor.rowcount > 0:
     messagebox.showinfo(
     "Success",
     "Student record deleted successfully."
     )
 else:
     messagebox.showwarning(
     "Warning",
     "Student ID not found."
     )
     clear_fields()
def clear_fields():
 id_entry.delete(0, tk.END)
 name_entry.delete(0, tk.END)
 course_entry.delete(0, tk.END)
 email_entry.delete(0, tk.END)
# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x550")
root.resizable(False, False)
# Heading
heading = tk.Label(
 root,
 text="Student Management System",
 font=("Arial", 20, "bold")
)
heading.pack(pady=20)
# Form
form_frame = tk.Frame(root)
form_frame.pack()
tk.Label(
 form_frame,
 text="Student ID:",
 font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(
 form_frame,
 width=30
)
id_entry.grid(row=0, column=1)
tk.Label(
 form_frame,
 text="Name:",
 font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(
 form_frame,
 width=30
)
name_entry.grid(row=1, column=1)
tk.Label(
 form_frame,
 text="Course:",
 font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10)
course_entry = tk.Entry(
 form_frame,
 width=30
)
course_entry.grid(row=2, column=1)
tk.Label(
 form_frame,
 text="Email:",
 font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=10)
email_entry = tk.Entry(
 form_frame,
 width=30
)
email_entry.grid(row=3, column=1)
# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)
tk.Button(
 button_frame,
 text="Add",
 width=12,
 command=add_student
).grid(row=0, column=0, padx=5)
tk.Button(
 button_frame,
 text="Display",
 width=12,
 command=display_students
).grid(row=0, column=1, padx=5)
tk.Button(
 button_frame,
 text="Update",
 width=12,
 command=update_student
).grid(row=0, column=2, padx=5)
tk.Button(
 button_frame,
 text="Delete",
 width=12,
 command=delete_student
).grid(row=1, column=0, padx=5, pady=10)
tk.Button(
 button_frame,
 text="Clear",
 width=12,
 command=clear_fields
).grid(row=1, column=1, padx=5, pady=10)
# Display area
text_area = tk.Text(
 root,
 width=65,
 height=12
)
text_area.pack(pady=10)
# Run application
root.mainloop(
