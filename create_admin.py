"""
Admin kullanıcı oluşturmak için script
Kullanım: python create_admin.py
"""

from app import create_app, db
from app.models.user import User
import sys

def create_admin():
    """Admin kullanıcı oluştur"""
    app = create_app()
    
    with app.app_context():
        print("=" * 50)
        print("Admin Kullanıcı Oluşturma")
        print("=" * 50)
        
        # Mevcut admin kullanıcıları kontrol et
        existing_admin = User.query.filter_by(role='admin').first()
        if existing_admin:
            print(f"\n[UYARI] Zaten bir admin kullanıcı var: {existing_admin.username}")
            response = input("Yeni admin kullanıcı oluşturmak istiyor musunuz? (e/h): ")
            if response.lower() != 'e':
                print("İşlem iptal edildi.")
                return
        
        # Kullanıcı bilgilerini al
        print("\nAdmin kullanıcı bilgilerini girin:")
        username = input("Kullanıcı Adı: ").strip()
        
        if not username:
            print("[HATA] Kullanıcı adı boş olamaz!")
            sys.exit(1)
        
        # Kullanıcı adı kontrolü
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"[HATA] '{username}' kullanıcı adı zaten kullanılıyor!")
            sys.exit(1)
        
        email = input("E-posta: ").strip()
        if not email:
            print("[HATA] E-posta boş olamaz!")
            sys.exit(1)
        
        # E-posta kontrolü
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            print(f"[HATA] '{email}' e-posta adresi zaten kayıtlı!")
            sys.exit(1)
        
        first_name = input("Ad: ").strip() or "Admin"
        last_name = input("Soyad: ").strip() or "User"
        
        password = input("Şifre: ").strip()
        if not password:
            print("[HATA] Şifre boş olamaz!")
            sys.exit(1)
        
        confirm_password = input("Şifre (Tekrar): ").strip()
        if password != confirm_password:
            print("[HATA] Şifreler eşleşmiyor!")
            sys.exit(1)
        
        # Admin kullanıcı oluştur
        try:
            admin = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role='admin'
            )
            admin.set_password(password)
            
            db.session.add(admin)
            db.session.commit()
            
            print("\n" + "=" * 50)
            print("[BAŞARILI] Admin kullanıcı oluşturuldu!")
            print("=" * 50)
            print(f"Kullanıcı Adı: {username}")
            print(f"E-posta: {email}")
            print(f"Ad Soyad: {first_name} {last_name}")
            print(f"Rol: admin")
            print("\nArtık bu bilgilerle giriş yapabilirsiniz!")
            print("=" * 50)
            
        except Exception as e:
            db.session.rollback()
            print(f"\n[HATA] Admin kullanıcı oluşturulurken hata oluştu: {str(e)}")
            sys.exit(1)

if __name__ == '__main__':
    create_admin()

