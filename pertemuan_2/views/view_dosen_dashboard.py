import tkinter as tk
from tkinter import ttk
from controllers.controller_report import ReportController
import theme

class DosenDashboard:
    def __init__(self, root, user, on_logout):
        self.root = root
        self.user = user
        self.on_logout = on_logout
        
        # Judul & Ukuran Window Dosen
        self.root.title(f"Dashboard Dosen - {self.user['nama']}")
        self.root.geometry("850x550")
        self.root.configure(bg=theme.COLOR_BG)
        
        # Header Panel Dosen
        header = tk.Frame(self.root, bg=theme.COLOR_PRIMARY, padx=25, pady=15)
        header.pack(fill="x")
        
        lbl_welcome = tk.Label(header, text=f"Selamat Datang, {self.user['nama']}", font=theme.FONT_TITLE, fg="white", bg=theme.COLOR_PRIMARY)
        lbl_welcome.pack(anchor="w")
        
        lbl_role = tk.Label(header, text=f"ID: {self.user['id']} • Role: {self.user['role'].capitalize()}", font=("Arial", 10), fg="#cbd5e1", bg=theme.COLOR_PRIMARY)
        lbl_role.pack(anchor="w", pady=(2, 0))
        
        btn_logout = tk.Button(header, text="LOGOUT", font=theme.FONT_BOLD, bg=theme.COLOR_DANGER, fg="white", bd=0, padx=15, pady=4, cursor="hand2", command=self.on_logout)
        btn_logout.place(relx=1.0, rely=0.5, anchor="e", x=-20)
        
        # Konten Utama
        content = tk.Frame(self.root, bg=theme.COLOR_BG, padx=25, pady=20)
        content.pack(fill="both", expand=True)
        
        # Baris Judul Tabel & Tombol Refresh
        top_frame = tk.Frame(content, bg=theme.COLOR_BG)
        top_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(top_frame, text="Panel Rekapitulasi Presensi Seluruh Mahasiswa", font=theme.FONT_BOLD, bg=theme.COLOR_BG, fg="#333").pack(side="left", anchor="w")
        
        btn_refresh = tk.Button(top_frame, text="🔄 REFRESH DATA", font=("Arial", 9, "bold"), bg=theme.COLOR_PRIMARY, fg="white", bd=0, padx=10, pady=4, cursor="hand2", command=self.load_data_rekap)
        btn_refresh.pack(side="right")
        
        # Pembuatan Struktur Tabel Rekap Mahasiswa
        cols = ('nama', 'tanggal', 'jam_masuk', 'jam_pulang', 'status', 'keterangan')
        self.tree = ttk.Treeview(content, columns=cols, show='headings')
        
        self.tree.heading('nama', text='Nama Mahasiswa')
        self.tree.heading('tanggal', text='Tanggal')
        self.tree.heading('jam_masuk', text='Jam Masuk')
        self.tree.heading('jam_pulang', text='Jam Pulang')
        self.tree.heading('status', text='Status')
        self.tree.heading('keterangan', text='Keterangan')
        
        # Pengaturan Lebar Kolom
        self.tree.column('nama', width=180, anchor="w")
        for col in cols[1:]:
            self.tree.column(col, width=110, anchor="center")
            
        # Desain Baris Tabel (Hijau soft agar teks hitam tetap terbaca jelas)
        self.tree.tag_configure('row_style', background='#e8f5e9')
            
        self.tree.pack(fill="both", expand=True)
        
        # Memuat data pertama kali saat halaman dibuka
        self.load_data_rekap()

    def load_data_rekap(self):
        """Fungsi untuk mengambil data real-time dari database ke tabel"""
        # Bersihkan tabel lama
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Ambil data terbaru melalui Controller
        rekap_data = ReportController.ambil_semua_rekap()
        
        # Masukkan data ke dalam tabel Treeview
        for row in rekap_data:
            processed_row = [str(item) if item is not None else "-" for item in row]
            self.tree.insert('', tk.END, values=processed_row, tags=('row_style',))