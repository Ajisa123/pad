from models.model_user import UserModel

class AuthController:
    @staticmethod
    def login(username, password):
        if not username or not password:
            return None, "Kolom Username dan Password wajib diisi!"
        
        user = UserModel.authenticate(username, password)
        if user:
            return user, "Verifikasi Berhasil!"
        return None, "Username atau Password salah!"