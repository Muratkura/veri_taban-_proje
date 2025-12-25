-- Kütüphane Yönetim Sistemi Veritabanı Şeması (MySQL)

-- Kategoriler tablosu
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Yazarlar tablosu
CREATE TABLE IF NOT EXISTS authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    biography TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Kitaplar tablosu
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    author_id INT,
    category_id INT,
    publication_date DATE,
    publisher VARCHAR(255),
    total_copies INT DEFAULT 1,
    available_copies INT DEFAULT 1,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE SET NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Kullanıcılar tablosu
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role ENUM('student', 'staff', 'admin') DEFAULT 'student',
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Ödünç işlemleri tablosu
CREATE TABLE IF NOT EXISTS loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    CHECK (status IN ('active', 'returned', 'overdue'))
);

-- Ceza tablosu
CREATE TABLE IF NOT EXISTS fines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT NOT NULL,
    user_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    reason VARCHAR(255) NOT NULL,
    paid BOOLEAN DEFAULT FALSE,
    paid_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (loan_id) REFERENCES loans(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Trigger: Kitap ödünç alındığında available_copies'i azalt
DELIMITER //
CREATE TRIGGER decrease_book_copies 
AFTER INSERT ON loans
FOR EACH ROW
BEGIN
    IF NEW.status = 'active' THEN
        UPDATE books
        SET available_copies = available_copies - 1
        WHERE id = NEW.book_id AND available_copies > 0;
    END IF;
END//
DELIMITER ;

-- Trigger: Kitap iade edildiğinde available_copies'i artır
DELIMITER //
CREATE TRIGGER increase_book_copies 
AFTER UPDATE ON loans
FOR EACH ROW
BEGIN
    IF NEW.status = 'returned' AND OLD.status = 'active' THEN
        UPDATE books
        SET available_copies = available_copies + 1
        WHERE id = NEW.book_id;
    END IF;
END//
DELIMITER ;

-- Trigger: Geç iade kontrolü ve ceza hesaplama
DELIMITER //
CREATE TRIGGER check_overdue_fine 
AFTER UPDATE ON loans
FOR EACH ROW
BEGIN
    DECLARE days_overdue INT;
    DECLARE fine_amount DECIMAL(10, 2);
    
    -- Eğer iade edildiyse
    IF NEW.status = 'returned' AND OLD.status = 'active' THEN
        -- Gecikme günü hesapla
        SET days_overdue = GREATEST(0, DATEDIFF(NEW.return_date, NEW.due_date));
        
        -- Eğer geç iade edildiyse ceza oluştur
        IF days_overdue > 0 THEN
            -- Günlük ceza: 5 TL
            SET fine_amount = days_overdue * 5.00;
            
            -- Ceza kaydı oluştur
            INSERT INTO fines (loan_id, user_id, amount, reason)
            VALUES (NEW.id, NEW.user_id, fine_amount, 
                    CONCAT('Geç iade cezası: ', days_overdue, ' gün gecikme'));
        END IF;
    END IF;
END//
DELIMITER ;

-- Trigger: Vadesi geçen kitapları otomatik olarak overdue yap
DELIMITER //
CREATE TRIGGER update_loans_overdue 
BEFORE UPDATE ON loans
FOR EACH ROW
BEGIN
    IF NEW.due_date < CURDATE() AND NEW.status = 'active' AND NEW.return_date IS NULL THEN
        SET NEW.status = 'overdue';
    END IF;
END//
DELIMITER ;

-- Stored Procedure: Vadesi geçen tüm kitapları kontrol et ve güncelle
DELIMITER //
CREATE PROCEDURE update_all_overdue_loans()
BEGIN
    UPDATE loans
    SET status = 'overdue'
    WHERE due_date < CURDATE() 
      AND status = 'active'
      AND return_date IS NULL;
END//
DELIMITER ;

-- Stored Procedure: Kullanıcının toplam ceza miktarını hesapla
DELIMITER //
CREATE PROCEDURE get_user_total_fine(IN p_user_id INT, OUT total_fine DECIMAL(10, 2))
BEGIN
    SELECT COALESCE(SUM(amount), 0.00)
    INTO total_fine
    FROM fines
    WHERE user_id = p_user_id AND paid = FALSE;
END//
DELIMITER ;

-- Stored Procedure: Kitap istatistiklerini getir
DELIMITER //
CREATE PROCEDURE get_book_statistics()
BEGIN
    SELECT 
        (SELECT COUNT(*) FROM books) AS total_books,
        (SELECT COUNT(*) FROM loans) AS total_loans,
        (SELECT COUNT(*) FROM loans WHERE status = 'active') AS active_loans,
        (SELECT COUNT(*) FROM loans WHERE status = 'overdue') AS overdue_loans,
        (SELECT COALESCE(SUM(amount), 0.00) FROM fines WHERE paid = FALSE) AS total_fines;
END//
DELIMITER ;

-- İndeksler
CREATE INDEX idx_books_author ON books(author_id);
CREATE INDEX idx_books_category ON books(category_id);
CREATE INDEX idx_loans_user ON loans(user_id);
CREATE INDEX idx_loans_book ON loans(book_id);
CREATE INDEX idx_loans_status ON loans(status);
CREATE INDEX idx_fines_user ON fines(user_id);
CREATE INDEX idx_fines_loan ON fines(loan_id);

-- Örnek veriler (Opsiyonel - test için)
-- INSERT INTO categories (name, description) VALUES 
-- ('Roman', 'Kurgu romanlar'),
-- ('Tarih', 'Tarih kitapları'),
-- ('Bilim', 'Bilim kitapları');

-- INSERT INTO authors (first_name, last_name) VALUES
-- ('Orhan', 'Pamuk'),
-- ('Elif', 'Şafak'),
-- ('İlber', 'Ortaylı');
