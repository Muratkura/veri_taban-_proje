-- Örnek veriler (Test için)
-- Bu dosya veritabanını doldurmak için kapsamlı örnek veriler içerir

-- Kategoriler
INSERT IGNORE INTO categories (name, description) VALUES 
('Roman', 'Kurgu romanlar ve edebiyat eserleri'),
('Tarih', 'Tarih kitapları ve araştırmaları'),
('Bilim', 'Bilim kitapları ve popüler bilim'),
('Felsefe', 'Felsefe kitapları ve düşünce eserleri'),
('Biyografi', 'Biyografi ve otobiyografi kitapları'),
('Polisiye', 'Polisiye ve gerilim romanları'),
('Fantastik', 'Fantastik ve bilim kurgu kitapları'),
('Şiir', 'Şiir kitapları ve antolojiler'),
('Çocuk', 'Çocuk kitapları ve gençlik edebiyatı'),
('Psikoloji', 'Psikoloji kitapları ve kişisel gelişim'),
('Ekonomi', 'Ekonomi ve iş dünyası kitapları'),
('Sanat', 'Sanat tarihi ve sanat kitapları'),
('Edebiyat', 'Edebiyat eleştirisi ve inceleme'),
('Gezi', 'Gezi ve seyahat kitapları'),
('Mizah', 'Mizah ve komedi kitapları');

-- Yazarlar
INSERT IGNORE INTO authors (first_name, last_name, birth_date, biography) VALUES
-- Türk Yazarlar
('Orhan', 'Pamuk', '1952-06-07', 'Nobel Edebiyat Ödülü sahibi Türk yazar. Modern Türk edebiyatının önemli isimlerinden.'),
('Elif', 'Şafak', '1971-10-25', 'Türk yazar ve akademisyen. Çok sayıda ödüllü romanı bulunmaktadır.'),
('İlber', 'Ortaylı', '1947-05-21', 'Türk tarihçi ve akademisyen. Osmanlı tarihi uzmanı.'),
('Ahmet', 'Ümit', '1960-09-30', 'Türk yazar ve şair. Polisiye romanlarıyla tanınır.'),
('Yaşar', 'Kemal', '1923-10-06', 'Türk yazar ve şair. Çukurova bölgesini anlatan eserleriyle ünlü.'),
('Nazım', 'Hikmet', '1902-01-15', 'Türk şair, oyun yazarı ve romancı. Modern Türk şiirinin öncüsü.'),
('Reşat', 'Nuri Güntekin', '1889-11-25', 'Türk yazar. Çalıkuşu romanıyla tanınır.'),
('Halide', 'Edib Adıvar', '1884-06-11', 'Türk yazar ve siyasetçi. Milli Mücadele dönemi yazarlarından.'),
('Sabahattin', 'Ali', '1907-02-25', 'Türk yazar ve şair. Kürk Mantolu Madonna eseriyle ünlü.'),
('Oğuz', 'Atay', '1934-10-12', 'Türk yazar. Tutunamayanlar romanıyla tanınır.'),
('Peyami', 'Safa', '1899-04-02', 'Türk yazar ve gazeteci. Dokuzuncu Hariciye Koğuşu ile ünlü.'),
('Cemal', 'Süreya', '1931-08-01', 'Türk şair. İkinci Yeni akımının önemli temsilcilerinden.'),
('Turgut', 'Ozakman', '1930-09-01', 'Türk yazar ve tiyatro eleştirmeni. Şu Çılgın Türkler ile ünlü.'),
('Ayşe', 'Kulin', '1941-08-26', 'Türk yazar ve gazeteci. Biyografik romanlarıyla tanınır.'),
('Zülfü', 'Livaneli', '1946-06-20', 'Türk müzisyen, yazar ve siyasetçi. Serenad romanıyla ünlü.'),
('İhsan', 'Oktay Anar', '1960-03-11', 'Türk yazar. Fantastik ve tarihi romanlarıyla tanınır.'),
('Murat', 'Menteş', '1974-01-01', 'Türk yazar. Modern Türk edebiyatının önemli isimlerinden.'),
('Buket', 'Uzuner', '1955-10-03', 'Türk yazar. Çevre ve doğa temalı eserleriyle tanınır.'),
('Hakan', 'Günday', '1976-05-29', 'Türk yazar. Sert ve gerçekçi romanlarıyla tanınır.'),
('Sait', 'Faik Abasıyanık', '1906-11-18', 'Türk öykü yazarı. Modern Türk öykücülüğünün öncüsü.'),
-- Yabancı Yazarlar
('Stefan', 'Zweig', '1881-11-28', 'Avusturyalı yazar. Biyografi ve novella türünde eserler vermiştir.'),
('Franz', 'Kafka', '1883-07-03', 'Çek-Alman yazar. Dönüşüm ve Dava eserleriyle ünlü.'),
('Gabriel', 'García Márquez', '1927-03-06', 'Kolombiyalı yazar. Yüzyıllık Yalnızlık ile Nobel ödülü almıştır.'),
('Milan', 'Kundera', '1929-04-01', 'Çek-Fransız yazar. Varolmanın Dayanılmaz Hafifliği ile ünlü.'),
('Haruki', 'Murakami', '1949-01-12', 'Japon yazar. Modern Japon edebiyatının önemli temsilcisi.'),
('Paulo', 'Coelho', '1947-08-24', 'Brezilyalı yazar. Simyacı romanıyla dünya çapında tanınır.'),
('Umberto', 'Eco', '1932-01-05', 'İtalyan yazar ve akademisyen. Gülün Adı romanıyla ünlü.'),
('Jorge Luis', 'Borges', '1899-08-24', 'Arjantinli yazar ve şair. Fantastik edebiyatın öncülerinden.'),
('Italo', 'Calvino', '1923-10-15', 'İtalyan yazar. Postmodern edebiyatın önemli isimlerinden.'),
('Albert', 'Camus', '1913-11-07', 'Fransız yazar ve filozof. Yabancı romanıyla Nobel ödülü almıştır.'),
('George', 'Orwell', '1903-06-25', 'İngiliz yazar. 1984 ve Hayvan Çiftliği ile ünlü.'),
('J.D.', 'Salinger', '1919-01-01', 'Amerikalı yazar. Çavdar Tarlasında Çocuklar ile ünlü.'),
('Ernest', 'Hemingway', '1899-07-21', 'Amerikalı yazar. İhtiyar Adam ve Deniz ile Nobel ödülü almıştır.'),
('Fyodor', 'Dostoyevski', '1821-11-11', 'Rus yazar. Suç ve Ceza, Karamazov Kardeşler ile ünlü.'),
('Leo', 'Tolstoy', '1828-09-09', 'Rus yazar. Savaş ve Barış, Anna Karenina ile ünlü.');

