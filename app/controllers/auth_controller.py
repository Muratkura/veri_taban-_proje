from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.repositories.user_repository import UserRepository

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Kullanıcı kaydı"""
    try:
        data = request.get_json()
        
        # Gerekli alanları kontrol et
        required_fields = ['username', 'email', 'password', 'first_name', 'last_name']
        for field in required_fields:
            if field not in data:
                return jsonify({'message': f'{field} alanı zorunludur'}), 400
        
        user, error = AuthService.register(data)
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Kullanıcı başarıyla kaydedildi',
            'user': user.to_dict()
        }), 201
    
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Kullanıcı girişi"""
    try:
        data = request.get_json()
        
        if 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Kullanıcı adı ve şifre gerekli'}), 400
        
        result, error = AuthService.login(data['username'], data['password'])
        if error:
            return jsonify({'message': error}), 401
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Mevcut kullanıcı bilgilerini getir"""
    try:
        current_user_id = get_jwt_identity()
        user = UserRepository.find_by_id(current_user_id)
        
        if not user:
            return jsonify({'message': 'Kullanıcı bulunamadı'}), 404
        
        return jsonify(user.to_dict()), 200
    
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500



