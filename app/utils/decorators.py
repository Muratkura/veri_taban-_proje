"""
Decorator fonksiyonları
Flask route'larında kullanılacak özel decorator'lar burada tanımlanır
"""
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, get_jwt_identity
from app.repositories.user_repository import UserRepository

def admin_required(f):
    """
    Admin yetkisi gerektiren endpoint decorator
    
    Bu decorator, bir route'un sadece admin kullanıcılar tarafından
    erişilebilir olmasını sağlar. Kullanıcının giriş yapmış olması
    ve admin rolüne sahip olması gerekir.
    
    Kullanım:
        @admin_bp.route('/admin-only')
        @jwt_required()
        @admin_required
        def admin_only_route():
            return jsonify({'message': 'Sadece admin erişebilir'})
    
    Args:
        f (function): Dekore edilecek fonksiyon
    
    Returns:
        function: Dekore edilmiş fonksiyon veya hata response'u
    """
    @wraps(f)  # Orijinal fonksiyon metadata'sını koru
    def decorated_function(*args, **kwargs):
        # JWT token'dan kullanıcı ID'sini al
        current_user_id = get_jwt_identity()
        
        # Kullanıcı giriş yapmamışsa hata döndür
        if not current_user_id:
            return jsonify({'message': 'Kimlik doğrulaması gerekli'}), 401
        
        # Kullanıcıyı veritabanından bul
        user = UserRepository.find_by_id(current_user_id)
        
        # Kullanıcı bulunamadıysa veya admin değilse hata döndür
        if not user or not user.is_admin():
            return jsonify({'message': 'Admin yetkisi gerekli'}), 403
        
        # Her şey tamam ise orijinal fonksiyonu çalıştır
        return f(*args, **kwargs)
    return decorated_function










