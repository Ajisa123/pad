import tkinter as tk
from tkinter import ttk, messagebox
from controllers.controller_absensi import AbsensiController
import theme

class MahasiswaDashboard:
    def __init__(self, root, user, on_logout):
        self.root = root
        self.user = user
        self.on_logout = on_logout
        
        self.root.title(f"Dashboard Mahasiswa - {self.user['nama']}")
        self.root.geometry("800x550")
        self.root.configure(bg=theme.COLOR_BG)
        
        header = tk.Frame(self.root, bg=theme.COLOR_PRIMARY, padx=25, pady=15)
        header.pack(fill="x")
        
        lbl_welcome = tk.Label(header, text=f"Selamat Datang, {self.user['nama']}", font=theme.FONT_TITLE, fg="white", bg=theme.COLOR_PRIMARY)
        lbl_welcome.pack(anchor="w")
        
        lbl_role = tk.Label(header, text=f"ID: {self.user['id']} • Role: {self.user['role'].capitalize()}", font=("Arial", 10), fg="#cbd5e1", bg=theme.COLOR_PRIMARY)
        lbl_role.pack(anchor="w", pady=(2, 0))
        
        btn_logout = tk.Button(header, text="LOGOUT", font=theme.FONT_BOLD, bg=theme.COLOR_DANGER, fg="white", bd=0, padx=15, pady=4, cursor="hand2", command=self.on_logout)
        btn_logout.place(relx=1.0, rely=0.5, anchor="e", x=-20)
        
        content = tk.Frame(self.root, bg=theme.COLOR_BG, padx=25, pady=20)
        content.pack(fill="both", expand=True)
        
        tk.Label(content, text="Status Absensi Hari Ini", font=theme.FONT_BOLD, bg=theme.COLOR_BG, fg="#333").pack(anchor="w", pady=(0, 5))
        self.lbl_realtime_status = tk.Label(content, text="Memuat data...", font=theme.FONT_MAIN, bg="white", fg="#555", anchor="w", padx=15, pady=12, bd=1, relief="solid")
        self.lbl_realtime_status.pack(fill="x", pady=(0, 20))
        
        tk.Label(content, text="Aksi Absensi", font=theme.FONT_BOLD, bg=theme.COLOR_BG, fg="#333").pack(anchor="w", pady=(0, 5))
        btn_frame = tk.Frame(content, bg=theme.COLOR_BG)
        btn_frame.pack(fill="x", pady=(0, 25))
        
        # PERBAIKAN SINKRONISASI: ipady dipindah ke fungsi .pack()
        self.btn_masuk = tk.Button(btn_frame, text="✓ ABSEN MASUK", font=theme.FONT_BOLD, bg=theme.COLOR_ACCENT, fg="white", bd=0, padx=20, cursor="hand2", command=self.handle_masuk)
        self.btn_masuk.pack(side="left", padx=(0, 15), ipady=8)
        
        self.btn_pulang = tk.Button(btn_frame, text="✗ ABSEN PULANG", font=theme.FONT_BOLD, bg="#ff4d4d", fg="white", bd=0, padx=20, cursor="hand2", command=self.handle_pulang)
        self.btn_pulang.pack(side="left", ipady=8)
        
        tk.Label(content, text="Riwayat Absensi", font=theme.FONT_BOLD, bg=theme.COLOR_BG, fg="#333").pack(anchor="w", pady=(5, 5))
        
        cols = ('tanggal', 'jam_masuk', 'jam_pulang', 'status', 'keterangan')
        self.tree = ttk.Treeview(content, columns=cols, show='headings')
        
        self.tree.heading('tanggal', text='Tanggal')
        self.tree.heading('jam_masuk', text='Jam Masuk')
        self.tree.heading('jam_pulang', text='Jam Pulang')
        self.tree.heading('status', text='Status')
        self.tree.heading('keterangan', text='Keterangan')
        
        for col in cols:
            self.tree.column(col, width=140, anchor="center")
            
        self.tree.tag_configure('row_hadir', background='#17b978', foreground='white')
            
        self.tree.pack(fill="both", expand=True)
        self.sync_data_ui()

    def sync_data_ui(self):
        status = AbsensiController.ambil_status(self.user['id'])
        if status:
            j_masuk, j_pulang, stat = status['jam_masuk'], status['jam_pulang'], status['status']
            j_pulang_str = j_pulang if j_pulang else "-"
            self.lbl_realtime_status.config(text=f"✓ {stat.upper()} | Masuk: {j_masuk} | Pulang: {j_pulang_str}", fg="#1b5e20")
        else:
            self.lbl_realtime_status.config(text="Belum melakukan absensi pada hari ini.", fg="#b71c1c")
        
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for row in AbsensiController.ambil_riwayat(self.user['id']):
            processed_row = [str(item) if item is not None else "-" for item in row]
            self.tree.insert('', tk.END, values=processed_row, tags=('row_hadir',))

    def handle_masuk(self):
        success, msg = AbsensiController.proses_masuk(self.user['id'])
        if success:
            messagebox.showinfo("Berhasil", msg)
            self.sync_data_ui()
        else:
            messagebox.showwarning("Peringatan", msg)

    def handle_pulang(self):
        success, msg = AbsensiController.proses_pulang(self.user['id'])
        if success:
            messagebox.showinfo("Berhasil", msg)
            self.sync_data_ui()
        else:
            messagebox.showwarning("Peringatan", msg)