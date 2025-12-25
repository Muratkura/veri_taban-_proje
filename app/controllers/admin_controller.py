from flask import Blueprint, request, jsonify
from app.services.admin_service import AdminService
from app.services.book_service import AuthorService, CategoryService
from flask_jwt_extended import jwt_required
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/statistics', methods=['GET'])
@jwt_required()
@admin_required
def get_statistics():
    """Sistem istatistiklerini getir"""
    try:
        stats = AdminService.get_statistics()
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    """Tüm kullanıcıları listele"""
    try:
        users = AdminService.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_user(user_id):
    """Kullanıcı detayı"""
    try:
        user = AdminService.get_user_by_id(user_id)
        if not user:
            return jsonify({'message': 'Kullanıcı bulunamadı'}), 404
        return jsonify(user), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_user(user_id):
    """Kullanıcı güncelle"""
    try:
        data = request.get_json()
        user, error = AdminService.update_user(user_id, data)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({
            'message': 'Kullanıcı başarıyla güncellendi',
            'user': user
        }), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(user_id):
    """Kullanıcı sil"""
    try:
        success, error = AdminService.delete_user(user_id)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({'message': 'Kullanıcı başarıyla silindi'}), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

# Yazar yönetimi
@admin_bp.route('/authors', methods=['GET'])
@jwt_required()
def get_authors():
    """Yazarları listele"""
    try:
        authors = AuthorService.get_all_authors()
        return jsonify(authors), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/authors', methods=['POST'])
@jwt_required()
@admin_required
def create_author():
    """Yeni yazar ekle"""
    try:
        data = request.get_json()
        author, error = AuthorService.create_author(data)
        
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Yazar başarıyla eklendi',
            'author': author
        }), 201
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/authors/<int:author_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_author(author_id):
    """Yazar güncelle"""
    try:
        data = request.get_json()
        author, error = AuthorService.update_author(author_id, data)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({
            'message': 'Yazar başarıyla güncellendi',
            'author': author
        }), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

# Kategori yönetimi
@admin_bp.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    """Kategorileri listele"""
    try:
        categories = CategoryService.get_all_categories()
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/categories', methods=['POST'])
@jwt_required()
@admin_required
def create_category():
    """Yeni kategori ekle"""
    try:
        data = request.get_json()
        category, error = CategoryService.create_category(data)
        
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Kategori başarıyla eklendi',
            'category': category
        }), 201
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@admin_bp.route('/categories/<int:category_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_category(category_id):
    """Kategori güncelle"""
    try:
        data = request.get_json()
        category, error = CategoryService.update_category(category_id, data)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({
            'message': 'Kategori başarıyla güncellendi',
            'category': category
        }), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500



