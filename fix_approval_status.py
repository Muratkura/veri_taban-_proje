"""
approval_status sütununu kontrol edip ekleyen script
Kullanım: python fix_approval_status.py
"""

from app import create_app, db
from sqlalchemy import text
import sys

def fix_approval_status():
    """approval_status sütununu kontrol et ve ekle"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("approval_status Sütunu Kontrol ve Düzeltme")
        print("=" * 60)
        
        try:
            # Önce sütunun var olup olmadığını kontrol et
            print("\n[1/4] Sütun kontrol ediliyor...")
            result = db.session.execute(text("""
                SELECT COUNT(*) as count 
                FROM information_schema.COLUMNS 
                WHERE TABLE_SCHEMA = DATABASE() 
                AND TABLE_NAME = 'loans' 
                AND COLUMN_NAME = 'approval_status'
            """))
            
            column_exists = result.fetchone()[0] > 0
            
            if column_exists:
                print("[OK] approval_status sutunu zaten mevcut!")
            else:
                print("[EKLENIYOR] approval_status sutunu bulunamadi, ekleniyor...")
                
                # Sütunu ekle
                db.session.execute(text("""
                    ALTER TABLE loans 
                    ADD COLUMN approval_status VARCHAR(20) DEFAULT 'pending' 
                    AFTER status
                """))
                db.session.commit()
                print("[OK] approval_status sutunu eklendi!")
            
            # Mevcut kayıtları güncelle
            print("\n[2/4] Mevcut odunc kayitlari guncelleniyor...")
            db.session.execute(text("""
                UPDATE loans 
                SET approval_status = 'approved' 
                WHERE approval_status IS NULL 
                AND status IN ('active', 'overdue', 'returned')
            """))
            db.session.commit()
            print("[OK] Mevcut kayitlar guncellendi!")
            
            # Constraint kontrolü
            print("\n[3/4] Constraint kontrol ediliyor...")
            try:
                # Constraint'i eklemeyi dene (varsa hata verir ama sorun değil)
                db.session.execute(text("""
                    ALTER TABLE loans 
                    ADD CONSTRAINT chk_approval_status 
                    CHECK (approval_status IN ('pending', 'approved', 'rejected'))
                """))
                db.session.commit()
                print("[OK] Constraint eklendi!")
            except Exception as e:
                if "Duplicate constraint" in str(e) or "already exists" in str(e).lower():
                    print("[OK] Constraint zaten mevcut!")
                else:
                    print(f"[UYARI] Constraint eklenemedi (sorun degil): {e}")
                db.session.rollback()
            
            # Trigger kontrolü
            print("\n[4/4] Trigger kontrol ediliyor...")
            try:
                # Eski trigger'ı sil
                db.session.execute(text("DROP TRIGGER IF EXISTS decrease_book_copies"))
                db.session.commit()
                
                # Yeni trigger'ı oluştur
                db.session.execute(text("""
                    CREATE TRIGGER decrease_book_copies 
                    AFTER UPDATE ON loans
                    FOR EACH ROW
                    BEGIN
                        IF NEW.approval_status = 'approved' AND OLD.approval_status = 'pending' AND NEW.status = 'active' THEN
                            UPDATE books
                            SET available_copies = available_copies - 1
                            WHERE id = NEW.book_id AND available_copies > 0;
                        END IF;
                    END
                """))
                db.session.commit()
                print("[OK] Trigger guncellendi!")
            except Exception as e:
                print(f"[UYARI] Trigger guncellenemedi (sorun degil): {e}")
                db.session.rollback()
            
            print("\n" + "=" * 60)
            print("[BAŞARILI] Tüm işlemler tamamlandı!")
            print("=" * 60)
            print("\nŞimdi yapmanız gerekenler:")
            print("1. Backend'i durdurun (Ctrl+C)")
            print("2. Backend'i yeniden başlatın: python run.py")
            print("3. Tarayıcıyı yenileyin (F5)")
            print("=" * 60)
            
        except Exception as e:
            db.session.rollback()
            print(f"\n[HATA] İşlem sırasında hata oluştu: {str(e)}")
            print("\nLütfen şunları kontrol edin:")
            print("1. MySQL'in çalıştığından emin olun")
            print("2. .env dosyasındaki DATABASE_URL'in doğru olduğundan emin olun")
            print("3. Veritabanı bağlantısını kontrol edin")
            sys.exit(1)

if __name__ == '__main__':
    fix_approval_status()

