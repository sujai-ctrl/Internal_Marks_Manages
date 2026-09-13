import tkinter as tk
from tkinter import messagebox

from database import add_student
from marks import calculate_internal


def student_form(parent):

    window = tk.Toplevel(parent)
    window.title("Add Student")
    window.geometry("450x600")

    labels = [
        "Register Number",
        "Student Name",
        "Department",
        "Semester",
        "Test 1 Mark",
        "Test 2 Mark",
        "Assignment Mark",
        "Attendance Mark"
    ]

    entries = []

    for label in labels:

        tk.Label(
            window,
            text=label,
            font=("Arial", 10)
        ).pack(pady=(10, 2))

        entry = tk.Entry(window, width=35)
        entry.pack()

        entries.append(entry)

    def save_student():

        try:

            register_no = entries[0].get()
            name = entries[1].get()
            department = entries[2].get()
            semester = entries[3].get()

            test1 = float(entries[4].get())
            test2 = float(entries[5].get())
            assignment = float(entries[6].get())
            attendance = float(entries[7].get())

            if not register_no or not name:
                messagebox.showwarning(
                    "Warning",
                    "Enter student details"
                )
                return

            internal_mark = calculate_internal(
                test1,
                test2,
                assignment,
                attendance
            )

            data = (
                register_no,
                name,
                department,
                semester,
                test1,
                test2,
                assignment,
                attendance,
                internal_mark
            )

            add_student(data)

            messagebox.showinfo(
                "Success",
                f"Student added successfully!\n\n"
                f"Internal Mark: {internal_mark}"
            )

            window.destroy()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid marks"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    tk.Button(
        window,
        text="Calculate & Save",
        width=20,
        command=save_student
    ).pack(pady=25)
