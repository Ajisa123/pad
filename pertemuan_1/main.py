import tkinter as tk
from tkinter import messagebox

# --- WINDOW SETUP ---
root = tk.Tk()
root.title("Developer Profile")
root.geometry("450x550")
root.config(bg="#0F172A") # Slate dark background

# --- MAIN CARD CONTAINER ---
# Menggunakan padding natural agar proporsi card selalu seimbang
card = tk.Frame(
    root,
    bg="#1E293B", # Darker slate untuk card
    bd=0,
    padx=25,
    pady=25
)
card.place(relx=0.5, rely=0.5, anchor="center")

# Garis Aksen Atas (Menyerupai tab border pada code editor)
accent_bar = tk.Frame(card, bg="#38BDF8", height=4, width=350)
accent_bar.pack(fill="x", pady=(0, 15))

# --- HEADER SECTION ---
title = tk.Label(
    card,
    text="~/profile/ajisa",
    font=("Consolas", 16, "bold"),
    fg="#38BDF8",
    bg="#1E293B"
)
title.pack(anchor="w")

subtitle = tk.Label(
    card,
    text="Information Systems Student",
    font=("Segoe UI", 10),
    fg="#94A3B8",
    bg="#1E293B"
)
subtitle.pack(anchor="w", pady=(0, 15))

# Garis Pembatas Tipis
line = tk.Frame(card, bg="#334155", height=1)
line.pack(fill="x", pady=(0, 20))

# --- DATA BIODATA (MONOSPACE ALIGNED) ---
# Menggunakan spasi statis yang pas agar rapi di font monospace
info = (
    "👤 Name      : AJI SAKA TIRTA ALFITRAH\n"
    "🎂 Age       : 21 years old\n"
    "📍 Location  : RIAU\n"
    "🎓 Major     : Information Systems\n"
    "📚 Semester  : 6\n"
    "💻 Skills    : Python, SQL, HTML, CSS\n"
    "🎵 Hobby     : DESAIN GRAFIS\n"
    "✨ Motto     : Keep Calm"
)

# Box Khusus Data (Berfungsi seperti blockquote / kotak terminal mini)
profile_box = tk.Label(
    card,
    text=info,
    justify="left",
    anchor="w",
    font=("Consolas", 10),
    fg="#E2E8F0",
    bg="#0F172A", # Latar belakang box lebih gelap dari card
    padx=15,
    pady=15,
    bd=1,
    relief="solid",
    highlightbackground="#334155"
)
profile_box.pack(fill="x", pady=(0, 25))

# --- TOMBOL INTERAKTIF ---
def on_ping():
    messagebox.showinfo("Status", "Connection Successful! Let's build something awesome. 🚀")

btn_ping = tk.Button(
    card,
    text="> PING ME",
    font=("Consolas", 10, "bold"),
    bg="#38BDF8",
    fg="#0F172A",
    activebackground="#0EA5E9",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=on_ping,
    pady=8
)
btn_ping.pack(fill="x")

# --- FOOTER ---
footer = tk.Label(
    card,
    text="print('Made with Python');",
    font=("Consolas", 8, "italic"),
    fg="#64748B",
    bg="#1E293B"
)
footer.pack(pady=(20, 0))

root.mainloop()