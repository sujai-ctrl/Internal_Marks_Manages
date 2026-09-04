import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def login_window(open_dashboard):

    root = tk.Tk()
    root.title("Internal Mark Management System")
    root.geometry("900x550")
    root.resizable(False, False)
    root.configure(bg="#f4f7fb")

    # ---------------- LEFT PANEL ----------------

    left = tk.Frame(
        root,
        bg="#172554",
        width=450,
        height=550
    )
    left.pack(side="left", fill="both")
    left.pack_propagate(False)

    tk.Label(
        left,
        text="INTERNAL",
        font=("Segoe UI", 30, "bold"),
        fg="white",
        bg="#172554"
    ).pack(pady=(120, 0))

    tk.Label(
        left,
        text="MARK MANAGEMENT",
        font=("Segoe UI", 22, "bold"),
        fg="#60a5fa",
        bg="#172554"
    ).pack()

    tk.Label(
        left,
        text="Student Academic Performance System",
        font=("Segoe UI", 11),
        fg="#cbd5e1",
        bg="#172554"
    ).pack(pady=15)

    tk.Label(
        left,
        text="✓ Student Management\n"
             "✓ Automatic Mark Calculation\n"
             "✓ Result Management\n"
             "✓ Academic Reports",
        font=("Segoe UI", 11),
        justify="left",
        fg="#e2e8f0",
        bg="#172554"
    ).pack(pady=25)

    # ---------------- RIGHT PANEL ----------------

    right = tk.Frame(
        root,
        bg="white",
        width=450,
        height=550
    )
    right.pack(side="right", fill="both")
    right.pack_propagate(False)

    tk.Label(
        right,
        text="Welcome Back",
        font=("Segoe UI", 25, "bold"),
        bg="white",
        fg="#111827"
    ).pack(pady=(95, 5))

    tk.Label(
        right,
        text="Login to continue",
        font=("Segoe UI", 11),
        bg="white",
        fg="#6b7280"
    ).pack(pady=(0, 30))

    # Username

    tk.Label(
        right,
        text="Username",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="#374151"
    ).pack(anchor="w", padx=75)

    username = tk.Entry(
        right,
        font=("Segoe UI", 11),
        width=30,
        bd=1,
        relief="solid"
    )
    username.pack(pady=(7, 18), ipady=8)

    # Password

    tk.Label(
        right,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="#374151"
    ).pack(anchor="w", padx=75)

    password = tk.Entry(
        right,
        font=("Segoe UI", 11),
        width=30,
        show="*",
        bd=1,
        relief="solid"
    )
    password.pack(pady=(7, 25), ipady=8)

    # Login function

    def check_login():

        user = username.get().strip()
        pwd = password.get().strip()

        if user == "admin" and pwd == "1234":

            root.destroy()
            open_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password.\n\n"
                "Please try again."
            )

    login_button = tk.Button(
        right,
        text="LOGIN",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        height=2,
        command=check_login
    )
    login_button.pack()

    tk.Label(
        right,
        text="Prototype Login",
        font=("Segoe UI", 9),
        bg="white",
        fg="#9ca3af"
    ).pack(pady=(25, 3))

    tk.Label(
        right,
        text="Username: admin    Password: 1234",
        font=("Segoe UI", 9),
        bg="white",
        fg="#6b7280"
    ).pack()

    username.focus()

    root.bind("<Return>", lambda event: check_login())

    root.mainloop()