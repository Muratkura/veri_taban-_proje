"""
Admin kullanıcı oluşturmak için script

Bu script, kütüphane yönetim sistemine admin kullanıcı eklemek için kullanılır.
İnteraktif olarak kullanıcı bilgilerini alır ve admin rolüyle kaydeder.

Kullanım:
    python create_admin.py

Not: Eğer sistemde zaten bir admin varsa, yeni admin eklemek için onay ister.
"""

from app import create_app, db
from app.models.user import User
import sys

def create_admin():
    """
    Admin kullanıcı oluşturma fonksiyonu
    Kullanıcıdan bilgileri alır, doğrular ve admin olarak kaydeder
    """
    # Flask uygulamasını oluştur
    app = create_app()
    
    # Uygulama context'i içinde çalış
    with app.app_context():
        # Başlık yazdır
        print("=" * 50)
        print("Admin Kullanıcı Oluşturma")
        print("=" * 50)
        
        # Mevcut admin kullanıcıları kontrol et
        existing_admin = User.query.filter_by(role='admin').first()
        if existing_admin:
            # Eğer zaten admin varsa uyar ve onay iste
            print(f"\n[UYARI] Zaten bir admin kullanıcı var: {existing_admin.username}")
            response = input("Yeni admin kullanıcı oluşturmak istiyor musunuz? (e/h): ")
            if response.lower() != 'e':
                print("İşlem iptal edildi.")
                return
        
        # Kullanıcı bilgilerini al
        print("\nAdmin kullanıcı bilgilerini girin:")
        
        # Kullanıcı adı al ve doğrula
        username = input("Kullanıcı Adı: ").strip()
        
        if not username:
            print("[HATA] Kullanıcı adı boş olamaz!")
            sys.exit(1)
        
        # Kullanıcı adı kontrolü: Aynı kullanıcı adı zaten var mı?
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"[HATA] '{username}' kullanıcı adı zaten kullanılıyor!")
            sys.exit(1)
        
        # E-posta al ve doğrula
        email = input("E-posta: ").strip()
        if not email:
            print("[HATA] E-posta boş olamaz!")
            sys.exit(1)
        
        # E-posta kontrolü: Aynı e-posta zaten kayıtlı mı?
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            print(f"[HATA] '{email}' e-posta adresi zaten kayıtlı!")
            sys.exit(1)
        
        # Ad ve soyad al (opsiyonel, varsayılan değerler var)
        first_name = input("Ad: ").strip() or "Admin"
        last_name = input("Soyad: ").strip() or "User"
        
        # Şifre al ve doğrula
        password = input("Şifre: ").strip()
        if not password:
            print("[HATA] Şifre boş olamaz!")
            sys.exit(1)
        
        # Şifre tekrarını al ve eşleşme kontrolü yap
        confirm_password = input("Şifre (Tekrar): ").strip()
        if password != confirm_password:
            print("[HATA] Şifreler eşleşmiyor!")
            sys.exit(1)
        
        # Admin kullanıcı oluştur
        try:
            # Yeni admin kullanıcı nesnesi oluştur
            admin = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                role='admin'  # Rolü admin olarak ayarla
            )
            
            # Şifreyi hash'leyerek kaydet
            admin.set_password(password)
            
            # Veritabanına ekle ve kaydet
            db.session.add(admin)
            db.session.commit()
            
            # Başarı mesajı göster
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
            # Hata durumunda değişiklikleri geri al
            db.session.rollback()
            print(f"\n[HATA] Admin kullanıcı oluşturulurken hata oluştu: {str(e)}")
            sys.exit(1)

# Script doğrudan çalıştırılırsa fonksiyonu çağır
if __name__ == '__main__':
    create_admin()

