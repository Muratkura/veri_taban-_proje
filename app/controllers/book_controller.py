"""
Kitap controller'ı
Kitap listeleme, arama, ekleme, güncelleme ve silme işlemleri için endpoint'ler
"""
from flask import Blueprint, request, jsonify
from app.services.book_service import BookService, CategoryService
from flask_jwt_extended import jwt_required
from app.utils.decorators import admin_required

# Book blueprint'i: /api/books/* endpoint'leri için
book_bp = Blueprint('books', __name__)

@book_bp.route('', methods=['GET'])
def get_all_books():
    """
    Tüm kitapları listele
    Query parametreleri:
        - q: Arama terimi (başlık, ISBN, yayınevi)
        - category_id: Kategoriye göre filtreleme
    """
    try:
        # Kategori filtresi varsa kategoriye göre filtrele
        category_id = request.args.get('category_id')
        if category_id:
            try:
                category_id = int(category_id)
                books = BookService.get_books_by_category(category_id)
            except ValueError:
                return jsonify({'message': 'Geçersiz kategori ID'}), 400
        # Arama parametresi varsa ara
        elif request.args.get('q'):
            query = request.args.get('q')
            books = BookService.search_books(query)
        else:
            # Tüm kitapları getir
            books = BookService.get_all_books()
        
        return jsonify(books), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('/available', methods=['GET'])
def get_available_books():
    """Müsait kitapları listele"""
    try:
        books = BookService.get_available_books()
        return jsonify(books), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Kitap detayı"""
    try:
        book = BookService.get_book_by_id(book_id)
        if not book:
            return jsonify({'message': 'Kitap bulunamadı'}), 404
        
        return jsonify(book), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_book():
    """Yeni kitap ekle (Admin)"""
    try:
        data = request.get_json()
        book, error = BookService.create_book(data)
        
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Kitap başarıyla eklendi',
            'book': book
        }), 201
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('/<int:book_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_book(book_id):
    """Kitap güncelle (Admin)"""
    try:
        data = request.get_json()
        book, error = BookService.update_book(book_id, data)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({
            'message': 'Kitap başarıyla güncellendi',
            'book': book
        }), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('/<int:book_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_book(book_id):
    """Kitap sil (Admin)"""
    try:
        success, error = BookService.delete_book(book_id)
        
        if error:
            return jsonify({'message': error}), 404
        
        return jsonify({'message': 'Kitap başarıyla silindi'}), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@book_bp.route('/categories', methods=['GET'])
def get_categories():
    """Tüm kategorileri listele (Herkes erişebilir)"""
    try:
        categories = CategoryService.get_all_categories()
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500










