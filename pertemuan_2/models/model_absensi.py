import sqlite3
from database import get_connection
from datetime import datetime

class AbsensiModel:
    @staticmethod
    def get_riwayat(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT tanggal, jam_masuk, jam_pulang, status, keterangan FROM absensi WHERE user_id = ? ORDER BY tanggal DESC', (user_id,))
        rows = cursor.fetchall()
        result = [tuple(row) for row in rows]
        conn.close()
        return result

    @staticmethod
    def get_status_hari_ini(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        tanggal = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('SELECT jam_masuk, jam_pulang, status FROM absensi WHERE user_id = ? AND tanggal = ?', (user_id, tanggal))
        row = cursor.fetchone()
        
        result = None
        if row:
            result = {'jam_masuk': row['jam_masuk'], 'jam_pulang': row['jam_pulang'], 'status': row['status']}
        conn.close()
        return result

    @staticmethod
    def absen_masuk(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        tanggal = datetime.now().strftime('%Y-%m-%d')
        jam_masuk = datetime.now().strftime('%H:%M:%S')
        
        try:
            cursor.execute('''
                INSERT INTO absensi (user_id, tanggal, jam_masuk, status, keterangan) 
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, tanggal, jam_masuk, 'hadir', 'Tepat Waktu'))
            conn.commit()
            return True, "Absen masuk berhasil!"
        except sqlite3.IntegrityError:
            return False, "Anda sudah melakukan absen masuk hari ini!"
        finally:
            conn.close()

    @staticmethod
    def absen_pulang(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        tanggal = datetime.now().strftime('%Y-%m-%d')
        jam_pulang = datetime.now().strftime('%H:%M:%S')
        
        cursor.execute('SELECT id, jam_pulang FROM absensi WHERE user_id = ? AND tanggal = ?', (user_id, tanggal))
        row = cursor.fetchone()
        
        if not row:
            conn.close()
            return False, "Gagal! Anda belum absen masuk hari ini."
        if row['jam_pulang'] is not None:
            conn.close()
            return False, "Anda sudah melakukan absen pulang hari ini!"
        
        cursor.execute('UPDATE absensi SET jam_pulang = ? WHERE id = ?', (jam_pulang, row['id']))
        conn.commit()
        conn.close()
        return True, "Absen pulang berhasil!"
    
    @staticmethod
    def get_all_rekap():
        conn = get_connection()
        cursor = conn.cursor()
        # Mengambil data absensi digabung dengan nama mahasiswa dari tabel users
        cursor.execute('''
            SELECT u.nama, a.tanggal, a.jam_masuk, a.jam_pulang, a.status, a.keterangan 
            FROM absensi a 
            JOIN users u ON a.user_id = u.id 
            ORDER BY a.tanggal DESC
        ''')
        rows = cursor.fetchall()
        result = [tuple(row) for row in rows]
        conn.close()
        return result