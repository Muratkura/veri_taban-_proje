# Veritabanı Migration - approval_status Ekleme

## Hata
```
Unknown column 'approval_status' in 'field list'
```

Bu hata, veritabanında `approval_status` sütununun olmadığını gösteriyor.

## Çözüm: Migration'ı Çalıştırın

### Yöntem 1: Komut Satırından (Önerilen)

1. **Terminal/CMD/PowerShell açın**

2. **MySQL'e bağlanın ve migration'ı çalıştırın:**
   ```bash
   mysql -u root -p kutuphane_db < database\migration_add_approval_status.sql
   ```
   
   Şifre isterse, MySQL root şifrenizi girin.

3. **Alternatif: Tam yol ile:**
   ```bash
   mysql -u root -p kutuphane_db < "C:\Users\hp\Desktop\veri_tabanı_proje\database\migration_add_approval_status.sql"
   ```

### Yöntem 2: MySQL Workbench ile

1. **MySQL Workbench'i açın**
2. **Local instance'a bağlanın** (root şifrenizi girin)
3. **Sol tarafta `kutuphane_db` veritabanını seçin** (çift tıklayın)
4. **File > Open SQL Script** seçin
5. **`database/migration_add_approval_status.sql` dosyasını açın**
6. **Execute (⚡) butonuna tıklayın**

### Yöntem 3: MySQL Komut Satırından Manuel

1. **MySQL'e bağlanın:**
   ```bash
   mysql -u root -p kutuphane_db
   ```

2. **Migration SQL komutlarını çalıştırın:**
   ```sql
   -- approval_status sütununu ekle
   ALTER TABLE loans 
   ADD COLUMN approval_status VARCHAR(20) DEFAULT 'pending' 
   AFTER status;
   
   -- Mevcut ödünçleri onaylı olarak işaretle
   UPDATE loans 
   SET approval_status = 'approved' 
   WHERE status IN ('active', 'overdue', 'returned');
   
   -- Constraint ekle
   ALTER TABLE loans 
   ADD CONSTRAINT chk_approval_status 
   CHECK (approval_status IN ('pending', 'approved', 'rejected'));
   
   -- Eski trigger'ı sil
   DROP TRIGGER IF EXISTS decrease_book_copies;
   
   -- Yeni trigger oluştur
   DELIMITER //
   CREATE TRIGGER decrease_book_copies 
   AFTER UPDATE ON loans
   FOR EACH ROW
   BEGIN
       IF NEW.approval_status = 'approved' AND OLD.approval_status = 'pending' AND NEW.status = 'active' THEN
           UPDATE books
           SET available_copies = available_copies - 1
           WHERE id = NEW.book_id AND available_copies > 0;
       END IF;
   END//
   DELIMITER ;
   
   EXIT;
   ```

## Migration Sonrası

1. **Backend'i yeniden başlatın** (eğer çalışıyorsa):
   - Ctrl+C ile durdurun
   - `python run.py` ile tekrar başlatın

2. **Tarayıcıyı yenileyin** (F5)

3. **Kitap ödünç alma işlemini tekrar deneyin**

## Kontrol

Migration'ın başarılı olup olmadığını kontrol etmek için:

```bash
mysql -u root -p kutuphane_db
```

```sql
-- loans tablosunun yapısını kontrol et
DESCRIBE loans;

-- approval_status sütununu görmelisiniz
EXIT;
```

