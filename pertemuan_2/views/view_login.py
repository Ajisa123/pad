import tkinter as tk
from tkinter import ttk, messagebox
from controllers.controller_auth import AuthController
import theme

class LoginView:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        
        self.root.title("Sistem Absensi - Login")
        self.root.geometry("380x420")
        self.root.configure(bg=theme.COLOR_BG)
        
        header = tk.Frame(self.root, bg=theme.COLOR_PRIMARY, height=110)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        lbl_title = tk.Label(header, text="Sistem Absensi", font=theme.FONT_TITLE, fg="white", bg=theme.COLOR_PRIMARY)
        lbl_title.pack(pady=(30, 2))
        lbl_sub = tk.Label(header, text="Manajemen Kehadiran", font=("Arial", 9, "italic"), fg="#cbd5e1", bg=theme.COLOR_PRIMARY)
        lbl_sub.pack()
        
        form = tk.Frame(self.root, bg=theme.COLOR_BG, padx=35, pady=25)
        form.pack(fill="both", expand=True)
        
        tk.Label(form, text="Username", font=theme.FONT_MAIN, bg=theme.COLOR_BG, fg="#333").pack(anchor="w", pady=(5, 2))
        self.entry_user = ttk.Entry(form, font=("Arial", 10))
        self.entry_user.pack(fill="x", ipady=3, pady=(0, 15))
        
        tk.Label(form, text="Password", font=theme.FONT_MAIN, bg=theme.COLOR_BG, fg="#333").pack(anchor="w", pady=(5, 2))
        self.entry_pass = ttk.Entry(form, show="*", font=("Arial", 10))
        self.entry_pass.pack(fill="x", ipady=3, pady=(0, 25))
        
        btn_login = tk.Button(form, text="LOGIN", font=theme.FONT_BOLD, bg=theme.COLOR_PRIMARY, fg="white", bd=0, cursor="hand2", command=self.handle_login)
        btn_login.pack(fill="x", ipady=6, pady=4)
        
        btn_clear = tk.Button(form, text="CLEAR", font=theme.FONT_BOLD, bg="#e2e8f0", fg="#475569", bd=0, cursor="hand2", command=self.handle_clear)
        btn_clear.pack(fill="x", ipady=6, pady=4)
        
    def handle_login(self):
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()
        
        user, msg = AuthController.login(username, password)
        if user:
            messagebox.showinfo("Sukses", msg)
            self.on_login_success(user)
        else:
            messagebox.showerror("Gagal", msg)
            
    def handle_clear(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)