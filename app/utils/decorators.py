from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt, get_jwt_identity
from app.repositories.user_repository import UserRepository

def admin_required(f):
    """Admin yetkisi gerektiren endpoint decorator"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        if not current_user_id:
            return jsonify({'message': 'Kimlik doğrulaması gerekli'}), 401
        
        user = UserRepository.find_by_id(current_user_id)
        if not user or not user.is_admin():
            return jsonify({'message': 'Admin yetkisi gerekli'}), 403
        
        return f(*args, **kwargs)
    return decorated_function




