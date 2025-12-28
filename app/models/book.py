"""
Kitap (Book), Yazar (Author) ve Kategori (Category) modelleri
Kütüphane sistemindeki kitapları ve ilgili verileri temsil eder
"""
from app import db
from datetime import datetime

class Category(db.Model):
    """
    Kategori modeli
    Kitapların kategorilerini temsil eder (örn: Roman, Tarih, Bilim)
    """
    __tablename__ = 'categories'
    
    # Birincil anahtar: Benzersiz kategori kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Kategori adı: Benzersiz, boş olamaz
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    # Kategori açıklaması: Opsiyonel
    description = db.Column(db.Text)
    
    # Oluşturulma tarihi: Otomatik olarak eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # İlişkiler (Relationships)
    # Bu kategoriye ait kitaplar
    books = db.relationship('Book', backref='category', lazy=True)
    
    def to_dict(self):
        """
        Kategori modelini dictionary formatına çevirir
        
        Returns:
            dict: Kategori bilgilerini içeren dictionary
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        """
        Kategori nesnesinin string temsilini döndürür
        
        Returns:
            str: Kategori adını içeren string
        """
        return f'<Category {self.name}>'


class Author(db.Model):
    """
    Yazar modeli
    Kitapların yazarlarını temsil eder
    """
    __tablename__ = 'authors'
    
    # Birincil anahtar: Benzersiz yazar kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Yazarın adı: Zorunlu alan
    first_name = db.Column(db.String(100), nullable=False)
    
    # Yazarın soyadı: Zorunlu alan
    last_name = db.Column(db.String(100), nullable=False)
    
    # Doğum tarihi: Opsiyonel
    birth_date = db.Column(db.Date)
    
    # Yazar biyografisi: Opsiyonel
    biography = db.Column(db.Text)
    
    # Oluşturulma tarihi: Otomatik olarak eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # İlişkiler (Relationships)
    # Bu yazara ait kitaplar
    books = db.relationship('Book', backref='author', lazy=True)
    
    @property
    def full_name(self):
        """
        Yazarın tam adını döndürür (ad + soyad)
        
        Returns:
            str: Yazarın tam adı
        """
        return f"{self.first_name} {self.last_name}"
    
    def to_dict(self):
        """
        Yazar modelini dictionary formatına çevirir
        
        Returns:
            dict: Yazar bilgilerini içeren dictionary
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'birth_date': self.birth_date.isoformat() if self.birth_date else None,
            'biography': self.biography,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        """
        Yazar nesnesinin string temsilini döndürür
        
        Returns:
            str: Yazarın tam adını içeren string
        """
        return f'<Author {self.full_name}>'


class Book(db.Model):
    """
    Kitap modeli
    Kütüphanedeki kitapları temsil eder
    """
    __tablename__ = 'books'
    
    # Birincil anahtar: Benzersiz kitap kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Kitap başlığı: Zorunlu, arama için index'li
    title = db.Column(db.String(255), nullable=False, index=True)
    
    # ISBN numarası: Benzersiz, arama için index'li
    isbn = db.Column(db.String(20), unique=True, index=True)
    
    # Yazar ID'si: Yazar silinirse NULL olur (Foreign Key)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id', ondelete='SET NULL'))
    
    # Kategori ID'si: Kategori silinirse NULL olur (Foreign Key)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='SET NULL'))
    
    # Yayın tarihi: Opsiyonel
    publication_date = db.Column(db.Date)
    
    # Yayınevi: Opsiyonel
    publisher = db.Column(db.String(255))
    
    # Toplam kopya sayısı: Varsayılan 1
    total_copies = db.Column(db.Integer, default=1)
    
    # Müsait kopya sayısı: Varsayılan 1
    available_copies = db.Column(db.Integer, default=1)
    
    # Kitap açıklaması: Opsiyonel
    description = db.Column(db.Text)
    
    # Oluşturulma tarihi: Otomatik olarak eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Güncelleme tarihi: Her güncellemede otomatik olarak güncellenir
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # İlişkiler (Relationships)
    # Bu kitaba ait ödünç işlemleri
    loans = db.relationship('Loan', backref='book', lazy=True)
    
    @property
    def is_available(self):
        """
        Kitabın ödünç alınabilir durumda olup olmadığını kontrol eder
        
        Returns:
            bool: Müsait kopya varsa True, yoksa False
        """
        return self.available_copies > 0
    
    def to_dict(self, include_details=False):
        """
        Kitap modelini dictionary formatına çevirir
        
        Args:
            include_details (bool): Detaylı bilgileri (açıklama) dahil etmek için True
        
        Returns:
            dict: Kitap bilgilerini içeren dictionary
        """
        data = {
            'id': self.id,
            'title': self.title,
            'isbn': self.isbn,
            # Yazar bilgisi varsa dictionary formatında ekle
            'author': self.author.to_dict() if self.author else None,
            # Kategori bilgisi varsa dictionary formatında ekle
            'category': self.category.to_dict() if self.category else None,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'publisher': self.publisher,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'is_available': self.is_available,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        
        # Detaylı bilgi isteniyorsa açıklama ekle
        if include_details:
            data['description'] = self.description
        
        return data
    
    def __repr__(self):
        """
        Kitap nesnesinin string temsilini döndürür
        
        Returns:
            str: Kitap başlığını içeren string
        """
        return f'<Book {self.title}>'










