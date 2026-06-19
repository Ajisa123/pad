from models.model_absensi import AbsensiModel

class ReportController:
    @staticmethod
    def ambil_semua_rekap():
        # Mengambil data rekap dari model absensi
        return AbsensiModel.get_all_rekap()