"""
Kullanıcı (User) modeli
Sistemdeki kullanıcıları temsil eder
"""
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    """
    Kullanıcı modeli
    Kütüphane sistemindeki tüm kullanıcıları (öğrenci, personel, admin) temsil eder
    """
    __tablename__ = 'users'
    
    # Birincil anahtar: Benzersiz kullanıcı kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Kullanıcı adı: Benzersiz, boş olamaz, arama için index'li
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    
    # E-posta adresi: Benzersiz, boş olamaz, arama için index'li
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    
    # Şifre hash'i: Şifre düz metin olarak saklanmaz, hash'lenir
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Kullanıcının adı: Zorunlu alan
    first_name = db.Column(db.String(100), nullable=False)
    
    # Kullanıcının soyadı: Zorunlu alan
    last_name = db.Column(db.String(100), nullable=False)
    
    # Kullanıcı rolü: student, staff, admin (varsayılan: student)
    role = db.Column(db.String(20), nullable=False, default='student')
    
    # Telefon numarası: Opsiyonel
    phone = db.Column(db.String(20))
    
    # Adres bilgisi: Opsiyonel, uzun metin olabilir
    address = db.Column(db.Text)
    
    # Kayıt tarihi: Otomatik olarak oluşturulma zamanı eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Güncelleme tarihi: Her güncellemede otomatik olarak güncellenir
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # İlişkiler (Relationships)
    # Kullanıcının ödünç işlemleri: Kullanıcı silinirse ödünçler de silinir
    loans = db.relationship('Loan', backref='user', lazy=True, cascade='all, delete-orphan')
    
    # Kullanıcının cezaları: Kullanıcı silinirse cezalar da silinir
    fines = db.relationship('Fine', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """
        Kullanıcı şifresini hash'ler ve kaydeder
        Güvenlik için şifre düz metin olarak saklanmaz
        
        Args:
            password (str): Hash'lenecek şifre
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """
        Verilen şifrenin doğru olup olmadığını kontrol eder
        Hash'lenmiş şifre ile karşılaştırma yapar
        
        Args:
            password (str): Kontrol edilecek şifre
            
        Returns:
            bool: Şifre doğru ise True, değilse False
        """
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """
        Kullanıcının admin rolünde olup olmadığını kontrol eder
        
        Returns:
            bool: Admin ise True, değilse False
        """
        return self.role == 'admin'
    
    def to_dict(self):
        """
        Kullanıcı modelini dictionary formatına çevirir
        API response'ları için kullanılır
        
        Returns:
            dict: Kullanıcı bilgilerini içeren dictionary
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'phone': self.phone,
            'address': self.address,
            # Tarih bilgilerini ISO formatında string olarak döndür
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        """
        Kullanıcı nesnesinin string temsilini döndürür
        Debug ve logging için kullanışlıdır
        
        Returns:
            str: Kullanıcı adını içeren string
        """
        return f'<User {self.username}>'