-- Kitaplar
INSERT IGNORE INTO books (title, isbn, author_id, category_id, publication_date, publisher, total_copies, available_copies, description) VALUES
-- Orhan Pamuk Kitapları
('Kafamda Bir Tuhaflık', '9789750827988', 1, 1, '2014-03-01', 'Yapı Kredi Yayınları', 5, 5, 'Orhan Pamuk''un modern İstanbul romanı. Bir sokak satıcısının hikayesi.'),
('Benim Adım Kırmızı', '9789750805139', 1, 1, '1998-01-01', 'İletişim Yayınları', 3, 3, '16. yüzyıl İstanbul''unda geçen bir cinayet romanı.'),
('Kar', '9789750807560', 1, 1, '2002-01-01', 'İletişim Yayınları', 4, 4, 'Kars şehrinde geçen siyasi ve romantik bir hikaye.'),
('Masumiyet Müzesi', '9789750811048', 1, 1, '2008-08-01', 'İletişim Yayınları', 3, 3, 'Aşk ve tutku dolu bir hikaye.'),
('Yeni Hayat', '9789754704547', 1, 1, '1994-01-01', 'İletişim Yayınları', 2, 2, 'Postmodern bir yolculuk hikayesi.'),
('Beyaz Kale', '9789754704548', 1, 1, '1985-01-01', 'Can Yayınları', 3, 3, 'Osmanlı döneminde geçen bir hikaye.'),
-- Elif Şafak Kitapları
('Aşk', '9789750817057', 2, 1, '2009-03-01', 'Doğan Kitap', 4, 4, 'Elif Şafak''ın en çok okunan romanlarından biri.'),
('İskender', '9789750817058', 2, 1, '2011-01-01', 'Doğan Kitap', 3, 3, 'Aile ve kimlik üzerine bir roman.'),
('Şemspare', '9789750817059', 2, 1, '2012-01-01', 'Doğan Kitap', 3, 3, 'Doğu ve Batı arasındaki köprü.'),
('Ustam ve Ben', '9789750817060', 2, 1, '2013-01-01', 'Doğan Kitap', 4, 4, 'Mimar Sinan ve çırağı hakkında.'),
('Kırk Kural', '9789750817061', 2, 1, '2010-01-01', 'Doğan Kitap', 3, 3, 'Sufi felsefesi üzerine bir roman.'),
-- İlber Ortaylı Kitapları
('Türklerin Tarihi', '9789752430965', 3, 2, '2015-01-01', 'Timaş Yayınları', 6, 6, 'Türk tarihi üzerine kapsamlı bir çalışma.'),
('Osmanlı''yı Yeniden Keşfetmek', '9789752430966', 3, 2, '2006-01-01', 'Timaş Yayınları', 5, 5, 'Osmanlı tarihine farklı bir bakış.'),
('İmparatorluğun En Uzun Yüzyılı', '9789752430967', 3, 2, '1983-01-01', 'Timaş Yayınları', 4, 4, '19. yüzyıl Osmanlı tarihi.'),
('Tarihin Işığında', '9789752430968', 3, 2, '2018-01-01', 'Timaş Yayınları', 3, 3, 'Tarih üzerine denemeler.'),
-- Ahmet Ümit Kitapları
('Patasana', '9789750817514', 4, 6, '2000-01-01', 'Doğan Kitap', 3, 3, 'Ahmet Ümit''in polisiye romanı.'),
('İstanbul Hatırası', '9789750817515', 4, 6, '2010-01-01', 'Everest Yayınları', 4, 4, 'İstanbul''da geçen bir polisiye.'),
('Beyoğlu''nun En Güzel Abisi', '9789750817516', 4, 6, '2013-01-01', 'Everest Yayınları', 3, 3, 'Beyoğlu''nda geçen bir hikaye.'),
('Elveda Güzel Vatanım', '9789750817517', 4, 6, '2015-01-01', 'Everest Yayınları', 3, 3, 'Tarihi bir polisiye roman.'),
('Sis ve Gece', '9789750817518', 4, 6, '1996-01-01', 'Doğan Kitap', 4, 4, 'Ahmet Ümit''in ilk romanı.'),
-- Yaşar Kemal Kitapları
('İnce Memed', '9789750805130', 5, 1, '1955-01-01', 'Yapı Kredi Yayınları', 5, 5, 'Çukurova''da geçen efsanevi bir hikaye.'),
('Yer Demir Gök Bakır', '9789750805131', 5, 1, '1963-01-01', 'Yapı Kredi Yayınları', 4, 4, 'Köy hayatını anlatan bir roman.'),
('Ölmez Otu', '9789750805132', 5, 1, '1968-01-01', 'Yapı Kredi Yayınları', 3, 3, 'Doğa ve insan ilişkisi.'),
('Demirciler Çarşısı Cinayeti', '9789750805133', 5, 1, '1974-01-01', 'Yapı Kredi Yayınları', 3, 3, 'Bir cinayet hikayesi.'),
-- Nazım Hikmet Kitapları
('Memleketimden İnsan Manzaraları', '9789750805140', 6, 8, '1966-01-01', 'Yapı Kredi Yayınları', 4, 4, 'Nazım Hikmet''in en önemli eseri.'),
('Şiirler', '9789750805141', 6, 8, '1950-01-01', 'Yapı Kredi Yayınları', 5, 5, 'Nazım Hikmet''in şiir derlemesi.'),
('Piraye''ye Mektuplar', '9789750805142', 6, 8, '1998-01-01', 'Yapı Kredi Yayınları', 3, 3, 'Nazım Hikmet''in eşine yazdığı mektuplar.'),
-- Reşat Nuri Güntekin Kitapları
('Çalıkuşu', '9789750805150', 7, 1, '1922-01-01', 'İnkılap Yayınları', 6, 6, 'Türk edebiyatının klasikleri arasında.'),
('Yaprak Dökümü', '9789750805151', 7, 1, '1930-01-01', 'İnkılap Yayınları', 4, 4, 'Aile dramı üzerine bir roman.'),
('Dudaktan Kalbe', '9789750805152', 7, 1, '1925-01-01', 'İnkılap Yayınları', 3, 3, 'Aşk ve ihanet hikayesi.'),
-- Halide Edib Adıvar Kitapları
('Sinekli Bakkal', '9789750805160', 8, 1, '1936-01-01', 'Can Yayınları', 4, 4, 'Osmanlı döneminde geçen bir roman.'),
('Ateşten Gömlek', '9789750805161', 8, 1, '1922-01-01', 'Can Yayınları', 3, 3, 'Kurtuluş Savaşı dönemini anlatır.'),
('Vurun Kahpeye', '9789750805162', 8, 1, '1926-01-01', 'Can Yayınları', 3, 3, 'Milli Mücadele dönemi romanı.'),
-- Sabahattin Ali Kitapları
('Kürk Mantolu Madonna', '9789750805170', 9, 1, '1943-01-01', 'Yapı Kredi Yayınları', 5, 5, 'Aşk ve yalnızlık üzerine bir roman.'),
('İçimizdeki Şeytan', '9789750805171', 9, 1, '1940-01-01', 'Yapı Kredi Yayınları', 4, 4, 'Toplumsal eleştiri romanı.'),
('Kuyucaklı Yusuf', '9789750805172', 9, 1, '1937-01-01', 'Yapı Kredi Yayınları', 3, 3, 'Köy hayatını anlatan bir roman.'),
-- Oğuz Atay Kitapları
('Tutunamayanlar', '9789750805180', 10, 1, '1971-01-01', 'İletişim Yayınları', 4, 4, 'Modern Türk edebiyatının başyapıtı.'),
('Tehlikeli Oyunlar', '9789750805181', 10, 1, '1973-01-01', 'İletişim Yayınları', 3, 3, 'Oğuz Atay''ın ikinci romanı.'),
('Bir Bilim Adamının Romanı', '9789750805182', 10, 1, '1975-01-01', 'İletişim Yayınları', 2, 2, 'Biyografik bir roman.'),
-- Stefan Zweig Kitapları
('Satranç', '9789750807485', 21, 1, '1942-01-01', 'İletişim Yayınları', 4, 4, 'Stefan Zweig''ın ünlü novellası.'),
('Amok Koşucusu', '9789750807486', 21, 1, '1922-01-01', 'İletişim Yayınları', 3, 3, 'Tutku ve çılgınlık hikayesi.'),
('Bir Kadının Yirmi Dört Saati', '9789750807487', 21, 1, '1927-01-01', 'İletişim Yayınları', 3, 3, 'Psikolojik bir hikaye.'),
('Marie Antoinette', '9789750807488', 21, 5, '1932-01-01', 'Can Yayınları', 2, 2, 'Fransız kraliçesinin biyografisi.'),
-- Franz Kafka Kitapları
('Dönüşüm', '9789750805190', 22, 1, '1915-01-01', 'İş Bankası Kültür Yayınları', 5, 5, 'Gregor Samsa''nın hikayesi.'),
('Dava', '9789750805191', 22, 1, '1925-01-01', 'İş Bankası Kültür Yayınları', 4, 4, 'Bürokrasi eleştirisi.'),
('Şato', '9789750805192', 22, 1, '1926-01-01', 'İş Bankası Kültür Yayınları', 3, 3, 'Kafka''nın son romanı.'),
-- Gabriel García Márquez Kitapları
('Yüzyıllık Yalnızlık', '9789750805200', 23, 1, '1967-01-01', 'Can Yayınları', 5, 5, 'Nobel ödüllü büyülü gerçekçilik romanı.'),
('Kırmızı Pazartesi', '9789750805201', 23, 1, '1981-01-01', 'Can Yayınları', 4, 4, 'Bir cinayet hikayesi.'),
('Kolera Günlerinde Aşk', '9789750805202', 23, 1, '1985-01-01', 'Can Yayınları', 3, 3, 'Aşk ve zaman üzerine.'),
-- Milan Kundera Kitapları
('Varolmanın Dayanılmaz Hafifliği', '9789750805210', 24, 1, '1984-01-01', 'Can Yayınları', 4, 4, 'Felsefi bir roman.'),
('Gülünesi Aşklar', '9789750805211', 24, 1, '1969-01-01', 'Can Yayınları', 3, 3, 'Aşk hikayeleri.'),
('Kimlik', '9789750805212', 24, 1, '1997-01-01', 'Can Yayınları', 2, 2, 'Kimlik sorgulaması.'),
-- Haruki Murakami Kitapları
('Norveç Ormanı', '9789750805220', 25, 1, '1987-01-01', 'Doğan Kitap', 4, 4, 'Gençlik ve kayıp üzerine.'),
('1Q84', '9789750805221', 25, 7, '2009-01-01', 'Doğan Kitap', 3, 3, 'Fantastik bir distopya.'),
('Kumandanı Öldürmek', '9789750805222', 25, 1, '2017-01-01', 'Doğan Kitap', 3, 3, 'Murakami''nin son romanı.'),
-- Paulo Coelho Kitapları
('Simyacı', '9789750805230', 26, 1, '1988-01-01', 'Can Yayınları', 6, 6, 'Dünya çapında en çok okunan kitaplardan.'),
('On Bir Dakika', '9789750805231', 26, 1, '2003-01-01', 'Can Yayınları', 4, 4, 'Aşk ve tutku hikayesi.'),
('Zahir', '9789750805232', 26, 1, '2005-01-01', 'Can Yayınları', 3, 3, 'Arayış ve buluş hikayesi.'),
-- Umberto Eco Kitapları
('Gülün Adı', '9789750805240', 27, 1, '1980-01-01', 'Can Yayınları', 4, 4, 'Ortaçağ manastırında bir cinayet.'),
('Foucault Sarkacı', '9789750805241', 27, 1, '1988-01-01', 'Can Yayınları', 3, 3, 'Komplo teorileri üzerine.'),
('Prag Mezarlığı', '9789750805242', 27, 1, '2010-01-01', 'Can Yayınları', 2, 2, 'Tarihi bir roman.'),
-- Albert Camus Kitapları
('Yabancı', '9789750805250', 30, 1, '1942-01-01', 'Can Yayınları', 5, 5, 'Varoluşçu edebiyatın başyapıtı.'),
('Veba', '9789750805251', 30, 1, '1947-01-01', 'Can Yayınları', 4, 4, 'Alegorik bir roman.'),
('Düşüş', '9789750805252', 30, 1, '1956-01-01', 'Can Yayınları', 3, 3, 'Felsefi bir monolog.'),
-- George Orwell Kitapları
('1984', '9789750805260', 31, 7, '1949-01-01', 'Can Yayınları', 6, 6, 'Distopya edebiyatının klasikleri arasında.'),
('Hayvan Çiftliği', '9789750805261', 31, 1, '1945-01-01', 'Can Yayınları', 5, 5, 'Alegorik bir siyasi hiciv.'),
-- Fyodor Dostoyevski Kitapları
('Suç ve Ceza', '9789750805270', 34, 1, '1866-01-01', 'İş Bankası Kültür Yayınları', 5, 5, 'Rus edebiyatının başyapıtı.'),
('Karamazov Kardeşler', '9789750805271', 34, 1, '1880-01-01', 'İş Bankası Kültür Yayınları', 4, 4, 'Dostoyevski''nin son ve en büyük eseri.'),
('Budala', '9789750805272', 34, 1, '1869-01-01', 'İş Bankası Kültür Yayınları', 3, 3, 'İyilik ve kötülük üzerine.'),
-- Leo Tolstoy Kitapları
('Savaş ve Barış', '9789750805280', 35, 1, '1869-01-01', 'İş Bankası Kültür Yayınları', 4, 4, 'Dünya edebiyatının en büyük eserlerinden.'),
('Anna Karenina', '9789750805281', 35, 1, '1877-01-01', 'İş Bankası Kültür Yayınları', 4, 4, 'Aşk ve toplumsal eleştiri.'),
('İvan İlyiç''in Ölümü', '9789750805282', 35, 1, '1886-01-01', 'İş Bankası Kültür Yayınları', 3, 3, 'Ölüm ve yaşam üzerine.'),
-- Diğer Türk Yazarlar
('Şu Çılgın Türkler', '9789750805290', 13, 2, '2005-01-01', 'Bilgi Yayınevi', 5, 5, 'Kurtuluş Savaşı''nı anlatan bir eser.'),
('Serenad', '9789750805300', 15, 1, '2011-01-01', 'Doğan Kitap', 4, 4, 'Zülfü Livaneli''nin tarihi romanı.'),
('Kardeşimin Hikayesi', '9789750805310', 14, 1, '2013-01-01', 'Everest Yayınları', 3, 3, 'Ayşe Kulin''in aile romanı.'),
('Puslu Kıtalar Atlası', '9789750805320', 16, 7, '1995-01-01', 'İletişim Yayınları', 4, 4, 'İhsan Oktay Anar''ın fantastik romanı.'),
('Az', '9789750805330', 17, 1, '2011-01-01', 'İletişim Yayınları', 3, 3, 'Murat Menteş''in modern romanı.'),
('Balık İzlerinin Sesi', '9789750805340', 18, 1, '1993-01-01', 'Everest Yayınları', 3, 3, 'Buket Uzuner''in çevre temalı romanı.'),
('Kinyas ve Kayra', '9789750805350', 19, 1, '2000-01-01', 'Doğan Kitap', 2, 2, 'Hakan Günday''ın sert romanı.'),
('Semaver', '9789750805360', 20, 1, '1936-01-01', 'Yapı Kredi Yayınları', 4, 4, 'Sait Faik''in öykü derlemesi.'),
('Mahalle Kahvesi', '9789750805361', 20, 1, '1950-01-01', 'Yapı Kredi Yayınları', 3, 3, 'Sait Faik''in öyküleri.'),
-- Bilim ve Felsefe Kitapları
('Zamanın Kısa Tarihi', '9789750805400', NULL, 3, '1988-01-01', 'Doğan Kitap', 4, 4, 'Stephen Hawking''in popüler bilim kitabı.'),
('Sofie''nin Dünyası', '9789750805410', NULL, 4, '1991-01-01', 'Pan Yayınları', 5, 5, 'Felsefe tarihine giriş romanı.'),
('İnsanın Anlam Arayışı', '9789750805420', NULL, 10, '1946-01-01', 'Okuyan Us Yayınları', 4, 4, 'Viktor Frankl''ın logoterapi kitabı.'),
('Düşünüyorum Öyleyse Varım', '9789750805430', NULL, 4, '1637-01-01', 'Say Yayınları', 3, 3, 'Descartes''in felsefe eseri.'),
-- Çocuk Kitapları
('Küçük Prens', '9789750805500', NULL, 9, '1943-01-01', 'Can Çocuk Yayınları', 6, 6, 'Antoine de Saint-Exupéry''nin klasik eseri.'),
('Şeker Portakalı', '9789750805510', NULL, 9, '1968-01-01', 'Can Çocuk Yayınları', 5, 5, 'José Mauro de Vasconcelos''un çocuk romanı.'),
('Charlie''nin Çikolata Fabrikası', '9789750805520', NULL, 9, '1964-01-01', 'Can Çocuk Yayınları', 4, 4, 'Roald Dahl''ın çocuk kitabı.');

-- Not: Kullanıcılar için şifreler hash'lenmiş olmalı
-- Bu örnek veriler sadece test amaçlıdır
-- Gerçek uygulamada kullanıcılar kayıt sayfasından oluşturulmalıdır
