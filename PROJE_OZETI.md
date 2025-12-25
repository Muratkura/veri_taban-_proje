# Akıllı Kütüphane Yönetim Sistemi - Proje Özeti

## Proje Hakkında

Bu proje, kütüphane işlemlerini otomatikleştiren bir web uygulamasıdır. Flask (Python) backend ve HTML/CSS/JavaScript frontend kullanılarak geliştirilmiştir.

## Özellikler

### ✅ Tamamlanan Özellikler

1. **Kimlik Doğrulama (JWT)**
   - Kullanıcı kaydı
   - Kullanıcı girişi
   - Token tabanlı kimlik doğrulama
   - Rol tabanlı yetkilendirme (admin, student, staff)

2. **Kitap Yönetimi**
   - Kitap listeleme
   - Kitap arama
   - Kitap ekleme (Admin)
   - Kitap güncelleme (Admin)
   - Kitap silme (Admin)

3. **Ödünç İşlemleri**
   - Kitap ödünç alma
   - Kitap iade etme
   - Ödünç geçmişi görüntüleme
   - Vade takibi

4. **Ceza Sistemi**
   - Geç iade cezası otomatik hesaplama
   - Ceza listeleme
   - Ceza ödeme takibi

5. **Admin Paneli**
   - Kullanıcı yönetimi
   - Yazar yönetimi
   - Kategori yönetimi
   - Sistem istatistikleri

6. **Veritabanı Özellikleri**
   - Trigger'lar (otomatik ceza hesaplama, kopya sayısı güncelleme)
   - Stored Procedure'lar (istatistikler, ceza hesaplama)
   - İlişkisel veritabanı tasarımı
   - Index'ler (performans optimizasyonu)

7. **E-posta Bildirimleri**
   - Geç iade bildirimleri
   - Vade yaklaşma bildirimleri (hazır)

## Proje Yapısı

```
veri_tabanı_proje/
├── app/                    # Backend uygulaması
│   ├── models/            # Entity katmanı (SQLAlchemy modelleri)
│   ├── repositories/      # Repository katmanı (veritabanı işlemleri)
│   ├── services/          # Service katmanı (iş mantığı)
│   ├── controllers/       # Controller katmanı (API endpoints)
│   ├── utils/             # Yardımcı fonksiyonlar
│   ├── __init__.py        # Flask app factory
│   └── config.py          # Konfigürasyon
├── database/              # Veritabanı dosyaları
│   ├── schema.sql         # Veritabanı şeması
│   └── init_sample_data.sql  # Örnek veriler
├── frontend/              # Frontend uygulaması
│   ├── index.html         # Ana sayfa
│   ├── login.html         # Giriş sayfası
│   ├── register.html      # Kayıt sayfası
│   ├── loans.html         # Ödünçler sayfası
│   ├── fines.html         # Cezalar sayfası
│   ├── css/               # Stil dosyaları
│   └── js/                # JavaScript dosyaları
├── requirements.txt       # Python bağımlılıkları
├── run.py                 # Uygulama başlatma dosyası
├── README.md              # Genel dokümantasyon
├── KURULUM.md             # Kurulum kılavuzu
└── PROJE_OZETI.md         # Bu dosya
```

## Teknolojiler

### Backend
- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **Flask-JWT-Extended** - JWT kimlik doğrulama
- **Flask-Mail** - E-posta gönderimi
- **PostgreSQL** - Veritabanı
- **psycopg2** - PostgreSQL driver

### Frontend
- **HTML5** - Yapı
- **CSS3** - Stil
- **JavaScript (Vanilla)** - İşlevsellik
- **Fetch API** - API çağrıları

## API Endpoints

### Kimlik Doğrulama
- `POST /api/auth/register` - Kullanıcı kaydı
- `POST /api/auth/login` - Giriş
- `GET /api/auth/me` - Mevcut kullanıcı bilgisi

### Kitaplar
- `GET /api/books` - Tüm kitapları listele
- `GET /api/books?q=<query>` - Kitap ara
- `GET /api/books/available` - Müsait kitapları listele
- `GET /api/books/<id>` - Kitap detayı
- `POST /api/books` - Yeni kitap ekle (Admin)
- `PUT /api/books/<id>` - Kitap güncelle (Admin)
- `DELETE /api/books/<id>` - Kitap sil (Admin)

### Ödünç İşlemleri
- `GET /api/loans` - Ödünç listesi
- `GET /api/loans/active` - Aktif ödünçler
- `POST /api/loans` - Kitap ödünç al
- `PUT /api/loans/<id>/return` - Kitap iade et
- `GET /api/loans/fines` - Ceza listesi

### Admin İşlemleri
- `GET /api/admin/statistics` - Sistem istatistikleri
- `GET /api/admin/users` - Kullanıcı listesi
- `GET /api/admin/authors` - Yazar listesi
- `POST /api/admin/authors` - Yazar ekle
- `GET /api/admin/categories` - Kategori listesi
- `POST /api/admin/categories` - Kategori ekle

## Veritabanı Şeması

### Tablolar
- `users` - Kullanıcılar
- `books` - Kitaplar
- `authors` - Yazarlar
- `categories` - Kategoriler
- `loans` - Ödünç işlemleri
- `fines` - Ceza kayıtları

### Trigger'lar
1. `update_updated_at_column` - Updated_at alanını otomatik günceller
2. `decrease_available_copies` - Ödünç alındığında kopya sayısını azaltır
3. `increase_available_copies` - İade edildiğinde kopya sayısını artırır
4. `check_overdue_and_fine` - Geç iade kontrolü ve ceza hesaplama
5. `update_loans_overdue` - Vadesi geçen kitapları otomatik işaretler

### Stored Procedure'lar
1. `update_all_overdue_loans()` - Tüm vadesi geçen kitapları günceller
2. `get_user_total_fine(user_id)` - Kullanıcının toplam cezasını hesaplar
3. `get_book_statistics()` - Sistem istatistiklerini getirir

## Katmanlı Mimari

Proje katmanlı mimari prensibine uygun olarak geliştirilmiştir:

1. **Entity/Model Katmanı**: Veritabanı modelleri (SQLAlchemy)
2. **Repository Katmanı**: Veritabanı işlemleri (CRUD)
3. **Service Katmanı**: İş mantığı
4. **Controller Katmanı**: API endpoints (REST)

## Güvenlik

- JWT token tabanlı kimlik doğrulama
- Şifreler bcrypt ile hash'lenmiyor (Werkzeug kullanılıyor)
- Rol tabanlı yetkilendirme (admin, student, staff)
- CORS desteği
- SQL injection koruması (SQLAlchemy ORM)

## Geliştirme Notları

- Tüm endpoint'ler RESTful API standartlarına uygun
- Hata yönetimi ve validasyon yapılmış
- Frontend ve backend ayrı çalışabilir
- Veritabanı migration sistemi eklenebilir (Flask-Migrate)

## İyileştirme Önerileri

1. **Güvenlik**
   - Şifre hash'leme için bcrypt kullanımı
   - Rate limiting
   - Input validation kütüphanesi (marshmallow)

2. **Performans**
   - Caching (Redis)
   - Database query optimization
   - Pagination

3. **Özellikler**
   - Rezervasyon sistemi
   - Bildirim sistemi (WebSocket)
   - Raporlama modülü
   - Admin dashboard

4. **Test**
   - Unit testler
   - Integration testler
   - E2E testler

## Lisans

Bu proje eğitim amaçlıdır.



