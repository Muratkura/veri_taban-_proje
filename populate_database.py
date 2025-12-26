"""
Veritabanını örnek verilerle doldurmak için script
Kullanım: python populate_database.py
"""

from app import create_app, db
from app.models.book import Book, Author, Category
from datetime import date
import sys

def populate_database():
    """Veritabanını örnek verilerle doldur"""
    app = create_app()
    
    with app.app_context():
        print("Veritabani dolduruluyor...")
        
        # Kategoriler
        categories_data = [
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
            ('Mizah', 'Mizah ve komedi kitapları'),
        ]
        
        category_map = {}
        for name, desc in categories_data:
            category = Category.query.filter_by(name=name).first()
            if not category:
                category = Category(name=name, description=desc)
                db.session.add(category)
                db.session.flush()
            category_map[name] = category
        
        print(f"[OK] {len(category_map)} kategori eklendi/guncellendi")
        
        # Yazarlar
        authors_data = [
            # Türk Yazarlar
            ('Orhan', 'Pamuk', date(1952, 6, 7), 'Nobel Edebiyat Ödülü sahibi Türk yazar. Modern Türk edebiyatının önemli isimlerinden.'),
            ('Elif', 'Şafak', date(1971, 10, 25), 'Türk yazar ve akademisyen. Çok sayıda ödüllü romanı bulunmaktadır.'),
            ('İlber', 'Ortaylı', date(1947, 5, 21), 'Türk tarihçi ve akademisyen. Osmanlı tarihi uzmanı.'),
            ('Ahmet', 'Ümit', date(1960, 9, 30), 'Türk yazar ve şair. Polisiye romanlarıyla tanınır.'),
            ('Yaşar', 'Kemal', date(1923, 10, 6), 'Türk yazar ve şair. Çukurova bölgesini anlatan eserleriyle ünlü.'),
            ('Nazım', 'Hikmet', date(1902, 1, 15), 'Türk şair, oyun yazarı ve romancı. Modern Türk şiirinin öncüsü.'),
            ('Reşat', 'Nuri Güntekin', date(1889, 11, 25), 'Türk yazar. Çalıkuşu romanıyla tanınır.'),
            ('Halide', 'Edib Adıvar', date(1884, 6, 11), 'Türk yazar ve siyasetçi. Milli Mücadele dönemi yazarlarından.'),
            ('Sabahattin', 'Ali', date(1907, 2, 25), 'Türk yazar ve şair. Kürk Mantolu Madonna eseriyle ünlü.'),
            ('Oğuz', 'Atay', date(1934, 10, 12), 'Türk yazar. Tutunamayanlar romanıyla tanınır.'),
            ('Peyami', 'Safa', date(1899, 4, 2), 'Türk yazar ve gazeteci. Dokuzuncu Hariciye Koğuşu ile ünlü.'),
            ('Cemal', 'Süreya', date(1931, 8, 1), 'Türk şair. İkinci Yeni akımının önemli temsilcilerinden.'),
            ('Turgut', 'Ozakman', date(1930, 9, 1), 'Türk yazar ve tiyatro eleştirmeni. Şu Çılgın Türkler ile ünlü.'),
            ('Ayşe', 'Kulin', date(1941, 8, 26), 'Türk yazar ve gazeteci. Biyografik romanlarıyla tanınır.'),
            ('Zülfü', 'Livaneli', date(1946, 6, 20), 'Türk müzisyen, yazar ve siyasetçi. Serenad romanıyla ünlü.'),
            ('İhsan', 'Oktay Anar', date(1960, 3, 11), 'Türk yazar. Fantastik ve tarihi romanlarıyla tanınır.'),
            ('Murat', 'Menteş', date(1974, 1, 1), 'Türk yazar. Modern Türk edebiyatının önemli isimlerinden.'),
            ('Buket', 'Uzuner', date(1955, 10, 3), 'Türk yazar. Çevre ve doğa temalı eserleriyle tanınır.'),
            ('Hakan', 'Günday', date(1976, 5, 29), 'Türk yazar. Sert ve gerçekçi romanlarıyla tanınır.'),
            ('Sait', 'Faik Abasıyanık', date(1906, 11, 18), 'Türk öykü yazarı. Modern Türk öykücülüğünün öncüsü.'),
            # Yabancı Yazarlar
            ('Stefan', 'Zweig', date(1881, 11, 28), 'Avusturyalı yazar. Biyografi ve novella türünde eserler vermiştir.'),
            ('Franz', 'Kafka', date(1883, 7, 3), 'Çek-Alman yazar. Dönüşüm ve Dava eserleriyle ünlü.'),
            ('Gabriel', 'García Márquez', date(1927, 3, 6), 'Kolombiyalı yazar. Yüzyıllık Yalnızlık ile Nobel ödülü almıştır.'),
            ('Milan', 'Kundera', date(1929, 4, 1), 'Çek-Fransız yazar. Varolmanın Dayanılmaz Hafifliği ile ünlü.'),
            ('Haruki', 'Murakami', date(1949, 1, 12), 'Japon yazar. Modern Japon edebiyatının önemli temsilcisi.'),
            ('Paulo', 'Coelho', date(1947, 8, 24), 'Brezilyalı yazar. Simyacı romanıyla dünya çapında tanınır.'),
            ('Umberto', 'Eco', date(1932, 1, 5), 'İtalyan yazar ve akademisyen. Gülün Adı romanıyla ünlü.'),
            ('Jorge Luis', 'Borges', date(1899, 8, 24), 'Arjantinli yazar ve şair. Fantastik edebiyatın öncülerinden.'),
            ('Italo', 'Calvino', date(1923, 10, 15), 'İtalyan yazar. Postmodern edebiyatın önemli isimlerinden.'),
            ('Albert', 'Camus', date(1913, 11, 7), 'Fransız yazar ve filozof. Yabancı romanıyla Nobel ödülü almıştır.'),
            ('George', 'Orwell', date(1903, 6, 25), 'İngiliz yazar. 1984 ve Hayvan Çiftliği ile ünlü.'),
            ('J.D.', 'Salinger', date(1919, 1, 1), 'Amerikalı yazar. Çavdar Tarlasında Çocuklar ile ünlü.'),
            ('Ernest', 'Hemingway', date(1899, 7, 21), 'Amerikalı yazar. İhtiyar Adam ve Deniz ile Nobel ödülü almıştır.'),
            ('Fyodor', 'Dostoyevski', date(1821, 11, 11), 'Rus yazar. Suç ve Ceza, Karamazov Kardeşler ile ünlü.'),
            ('Leo', 'Tolstoy', date(1828, 9, 9), 'Rus yazar. Savaş ve Barış, Anna Karenina ile ünlü.'),
        ]
        
        author_map = {}
        for first_name, last_name, birth_date, bio in authors_data:
            author = Author.query.filter_by(first_name=first_name, last_name=last_name).first()
            if not author:
                author = Author(
                    first_name=first_name,
                    last_name=last_name,
                    birth_date=birth_date,
                    biography=bio
                )
                db.session.add(author)
                db.session.flush()
            author_map[(first_name, last_name)] = author
        
        print(f"[OK] {len(author_map)} yazar eklendi/guncellendi")
        
        # Kitaplar
        books_data = [
            # Orhan Pamuk
            ('Kafamda Bir Tuhaflık', '9789750827988', ('Orhan', 'Pamuk'), 'Roman', date(2014, 3, 1), 'Yapı Kredi Yayınları', 5, 'Orhan Pamuk''un modern İstanbul romanı. Bir sokak satıcısının hikayesi.'),
            ('Benim Adım Kırmızı', '9789750805139', ('Orhan', 'Pamuk'), 'Roman', date(1998, 1, 1), 'İletişim Yayınları', 3, '16. yüzyıl İstanbul''unda geçen bir cinayet romanı.'),
            ('Kar', '9789750807560', ('Orhan', 'Pamuk'), 'Roman', date(2002, 1, 1), 'İletişim Yayınları', 4, 'Kars şehrinde geçen siyasi ve romantik bir hikaye.'),
            ('Masumiyet Müzesi', '9789750811048', ('Orhan', 'Pamuk'), 'Roman', date(2008, 8, 1), 'İletişim Yayınları', 3, 'Aşk ve tutku dolu bir hikaye.'),
            ('Yeni Hayat', '9789754704547', ('Orhan', 'Pamuk'), 'Roman', date(1994, 1, 1), 'İletişim Yayınları', 2, 'Postmodern bir yolculuk hikayesi.'),
            ('Beyaz Kale', '9789754704548', ('Orhan', 'Pamuk'), 'Roman', date(1985, 1, 1), 'Can Yayınları', 3, 'Osmanlı döneminde geçen bir hikaye.'),
            # Elif Şafak
            ('Aşk', '9789750817057', ('Elif', 'Şafak'), 'Roman', date(2009, 3, 1), 'Doğan Kitap', 4, 'Elif Şafak''ın en çok okunan romanlarından biri.'),
            ('İskender', '9789750817058', ('Elif', 'Şafak'), 'Roman', date(2011, 1, 1), 'Doğan Kitap', 3, 'Aile ve kimlik üzerine bir roman.'),
            ('Şemspare', '9789750817059', ('Elif', 'Şafak'), 'Roman', date(2012, 1, 1), 'Doğan Kitap', 3, 'Doğu ve Batı arasındaki köprü.'),
            ('Ustam ve Ben', '9789750817060', ('Elif', 'Şafak'), 'Roman', date(2013, 1, 1), 'Doğan Kitap', 4, 'Mimar Sinan ve çırağı hakkında.'),
            ('Kırk Kural', '9789750817061', ('Elif', 'Şafak'), 'Roman', date(2010, 1, 1), 'Doğan Kitap', 3, 'Sufi felsefesi üzerine bir roman.'),
            # İlber Ortaylı
            ('Türklerin Tarihi', '9789752430965', ('İlber', 'Ortaylı'), 'Tarih', date(2015, 1, 1), 'Timaş Yayınları', 6, 'Türk tarihi üzerine kapsamlı bir çalışma.'),
            ('Osmanlı''yı Yeniden Keşfetmek', '9789752430966', ('İlber', 'Ortaylı'), 'Tarih', date(2006, 1, 1), 'Timaş Yayınları', 5, 'Osmanlı tarihine farklı bir bakış.'),
            ('İmparatorluğun En Uzun Yüzyılı', '9789752430967', ('İlber', 'Ortaylı'), 'Tarih', date(1983, 1, 1), 'Timaş Yayınları', 4, '19. yüzyıl Osmanlı tarihi.'),
            ('Tarihin Işığında', '9789752430968', ('İlber', 'Ortaylı'), 'Tarih', date(2018, 1, 1), 'Timaş Yayınları', 3, 'Tarih üzerine denemeler.'),
            # Ahmet Ümit
            ('Patasana', '9789750817514', ('Ahmet', 'Ümit'), 'Polisiye', date(2000, 1, 1), 'Doğan Kitap', 3, 'Ahmet Ümit''in polisiye romanı.'),
            ('İstanbul Hatırası', '9789750817515', ('Ahmet', 'Ümit'), 'Polisiye', date(2010, 1, 1), 'Everest Yayınları', 4, 'İstanbul''da geçen bir polisiye.'),
            ('Beyoğlu''nun En Güzel Abisi', '9789750817516', ('Ahmet', 'Ümit'), 'Polisiye', date(2013, 1, 1), 'Everest Yayınları', 3, 'Beyoğlu''nda geçen bir hikaye.'),
            ('Elveda Güzel Vatanım', '9789750817517', ('Ahmet', 'Ümit'), 'Polisiye', date(2015, 1, 1), 'Everest Yayınları', 3, 'Tarihi bir polisiye roman.'),
            ('Sis ve Gece', '9789750817518', ('Ahmet', 'Ümit'), 'Polisiye', date(1996, 1, 1), 'Doğan Kitap', 4, 'Ahmet Ümit''in ilk romanı.'),
            # Yaşar Kemal
            ('İnce Memed', '9789750805130', ('Yaşar', 'Kemal'), 'Roman', date(1955, 1, 1), 'Yapı Kredi Yayınları', 5, 'Çukurova''da geçen efsanevi bir hikaye.'),
            ('Yer Demir Gök Bakır', '9789750805131', ('Yaşar', 'Kemal'), 'Roman', date(1963, 1, 1), 'Yapı Kredi Yayınları', 4, 'Köy hayatını anlatan bir roman.'),
            ('Ölmez Otu', '9789750805132', ('Yaşar', 'Kemal'), 'Roman', date(1968, 1, 1), 'Yapı Kredi Yayınları', 3, 'Doğa ve insan ilişkisi.'),
            ('Demirciler Çarşısı Cinayeti', '9789750805133', ('Yaşar', 'Kemal'), 'Roman', date(1974, 1, 1), 'Yapı Kredi Yayınları', 3, 'Bir cinayet hikayesi.'),
            # Nazım Hikmet
            ('Memleketimden İnsan Manzaraları', '9789750805140', ('Nazım', 'Hikmet'), 'Şiir', date(1966, 1, 1), 'Yapı Kredi Yayınları', 4, 'Nazım Hikmet''in en önemli eseri.'),
            ('Şiirler', '9789750805141', ('Nazım', 'Hikmet'), 'Şiir', date(1950, 1, 1), 'Yapı Kredi Yayınları', 5, 'Nazım Hikmet''in şiir derlemesi.'),
            ('Piraye''ye Mektuplar', '9789750805142', ('Nazım', 'Hikmet'), 'Şiir', date(1998, 1, 1), 'Yapı Kredi Yayınları', 3, 'Nazım Hikmet''in eşine yazdığı mektuplar.'),
            # Stefan Zweig
            ('Satranç', '9789750807485', ('Stefan', 'Zweig'), 'Roman', date(1942, 1, 1), 'İletişim Yayınları', 4, 'Stefan Zweig''ın ünlü novellası.'),
            ('Amok Koşucusu', '9789750807486', ('Stefan', 'Zweig'), 'Roman', date(1922, 1, 1), 'İletişim Yayınları', 3, 'Tutku ve çılgınlık hikayesi.'),
            ('Bir Kadının Yirmi Dört Saati', '9789750807487', ('Stefan', 'Zweig'), 'Roman', date(1927, 1, 1), 'İletişim Yayınları', 3, 'Psikolojik bir hikaye.'),
            ('Marie Antoinette', '9789750807488', ('Stefan', 'Zweig'), 'Biyografi', date(1932, 1, 1), 'Can Yayınları', 2, 'Fransız kraliçesinin biyografisi.'),
            # Franz Kafka
            ('Dönüşüm', '9789750805190', ('Franz', 'Kafka'), 'Roman', date(1915, 1, 1), 'İş Bankası Kültür Yayınları', 5, 'Gregor Samsa''nın hikayesi.'),
            ('Dava', '9789750805191', ('Franz', 'Kafka'), 'Roman', date(1925, 1, 1), 'İş Bankası Kültür Yayınları', 4, 'Bürokrasi eleştirisi.'),
            ('Şato', '9789750805192', ('Franz', 'Kafka'), 'Roman', date(1926, 1, 1), 'İş Bankası Kültür Yayınları', 3, 'Kafka''nın son romanı.'),
            # Gabriel García Márquez
            ('Yüzyıllık Yalnızlık', '9789750805200', ('Gabriel', 'García Márquez'), 'Roman', date(1967, 1, 1), 'Can Yayınları', 5, 'Nobel ödüllü büyülü gerçekçilik romanı.'),
            ('Kırmızı Pazartesi', '9789750805201', ('Gabriel', 'García Márquez'), 'Roman', date(1981, 1, 1), 'Can Yayınları', 4, 'Bir cinayet hikayesi.'),
            ('Kolera Günlerinde Aşk', '9789750805202', ('Gabriel', 'García Márquez'), 'Roman', date(1985, 1, 1), 'Can Yayınları', 3, 'Aşk ve zaman üzerine.'),
            # Milan Kundera
            ('Varolmanın Dayanılmaz Hafifliği', '9789750805210', ('Milan', 'Kundera'), 'Roman', date(1984, 1, 1), 'Can Yayınları', 4, 'Felsefi bir roman.'),
            ('Gülünesi Aşklar', '9789750805211', ('Milan', 'Kundera'), 'Roman', date(1969, 1, 1), 'Can Yayınları', 3, 'Aşk hikayeleri.'),
            ('Kimlik', '9789750805212', ('Milan', 'Kundera'), 'Roman', date(1997, 1, 1), 'Can Yayınları', 2, 'Kimlik sorgulaması.'),
            # Haruki Murakami
            ('Norveç Ormanı', '9789750805220', ('Haruki', 'Murakami'), 'Roman', date(1987, 1, 1), 'Doğan Kitap', 4, 'Gençlik ve kayıp üzerine.'),
            ('1Q84', '9789750805221', ('Haruki', 'Murakami'), 'Fantastik', date(2009, 1, 1), 'Doğan Kitap', 3, 'Fantastik bir distopya.'),
            ('Kumandanı Öldürmek', '9789750805222', ('Haruki', 'Murakami'), 'Roman', date(2017, 1, 1), 'Doğan Kitap', 3, 'Murakami''nin son romanı.'),
            # Paulo Coelho
            ('Simyacı', '9789750805230', ('Paulo', 'Coelho'), 'Roman', date(1988, 1, 1), 'Can Yayınları', 6, 'Dünya çapında en çok okunan kitaplardan.'),
            ('On Bir Dakika', '9789750805231', ('Paulo', 'Coelho'), 'Roman', date(2003, 1, 1), 'Can Yayınları', 4, 'Aşk ve tutku hikayesi.'),
            ('Zahir', '9789750805232', ('Paulo', 'Coelho'), 'Roman', date(2005, 1, 1), 'Can Yayınları', 3, 'Arayış ve buluş hikayesi.'),
            # Umberto Eco
            ('Gülün Adı', '9789750805240', ('Umberto', 'Eco'), 'Roman', date(1980, 1, 1), 'Can Yayınları', 4, 'Ortaçağ manastırında bir cinayet.'),
            ('Foucault Sarkacı', '9789750805241', ('Umberto', 'Eco'), 'Roman', date(1988, 1, 1), 'Can Yayınları', 3, 'Komplo teorileri üzerine.'),
            ('Prag Mezarlığı', '9789750805242', ('Umberto', 'Eco'), 'Roman', date(2010, 1, 1), 'Can Yayınları', 2, 'Tarihi bir roman.'),
            # Albert Camus
            ('Yabancı', '9789750805250', ('Albert', 'Camus'), 'Roman', date(1942, 1, 1), 'Can Yayınları', 5, 'Varoluşçu edebiyatın başyapıtı.'),
            ('Veba', '9789750805251', ('Albert', 'Camus'), 'Roman', date(1947, 1, 1), 'Can Yayınları', 4, 'Alegorik bir roman.'),
            ('Düşüş', '9789750805252', ('Albert', 'Camus'), 'Roman', date(1956, 1, 1), 'Can Yayınları', 3, 'Felsefi bir monolog.'),
            # George Orwell
            ('1984', '9789750805260', ('George', 'Orwell'), 'Fantastik', date(1949, 1, 1), 'Can Yayınları', 6, 'Distopya edebiyatının klasikleri arasında.'),
            ('Hayvan Çiftliği', '9789750805261', ('George', 'Orwell'), 'Roman', date(1945, 1, 1), 'Can Yayınları', 5, 'Alegorik bir siyasi hiciv.'),
            # Fyodor Dostoyevski
            ('Suç ve Ceza', '9789750805270', ('Fyodor', 'Dostoyevski'), 'Roman', date(1866, 1, 1), 'İş Bankası Kültür Yayınları', 5, 'Rus edebiyatının başyapıtı.'),
            ('Karamazov Kardeşler', '9789750805271', ('Fyodor', 'Dostoyevski'), 'Roman', date(1880, 1, 1), 'İş Bankası Kültür Yayınları', 4, 'Dostoyevski''nin son ve en büyük eseri.'),
            ('Budala', '9789750805272', ('Fyodor', 'Dostoyevski'), 'Roman', date(1869, 1, 1), 'İş Bankası Kültür Yayınları', 3, 'İyilik ve kötülük üzerine.'),
            # Leo Tolstoy
            ('Savaş ve Barış', '9789750805280', ('Leo', 'Tolstoy'), 'Roman', date(1869, 1, 1), 'İş Bankası Kültür Yayınları', 4, 'Dünya edebiyatının en büyük eserlerinden.'),
            ('Anna Karenina', '9789750805281', ('Leo', 'Tolstoy'), 'Roman', date(1877, 1, 1), 'İş Bankası Kültür Yayınları', 4, 'Aşk ve toplumsal eleştiri.'),
            ('İvan İlyiç''in Ölümü', '9789750805282', ('Leo', 'Tolstoy'), 'Roman', date(1886, 1, 1), 'İş Bankası Kültür Yayınları', 3, 'Ölüm ve yaşam üzerine.'),
            # Diğer Türk Yazarlar
            ('Şu Çılgın Türkler', '9789750805290', ('Turgut', 'Ozakman'), 'Tarih', date(2005, 1, 1), 'Bilgi Yayınevi', 5, 'Kurtuluş Savaşı''nı anlatan bir eser.'),
            ('Serenad', '9789750805300', ('Zülfü', 'Livaneli'), 'Roman', date(2011, 1, 1), 'Doğan Kitap', 4, 'Zülfü Livaneli''nin tarihi romanı.'),
            ('Kardeşimin Hikayesi', '9789750805310', ('Ayşe', 'Kulin'), 'Roman', date(2013, 1, 1), 'Everest Yayınları', 3, 'Ayşe Kulin''in aile romanı.'),
            ('Puslu Kıtalar Atlası', '9789750805320', ('İhsan', 'Oktay Anar'), 'Fantastik', date(1995, 1, 1), 'İletişim Yayınları', 4, 'İhsan Oktay Anar''ın fantastik romanı.'),
            ('Az', '9789750805330', ('Murat', 'Menteş'), 'Roman', date(2011, 1, 1), 'İletişim Yayınları', 3, 'Murat Menteş''in modern romanı.'),
            ('Balık İzlerinin Sesi', '9789750805340', ('Buket', 'Uzuner'), 'Roman', date(1993, 1, 1), 'Everest Yayınları', 3, 'Buket Uzuner''in çevre temalı romanı.'),
            ('Kinyas ve Kayra', '9789750805350', ('Hakan', 'Günday'), 'Roman', date(2000, 1, 1), 'Doğan Kitap', 2, 'Hakan Günday''ın sert romanı.'),
            ('Semaver', '9789750805360', ('Sait', 'Faik Abasıyanık'), 'Roman', date(1936, 1, 1), 'Yapı Kredi Yayınları', 4, 'Sait Faik''in öykü derlemesi.'),
            ('Mahalle Kahvesi', '9789750805361', ('Sait', 'Faik Abasıyanık'), 'Roman', date(1950, 1, 1), 'Yapı Kredi Yayınları', 3, 'Sait Faik''in öyküleri.'),
            # Reşat Nuri Güntekin
            ('Çalıkuşu', '9789750805150', ('Reşat', 'Nuri Güntekin'), 'Roman', date(1922, 1, 1), 'İnkılap Yayınları', 6, 'Türk edebiyatının klasikleri arasında.'),
            ('Yaprak Dökümü', '9789750805151', ('Reşat', 'Nuri Güntekin'), 'Roman', date(1930, 1, 1), 'İnkılap Yayınları', 4, 'Aile dramı üzerine bir roman.'),
            ('Dudaktan Kalbe', '9789750805152', ('Reşat', 'Nuri Güntekin'), 'Roman', date(1925, 1, 1), 'İnkılap Yayınları', 3, 'Aşk ve ihanet hikayesi.'),
            # Halide Edib Adıvar
            ('Sinekli Bakkal', '9789750805160', ('Halide', 'Edib Adıvar'), 'Roman', date(1936, 1, 1), 'Can Yayınları', 4, 'Osmanlı döneminde geçen bir roman.'),
            ('Ateşten Gömlek', '9789750805161', ('Halide', 'Edib Adıvar'), 'Roman', date(1922, 1, 1), 'Can Yayınları', 3, 'Kurtuluş Savaşı dönemini anlatır.'),
            ('Vurun Kahpeye', '9789750805162', ('Halide', 'Edib Adıvar'), 'Roman', date(1926, 1, 1), 'Can Yayınları', 3, 'Milli Mücadele dönemi romanı.'),
            # Sabahattin Ali
            ('Kürk Mantolu Madonna', '9789750805170', ('Sabahattin', 'Ali'), 'Roman', date(1943, 1, 1), 'Yapı Kredi Yayınları', 5, 'Aşk ve yalnızlık üzerine bir roman.'),
            ('İçimizdeki Şeytan', '9789750805171', ('Sabahattin', 'Ali'), 'Roman', date(1940, 1, 1), 'Yapı Kredi Yayınları', 4, 'Toplumsal eleştiri romanı.'),
            ('Kuyucaklı Yusuf', '9789750805172', ('Sabahattin', 'Ali'), 'Roman', date(1937, 1, 1), 'Yapı Kredi Yayınları', 3, 'Köy hayatını anlatan bir roman.'),
            # Oğuz Atay
            ('Tutunamayanlar', '9789750805180', ('Oğuz', 'Atay'), 'Roman', date(1971, 1, 1), 'İletişim Yayınları', 4, 'Modern Türk edebiyatının başyapıtı.'),
            ('Tehlikeli Oyunlar', '9789750805181', ('Oğuz', 'Atay'), 'Roman', date(1973, 1, 1), 'İletişim Yayınları', 3, 'Oğuz Atay''ın ikinci romanı.'),
            ('Bir Bilim Adamının Romanı', '9789750805182', ('Oğuz', 'Atay'), 'Biyografi', date(1975, 1, 1), 'İletişim Yayınları', 2, 'Biyografik bir roman.'),
        ]
        
        book_count = 0
        for title, isbn, author_key, category_name, pub_date, publisher, copies, desc in books_data:
            # Kitap zaten var mı kontrol et
            existing = Book.query.filter_by(isbn=isbn).first()
            if existing:
                continue
            
            author = author_map.get(author_key)
            category = category_map.get(category_name)
            
            if not author:
                print(f"[UYARI] {author_key} yazari bulunamadi, kitap atlaniyor: {title}")
                continue
            if not category:
                print(f"[UYARI] {category_name} kategorisi bulunamadi, kitap atlaniyor: {title}")
                continue
            
            book = Book(
                title=title,
                isbn=isbn,
                author_id=author.id,
                category_id=category.id,
                publication_date=pub_date,
                publisher=publisher,
                total_copies=copies,
                available_copies=copies,
                description=desc
            )
            db.session.add(book)
            book_count += 1
        
        # Degisiklikleri kaydet
        try:
            db.session.commit()
            print(f"[OK] {book_count} yeni kitap eklendi")
            print("\n[BASARILI] Veritabani basariyla dolduruldu!")
            print(f"\nOzet:")
            print(f"  - Kategoriler: {len(category_map)}")
            print(f"  - Yazarlar: {len(author_map)}")
            print(f"  - Kitaplar: {Book.query.count()}")
        except Exception as e:
            db.session.rollback()
            print(f"[HATA] {str(e)}")
            sys.exit(1)

if __name__ == '__main__':
    populate_database()

