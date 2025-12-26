-- Migration: Ödünç işlemlerine onay durumu ekleme
-- Bu dosyayı mevcut veritabanına uygulamak için çalıştırın

-- approval_status sütununu ekle
ALTER TABLE loans 
ADD COLUMN approval_status VARCHAR(20) DEFAULT 'pending' 
AFTER status;

-- Mevcut aktif ödünçleri onaylı olarak işaretle
UPDATE loans 
SET approval_status = 'approved' 
WHERE status IN ('active', 'overdue', 'returned');

-- Mevcut iade edilmiş ödünçleri onaylı olarak işaretle
UPDATE loans 
SET approval_status = 'approved' 
WHERE status = 'returned';

-- Constraint ekle
ALTER TABLE loans 
ADD CONSTRAINT chk_approval_status 
CHECK (approval_status IN ('pending', 'approved', 'rejected'));

-- Eski trigger'ı sil (eğer varsa)
DROP TRIGGER IF EXISTS decrease_book_copies;

-- Yeni trigger oluştur (sadece onaylandığında kopya azalt)
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

