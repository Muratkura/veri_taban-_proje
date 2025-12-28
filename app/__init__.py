"""
Flask uygulamasının ana yapılandırma dosyası
Bu dosya uygulamanın başlatılması ve yapılandırılmasından sorumludur
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from app.config import Config
import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

# Veritabanı bağlantısı için SQLAlchemy instance'ı
db = SQLAlchemy()

# JWT token yönetimi için JWTManager instance'ı
jwt = JWTManager()

# E-posta gönderimi için Mail instance'ı
mail = Mail()

def create_app():
    """
    Flask uygulama factory fonksiyonu
    Uygulamayı oluşturur, yapılandırır ve döndürür
    
    Returns:
        Flask: Yapılandırılmış Flask uygulaması
    """
    # Flask uygulamasını oluştur
    app = Flask(__name__)
    
    # Yapılandırma ayarlarını yükle
    app.config.from_object(Config)
    
    # Uzantıları başlat (extensions initialization)
    # Veritabanı bağlantısını uygulamaya bağla
    db.init_app(app)
    
    # JWT token yönetimini uygulamaya bağla
    jwt.init_app(app)
    
    # E-posta servisini uygulamaya bağla
    mail.init_app(app)
    
    # CORS (Cross-Origin Resource Sharing) desteğini etkinleştir
    # Bu, farklı origin'lerden gelen isteklere izin verir
    CORS(app)
    
    # Blueprint'leri kaydet (route modüllerini uygulamaya bağla)
    from app.controllers.auth_controller import auth_bp
    from app.controllers.book_controller import book_bp
    from app.controllers.loan_controller import loan_bp
    from app.controllers.admin_controller import admin_bp
    
    # Her blueprint'i belirli bir URL prefix ile kaydet
    # Auth endpoint'leri: /api/auth/*
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    # Kitap endpoint'leri: /api/books/*
    app.register_blueprint(book_bp, url_prefix='/api/books')
    
    # Ödünç işlemi endpoint'leri: /api/loans/*
    app.register_blueprint(loan_bp, url_prefix='/api/loans')
    
    # Admin endpoint'leri: /api/admin/*
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Ana sayfa endpoint'i (API bilgisi için)
    @app.route('/')
    def index():
        """
        Ana sayfa endpoint'i
        API hakkında temel bilgi döndürür
        
        Returns:
            dict: API mesajı ve versiyon bilgisi
        """
        return {'message': 'Kütüphane Yönetim Sistemi API', 'version': '1.0'}
    
    # Veritabanı tablolarını oluştur
    # app_context içinde çalıştırılması gerekir
    with app.app_context():
        # Tüm modellerde tanımlı tabloları veritabanında oluştur
        # Eğer tablolar zaten varsa bir şey yapmaz
        db.create_all()
    
    return app

