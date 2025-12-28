"""
Kimlik doğrulama servisi
Kullanıcı kaydı ve giriş işlemlerini yönetir
"""
from app.repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta

class AuthService:
    """
    Kimlik doğrulama işlemleri için servis sınıfı
    Kullanıcı kaydı ve giriş işlemlerini yönetir
    """
    @staticmethod
    def register(user_data):
        """Yeni kullanıcı kaydı"""
        # Kullanıcı adı kontrolü
        if UserRepository.find_by_username(user_data['username']):
            return None, "Bu kullanıcı adı zaten kullanılıyor"
        
        # E-posta kontrolü
        if UserRepository.find_by_email(user_data['email']):
            return None, "Bu e-posta adresi zaten kayıtlı"
        
        # Kullanıcı oluştur
        user = UserRepository.create(user_data)
        return user, None
    
    @staticmethod
    def login(username, password):
        """Kullanıcı girişi"""
        user = UserRepository.find_by_username(username)
        
        if not user:
            return None, "Kullanıcı adı veya şifre hatalı"
        
        if not user.check_password(password):
            return None, "Kullanıcı adı veya şifre hatalı"
        
        # JWT token oluştur
        access_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(days=7),
            additional_claims={"role": user.role}
        )
        
        return {
            "user": user.to_dict(),
            "access_token": access_token
        }, None










