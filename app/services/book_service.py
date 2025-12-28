"""
Kitap, Yazar ve Kategori servisleri
Kitap yönetimi işlemlerini yönetir
"""
from app.repositories.book_repository import BookRepository, AuthorRepository, CategoryRepository

class BookService:
    """
    Kitap işlemleri için servis sınıfı
    Kitap CRUD işlemlerini ve arama işlemlerini yönetir
    """
    @staticmethod
    def get_all_books():
        """Tüm kitapları getir"""
        books = BookRepository.get_all()
        return [book.to_dict() for book in books]
    
    @staticmethod
    def get_book_by_id(book_id):
        """ID ile kitap getir"""
        book = BookRepository.find_by_id(book_id)
        if not book:
            return None
        return book.to_dict(include_details=True)
    
    @staticmethod
    def search_books(query):
        """Kitap ara"""
        books = BookRepository.search(query)
        return [book.to_dict() for book in books]
    
    @staticmethod
    def get_available_books():
        """Müsait kitapları getir"""
        books = BookRepository.get_available_books()
        return [book.to_dict() for book in books]
    
    @staticmethod
    def get_books_by_category(category_id):
        """
        Belirli bir kategoriye ait kitapları getirir
        
        Args:
            category_id (int): Kategori ID'si
        
        Returns:
            list: Kategoriye ait kitap dictionary'leri
        """
        books = BookRepository.get_by_category(category_id)
        return [book.to_dict() for book in books]
    
    @staticmethod
    def create_book(book_data):
        """Yeni kitap oluştur"""
        # Gerekli alanları kontrol et
        if 'title' not in book_data:
            return None, "Kitap başlığı zorunludur"
        
        book = BookRepository.create(book_data)
        return book.to_dict(), None
    
    @staticmethod
    def update_book(book_id, book_data):
        """Kitap güncelle"""
        book = BookRepository.update(book_id, book_data)
        if not book:
            return None, "Kitap bulunamadı"
        return book.to_dict(), None
    
    @staticmethod
    def delete_book(book_id):
        """Kitap sil"""
        success = BookRepository.delete(book_id)
        if not success:
            return False, "Kitap bulunamadı"
        return True, None


class AuthorService:
    @staticmethod
    def get_all_authors():
        """Tüm yazarları getir"""
        authors = AuthorRepository.get_all()
        return [author.to_dict() for author in authors]
    
    @staticmethod
    def get_author_by_id(author_id):
        """ID ile yazar getir"""
        author = AuthorRepository.find_by_id(author_id)
        if not author:
            return None
        return author.to_dict()
    
    @staticmethod
    def create_author(author_data):
        """Yeni yazar oluştur"""
        if 'first_name' not in author_data or 'last_name' not in author_data:
            return None, "Yazar adı ve soyadı zorunludur"
        
        author = AuthorRepository.create(author_data)
        return author.to_dict(), None
    
    @staticmethod
    def update_author(author_id, author_data):
        """Yazar güncelle"""
        author = AuthorRepository.update(author_id, author_data)
        if not author:
            return None, "Yazar bulunamadı"
        return author.to_dict(), None


class CategoryService:
    @staticmethod
    def get_all_categories():
        """Tüm kategorileri getir"""
        categories = CategoryRepository.get_all()
        return [category.to_dict() for category in categories]
    
    @staticmethod
    def get_category_by_id(category_id):
        """ID ile kategori getir"""
        category = CategoryRepository.find_by_id(category_id)
        if not category:
            return None
        return category.to_dict()
    
    @staticmethod
    def create_category(category_data):
        """Yeni kategori oluştur"""
        if 'name' not in category_data:
            return None, "Kategori adı zorunludur"
        
        category = CategoryRepository.create(category_data)
        return category.to_dict(), None
    
    @staticmethod
    def update_category(category_id, category_data):
        """Kategori güncelle"""
        category = CategoryRepository.update(category_id, category_data)
        if not category:
            return None, "Kategori bulunamadı"
        return category.to_dict(), None










