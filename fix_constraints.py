"""
Eski CHECK constraint'lerini düzelten script
Kullanım: python fix_constraints.py
"""

from app import create_app, db
from sqlalchemy import text
import sys

def fix_constraints():
    """Eski constraint'leri sil ve yenilerini ekle"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("CHECK Constraint'leri Duzeltme")
        print("=" * 60)
        
        try:
            # Eski constraint'leri bul ve sil
            print("\n[1/3] Eski constraint'ler kontrol ediliyor...")
            
            # MySQL'de constraint isimlerini bul
            result = db.session.execute(text("""
                SELECT CONSTRAINT_NAME 
                FROM information_schema.TABLE_CONSTRAINTS 
                WHERE TABLE_SCHEMA = DATABASE() 
                AND TABLE_NAME = 'loans' 
                AND CONSTRAINT_TYPE = 'CHECK'
            """))
            
            constraints = [row[0] for row in result.fetchall()]
            print(f"Bulunan constraint'ler: {constraints}")
            
            # Eski constraint'leri sil
            for constraint_name in constraints:
                try:
                    db.session.execute(text(f"ALTER TABLE loans DROP CHECK {constraint_name}"))
                    db.session.commit()
                    print(f"[OK] Eski constraint silindi: {constraint_name}")
                except Exception as e:
                    print(f"[UYARI] Constraint silinemedi (sorun degil): {e}")
                    db.session.rollback()
            
            # Yeni constraint'leri ekle
            print("\n[2/3] Yeni constraint'ler ekleniyor...")
            
            try:
                # Status constraint
                db.session.execute(text("""
                    ALTER TABLE loans 
                    ADD CONSTRAINT chk_loans_status 
                    CHECK (status IN ('pending', 'active', 'returned', 'overdue'))
                """))
                db.session.commit()
                print("[OK] Status constraint eklendi!")
            except Exception as e:
                if "Duplicate" in str(e) or "already exists" in str(e).lower():
                    print("[OK] Status constraint zaten mevcut!")
                else:
                    print(f"[UYARI] Status constraint eklenemedi: {e}")
                db.session.rollback()
            
            try:
                # Approval status constraint
                db.session.execute(text("""
                    ALTER TABLE loans 
                    ADD CONSTRAINT chk_approval_status 
                    CHECK (approval_status IN ('pending', 'approved', 'rejected'))
                """))
                db.session.commit()
                print("[OK] Approval status constraint eklendi!")
            except Exception as e:
                if "Duplicate" in str(e) or "already exists" in str(e).lower():
                    print("[OK] Approval status constraint zaten mevcut!")
                else:
                    print(f"[UYARI] Approval status constraint eklenemedi: {e}")
                db.session.rollback()
            
            # Kontrol
            print("\n[3/3] Constraint'ler kontrol ediliyor...")
            result = db.session.execute(text("""
                SELECT CONSTRAINT_NAME, CHECK_CLAUSE
                FROM information_schema.CHECK_CONSTRAINTS 
                WHERE TABLE_SCHEMA = DATABASE() 
                AND TABLE_NAME = 'loans'
            """))
            
            constraints = result.fetchall()
            print(f"\nMevcut constraint'ler:")
            for name, clause in constraints:
                print(f"  - {name}: {clause}")
            
            print("\n" + "=" * 60)
            print("[BASARILI] Tum islemler tamamlandi!")
            print("=" * 60)
            print("\nSimdi yapmaniz gerekenler:")
            print("1. Backend'i durdurun (Ctrl+C)")
            print("2. Backend'i yeniden baslatin: python run.py")
            print("3. Tarayiciyi yenileyin (F5)")
            print("=" * 60)
            
        except Exception as e:
            db.session.rollback()
            print(f"\n[HATA] Islem sirasinda hata olustu: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    fix_constraints()

