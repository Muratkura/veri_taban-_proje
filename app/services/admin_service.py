from app.repositories.admin_repository import AdminRepository
from app.repositories.user_repository import UserRepository

class AdminService:
    @staticmethod
    def get_statistics():
        """Sistem istatistiklerini getir"""
        stats = AdminRepository.get_statistics()
        return stats
    
    @staticmethod
    def get_all_users():
        """Tüm kullanıcıları getir"""
        users = UserRepository.get_all()
        return [user.to_dict() for user in users]
    
    @staticmethod
    def get_user_by_id(user_id):
        """ID ile kullanıcı getir"""
        user = UserRepository.find_by_id(user_id)
        if not user:
            return None
        return user.to_dict()
    
    @staticmethod
    def update_user(user_id, user_data):
        """Kullanıcı güncelle"""
        user = UserRepository.update(user_id, user_data)
        if not user:
            return None, "Kullanıcı bulunamadı"
        return user.to_dict(), None
    
    @staticmethod
    def delete_user(user_id):
        """Kullanıcı sil"""
        success = UserRepository.delete(user_id)
        if not success:
            return False, "Kullanıcı bulunamadı"
        return True, None










