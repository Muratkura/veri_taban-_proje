-- Örnek veriler (Test için)

-- Kategoriler
INSERT IGNORE INTO categories (name, description) VALUES 
('Roman', 'Kurgu romanlar'),
('Tarih', 'Tarih kitapları'),
('Bilim', 'Bilim kitapları'),
('Felsefe', 'Felsefe kitapları'),
('Biyografi', 'Biyografi kitapları');

-- Yazarlar
INSERT IGNORE INTO authors (first_name, last_name, birth_date, biography) VALUES
('Orhan', 'Pamuk', '1952-06-07', 'Nobel Edebiyat Ödülü sahibi Türk yazar'),
('Elif', 'Şafak', '1971-10-25', 'Türk yazar ve akademisyen'),
('İlber', 'Ortaylı', '1947-05-21', 'Türk tarihçi ve akademisyen'),
('Ahmet', 'Ümit', '1960-09-30', 'Türk yazar ve şair'),
('Stefan', 'Zweig', '1881-11-28', 'Avusturyalı yazar');

-- Kitaplar
INSERT IGNORE INTO books (title, isbn, author_id, category_id, publication_date, publisher, total_copies, available_copies, description) VALUES
('Kafamda Bir Tuhaflık', '9789750827988', 1, 1, '2014-03-01', 'Yapı Kredi Yayınları', 5, 5, 'Orhan Pamuk''un modern İstanbul romanı'),
('Benim Adım Kırmızı', '9789750805139', 1, 1, '1998-01-01', 'İletişim Yayınları', 3, 3, '16. yüzyıl İstanbul''unda geçen bir cinayet romanı'),
('Aşk', '9789750817057', 2, 1, '2009-03-01', 'Doğan Kitap', 4, 4, 'Elif Şafak''ın en çok okunan romanlarından biri'),
('Türklerin Tarihi', '9789752430965', 3, 2, '2015-01-01', 'Timaş Yayınları', 6, 6, 'Türk tarihi üzerine kapsamlı bir çalışma'),
('Patasana', '9789750817514', 4, 1, '2000-01-01', 'Doğan Kitap', 3, 3, 'Ahmet Ümit''in polisiye romanı'),
('Satranç', '9789750807485', 5, 1, '1942-01-01', 'İletişim Yayınları', 4, 4, 'Stefan Zweig''ın ünlü novellası');

-- Not: Kullanıcılar için şifreler hash'lenmiş olmalı
-- Bu örnek veriler sadece test amaçlıdır
-- Gerçek uygulamada kullanıcılar kayıt sayfasından oluşturulmalıdır
