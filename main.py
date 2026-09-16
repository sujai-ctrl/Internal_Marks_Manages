import tkinter as tk
from tkinter import ttk

from database import create_table
from login import login_window
from student import student_form
from report import show_report


def dashboard():

    root = tk.Tk()

    root.title("Internal Mark Management System")
    root.geometry("1100x650")
    root.configure(bg="#f4f7fb")
    root.resizable(False, False)

    # ================= SIDEBAR =================

    sidebar = tk.Frame(
        root,
        bg="#172554",
        width=240,
        height=650
    )

    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="IMS",
        font=("Segoe UI", 32, "bold"),
        fg="white",
        bg="#172554"
    ).pack(pady=(40, 0))

    tk.Label(
        sidebar,
        text="Internal Mark System",
        font=("Segoe UI", 10),
        fg="#93c5fd",
        bg="#172554"
    ).pack(pady=(0, 40))

    def sidebar_button(text, command):

        button = tk.Button(
            sidebar,
            text=text,
            font=("Segoe UI", 11),
            anchor="w",
            padx=25,
            bg="#172554",
            fg="#e2e8f0",
            activebackground="#1e40af",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=22,
            height=2,
            command=command
        )

        button.pack(pady=4)

        return button

    sidebar_button(
        "  Dashboard",
        lambda: None
    )

    sidebar_button(
        "  Add Student",
        lambda: student_form(root)
    )

    sidebar_button(
        "  View Results",
        lambda: show_report(root)
    )

    sidebar_button(
        "  Exit",
        root.destroy
    )

    tk.Label(
        sidebar,
        text="Python Prototype\nVersion 1.0",
        font=("Segoe UI", 9),
        fg="#64748b",
        bg="#172554"
    ).pack(side="bottom", pady=25)

    # ================= MAIN AREA =================

    main = tk.Frame(
        root,
        bg="#f4f7fb"
    )

    main.pack(
        side="right",
        fill="both",
        expand=True
    )

    # Header

    header = tk.Frame(
        main,
        bg="#f4f7fb",
        height=100
    )

    header.pack(
        fill="x",
        padx=35,
        pady=25
    )

    tk.Label(
        header,
        text="Dashboard",
        font=("Segoe UI", 27, "bold"),
        bg="#f4f7fb",
        fg="#111827"
    ).pack(anchor="w")

    tk.Label(
        header,
        text="Manage and monitor student internal marks",
        font=("Segoe UI", 11),
        bg="#f4f7fb",
        fg="#6b7280"
    ).pack(anchor="w")

    # ================= CARDS =================

    cards = tk.Frame(
        main,
        bg="#f4f7fb"
    )

    cards.pack(
        fill="x",
        padx=35
    )

    def create_card(parent, title, value, subtitle):

        card = tk.Frame(
            parent,
            bg="white",
            width=220,
            height=140,
            highlightbackground="#e5e7eb",
            highlightthickness=1
        )

        card.pack(
            side="left",
            padx=(0, 20)
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 10),
            bg="white",
            fg="#6b7280"
        ).pack(anchor="w", padx=20, pady=(20, 5))

        tk.Label(
            card,
            text=value,
            font=("Segoe UI", 26, "bold"),
            bg="white",
            fg="#2563eb"
        ).pack(anchor="w", padx=20)

        tk.Label(
            card,
            text=subtitle,
            font=("Segoe UI", 9),
            bg="white",
            fg="#9ca3af"
        ).pack(anchor="w", padx=20)

        return card

    create_card(
        cards,
        "TOTAL STUDENTS",
        "0",
        "Registered students"
    )

    create_card(
        cards,
        "AVERAGE MARK",
        "0%",
        "Overall performance"
    )

    create_card(
        cards,
        "PASS RATE",
        "0%",
        "Student success rate"
    )

    # ================= QUICK ACTIONS =================

    tk.Label(
        main,
        text="Quick Actions",
        font=("Segoe UI", 18, "bold"),
        bg="#f4f7fb",
        fg="#111827"
    ).pack(
        anchor="w",
        padx=35,
        pady=(40, 15)
    )

    actions = tk.Frame(
        main,
        bg="#f4f7fb"
    )

    actions.pack(
        padx=35,
        anchor="w"
    )

    tk.Button(
        actions,
        text="+  Add New Student",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=25,
        height=2,
        command=lambda: student_form(root)
    ).pack(side="left", padx=(0, 15))

    tk.Button(
        actions,
        text="▣  View Student Results",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#2563eb",
        activebackground="#eff6ff",
        relief="solid",
        bd=1,
        cursor="hand2",
        width=25,
        height=2,
        command=lambda: show_report(root)
    ).pack(side="left")

    # ================= INFORMATION =================

    info = tk.Frame(
        main,
        bg="white",
        highlightbackground="#e5e7eb",
        highlightthickness=1
    )

    info.pack(
        fill="x",
        padx=35,
        pady=40
    )

    tk.Label(
        info,
        text="Internal Mark Calculation",
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#111827"
    ).pack(anchor="w", padx=25, pady=(20, 5))

    tk.Label(
        info,
        text="Test 1  •  25%     |     Test 2  •  25%     |     "
             "Assignment  •  25%     |     Attendance  •  25%",
        font=("Segoe UI", 10),
        bg="white",
        fg="#6b7280"
    ).pack(anchor="w", padx=25, pady=(0, 20))

    root.mainloop()


if __name__ == "__main__":

    create_table()

    login_window(dashboard)
