import tkinter as tk
from tkinter import ttk

from database import get_students
from marks import get_grade


def show_report(parent):

    window = tk.Toplevel(parent)
    window.title("Student Internal Mark Report")
    window.geometry("1000x500")

    columns = (
        "Register No",
        "Name",
        "Department",
        "Semester",
        "Test 1",
        "Test 2",
        "Assignment",
        "Attendance",
        "Internal Mark",
        "Grade"
    )

    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    for column in columns:

        table.heading(column, text=column)

        table.column(
            column,
            width=100
        )

    table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    students = get_students()

    for student in students:

        internal_mark = student[9]
        grade = get_grade(internal_mark)

        table.insert(
            "",
            "end",
            values=(
                student[1],
                student[2],
                student[3],
                student[4],
                student[5],
                student[6],
                student[7],
                student[8],
                student[9],
                grade
            )
        )