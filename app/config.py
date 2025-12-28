"""
Uygulama yapılandırma ayarları
Ortam değişkenlerinden veya varsayılan değerlerden yapılandırma bilgilerini okur
"""
import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

class Config:
    """
    Flask uygulaması için yapılandırma sınıfı
    Tüm ayarlar burada tanımlanır
    """
    
    # Veritabanı yapılandırması
    # MySQL veritabanı bağlantı string'i
    # Format: mysql+pymysql://kullanici:şifre@host:port/veritabani_adi
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:Murat123.@localhost:3306/kutuphane_db')
    
    # SQLAlchemy modifikasyon takibini kapat (performans için)
    # Her değişiklikte uyarı vermez
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT (JSON Web Token) yapılandırması
    # Token'ları imzalamak için kullanılan gizli anahtar
    # ÖNEMLİ: Production'da mutlaka değiştirilmelidir!
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key-change-in-production')
    
    # Token süresinin otomatik olarak dolmasını kapat
    # Süre yönetimi manuel olarak yapılıyor
    JWT_ACCESS_TOKEN_EXPIRES = False  # Token expiration handled manually
    
    # E-posta (Mail) yapılandırması
    # SMTP sunucu adresi (varsayılan: Gmail)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    
    # SMTP sunucu portu (varsayılan: 587 - TLS için)
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    
    # TLS (Transport Layer Security) kullanımı
    # Güvenli bağlantı için True olmalı
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    
    # E-posta gönderen kullanıcı adı
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    
    # E-posta gönderen kullanıcı şifresi
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    
    # Flask uygulama gizli anahtarı
    # Session ve cookie şifreleme için kullanılır
    SECRET_KEY = os.getenv('SECRET_KEY', 'flask-secret-key')


