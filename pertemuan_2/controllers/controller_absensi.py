from models.model_absensi import AbsensiModel

class AbsensiController:
    @staticmethod
    def proses_masuk(user_id):
        return AbsensiModel.absen_masuk(user_id)
        
    @staticmethod
    def proses_pulang(user_id):
        return AbsensiModel.absen_pulang(user_id)

    @staticmethod
    def ambil_status(user_id):
        return AbsensiModel.get_status_hari_ini(user_id)
        
    @staticmethod
    def ambil_riwayat(user_id):
        return AbsensiModel.get_riwayat(user_id)