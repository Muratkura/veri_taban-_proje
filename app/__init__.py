from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from app.config import Config
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    CORS(app)
    
    # Register blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.book_controller import book_bp
    from app.controllers.loan_controller import loan_bp
    from app.controllers.admin_controller import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(book_bp, url_prefix='/api/books')
    app.register_blueprint(loan_bp, url_prefix='/api/loans')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # CORS için root endpoint
    @app.route('/')
    def index():
        return {'message': 'Kütüphane Yönetim Sistemi API', 'version': '1.0'}
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

