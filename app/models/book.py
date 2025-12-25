from app import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # İlişkiler
    books = db.relationship('Book', backref='category', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        return f'<Category {self.name}>'


class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    biography = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # İlişkiler
    books = db.relationship('Book', backref='author', lazy=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def to_dict(self):
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
        return f'<Author {self.full_name}>'


class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    isbn = db.Column(db.String(20), unique=True, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id', ondelete='SET NULL'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='SET NULL'))
    publication_date = db.Column(db.Date)
    publisher = db.Column(db.String(255))
    total_copies = db.Column(db.Integer, default=1)
    available_copies = db.Column(db.Integer, default=1)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # İlişkiler
    loans = db.relationship('Loan', backref='book', lazy=True)
    
    @property
    def is_available(self):
        """Kitap ödünç alınabilir mi?"""
        return self.available_copies > 0
    
    def to_dict(self, include_details=False):
        """Model'i dictionary'ye çevir"""
        data = {
            'id': self.id,
            'title': self.title,
            'isbn': self.isbn,
            'author': self.author.to_dict() if self.author else None,
            'category': self.category.to_dict() if self.category else None,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'publisher': self.publisher,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'is_available': self.is_available,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        
        if include_details:
            data['description'] = self.description
        
        return data
    
    def __repr__(self):
        return f'<Book {self.title}>'



