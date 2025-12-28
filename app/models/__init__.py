"""
Models paketi
Tüm veritabanı modellerini içe aktarır ve dışa aktarır

Bu dosya, modellerin kolay import edilmesini sağlar:
    from app.models import User, Book, Loan

Modeller:
    - User: Kullanıcı modeli
    - Book: Kitap modeli
    - Author: Yazar modeli
    - Category: Kategori modeli
    - Loan: Ödünç işlemi modeli
    - Fine: Ceza modeli
"""
from app.models.user import User
from app.models.book import Book, Author, Category
from app.models.loan import Loan, Fine

# Dışa aktarılacak modelleri belirtir (from app.models import * kullanıldığında)
__all__ = ['User', 'Book', 'Author', 'Category', 'Loan', 'Fine']










