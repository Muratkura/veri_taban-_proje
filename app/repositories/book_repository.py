from app import db
from app.models.book import Book, Author, Category

class BookRepository:
    @staticmethod
    def find_by_id(book_id):
        """ID ile kitap bul"""
        return Book.query.get(book_id)
    
    @staticmethod
    def get_all():
        """Tüm kitapları getir"""
        return Book.query.all()
    
    @staticmethod
    def search(query):
        """Kitap ara (başlık, yazar, ISBN)"""
        search_term = f"%{query}%"
        return Book.query.filter(
            db.or_(
                Book.title.ilike(search_term),
                Book.isbn.ilike(search_term),
                Book.publisher.ilike(search_term)
            )
        ).all()
    
    @staticmethod
    def get_available_books():
        """Müsait kitapları getir"""
        return Book.query.filter(Book.available_copies > 0).all()
    
    @staticmethod
    def create(book_data):
        """Yeni kitap oluştur"""
        book = Book(
            title=book_data['title'],
            isbn=book_data.get('isbn'),
            author_id=book_data.get('author_id'),
            category_id=book_data.get('category_id'),
            publication_date=book_data.get('publication_date'),
            publisher=book_data.get('publisher'),
            total_copies=book_data.get('total_copies', 1),
            available_copies=book_data.get('available_copies', book_data.get('total_copies', 1)),
            description=book_data.get('description')
        )
        
        db.session.add(book)
        db.session.commit()
        return book
    
    @staticmethod
    def update(book_id, book_data):
        """Kitap bilgilerini güncelle"""
        book = BookRepository.find_by_id(book_id)
        if not book:
            return None
        
        if 'title' in book_data:
            book.title = book_data['title']
        if 'isbn' in book_data:
            book.isbn = book_data['isbn']
        if 'author_id' in book_data:
            book.author_id = book_data['author_id']
        if 'category_id' in book_data:
            book.category_id = book_data['category_id']
        if 'publication_date' in book_data:
            book.publication_date = book_data['publication_date']
        if 'publisher' in book_data:
            book.publisher = book_data['publisher']
        if 'total_copies' in book_data:
            # Toplam kopya değiştiğinde müsait kopyayı da güncelle
            diff = book_data['total_copies'] - book.total_copies
            book.total_copies = book_data['total_copies']
            book.available_copies = max(0, book.available_copies + diff)
        if 'description' in book_data:
            book.description = book_data['description']
        
        db.session.commit()
        return book
    
    @staticmethod
    def delete(book_id):
        """Kitabı sil"""
        book = BookRepository.find_by_id(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return True
        return False


class AuthorRepository:
    @staticmethod
    def find_by_id(author_id):
        """ID ile yazar bul"""
        return Author.query.get(author_id)
    
    @staticmethod
    def get_all():
        """Tüm yazarları getir"""
        return Author.query.all()
    
    @staticmethod
    def create(author_data):
        """Yeni yazar oluştur"""
        author = Author(
            first_name=author_data['first_name'],
            last_name=author_data['last_name'],
            birth_date=author_data.get('birth_date'),
            biography=author_data.get('biography')
        )
        
        db.session.add(author)
        db.session.commit()
        return author
    
    @staticmethod
    def update(author_id, author_data):
        """Yazar bilgilerini güncelle"""
        author = AuthorRepository.find_by_id(author_id)
        if not author:
            return None
        
        if 'first_name' in author_data:
            author.first_name = author_data['first_name']
        if 'last_name' in author_data:
            author.last_name = author_data['last_name']
        if 'birth_date' in author_data:
            author.birth_date = author_data['birth_date']
        if 'biography' in author_data:
            author.biography = author_data['biography']
        
        db.session.commit()
        return author


class CategoryRepository:
    @staticmethod
    def find_by_id(category_id):
        """ID ile kategori bul"""
        return Category.query.get(category_id)
    
    @staticmethod
    def get_all():
        """Tüm kategorileri getir"""
        return Category.query.all()
    
    @staticmethod
    def create(category_data):
        """Yeni kategori oluştur"""
        category = Category(
            name=category_data['name'],
            description=category_data.get('description')
        )
        
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def update(category_id, category_data):
        """Kategori bilgilerini güncelle"""
        category = CategoryRepository.find_by_id(category_id)
        if not category:
            return None
        
        if 'name' in category_data:
            category.name = category_data['name']
        if 'description' in category_data:
            category.description = category_data['description']
        
        db.session.commit()
        return category










