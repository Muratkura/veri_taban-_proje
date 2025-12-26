# Akıllı Kütüphane Yönetim Sistemi

Bu proje, kütüphane yönetim sistemini otomatikleştirmek için geliştirilmiş bir web uygulamasıdır.

## Teknolojiler

- **Backend:** Flask (Python)
- **Veritabanı:** PostgreSQL
- **Frontend:** HTML/CSS/JavaScript
- **Kimlik Doğrulama:** JWT (JSON Web Token)
- **E-posta:** Flask-Mail

## Proje Yapısı

```
veri_tabanı_proje/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/          # Entity katmanı
│   ├── repositories/    # Repository katmanı
│   ├── services/        # Service katmanı
│   ├── controllers/     # Controller katmanı
│   └── utils/           # Yardımcı fonksiyonlar
├── database/
│   └── schema.sql       # Veritabanı şeması
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── css/
│   └── js/
├── requirements.txt
└── README.md
```

## Kurulum

1. PostgreSQL veritabanını kurun ve çalıştırın

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyası oluşturun:
```env
DATABASE_URL=postgresql://kullanici:sifre@localhost:5432/kutuphane_db
JWT_SECRET_KEY=super-secret-key-change-in-production
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

4. Veritabanını oluşturun:
```bash
psql -U postgres
CREATE DATABASE kutuphane_db;
\q
psql -U postgres -d kutuphane_db -f database/schema.sql
```

5. Uygulamayı çalıştırın:
```bash
python run.py
```

## API Endpoints

### Kimlik Doğrulama
- `POST /api/auth/register` - Kullanıcı kaydı
- `POST /api/auth/login` - Giriş yapma

### Kitaplar
- `GET /api/books` - Tüm kitapları listele
- `GET /api/books/<id>` - Kitap detayı
- `GET /api/books/search?q=<query>` - Kitap ara
- `POST /api/books` - Yeni kitap ekle (Admin)
- `PUT /api/books/<id>` - Kitap güncelle (Admin)
- `DELETE /api/books/<id>` - Kitap sil (Admin)

### Ödünç İşlemleri
- `GET /api/loans` - Ödünç listesi
- `POST /api/loans` - Kitap ödünç al
- `PUT /api/loans/<id>/return` - Kitap iade et

### Admin İşlemleri
- `GET /api/authors` - Yazarları listele
- `POST /api/authors` - Yazar ekle
- `GET /api/categories` - Kategorileri listele
- `POST /api/categories` - Kategori ekle
- `GET /api/users` - Kullanıcıları listele

## Özellikler

- ✅ JWT tabanlı kimlik doğrulama
- ✅ Katmanlı mimari (Entity, Repository, Service, Controller)
- ✅ REST API endpoints
- ✅ Veritabanı trigger'ları (geç iade cezası)
- ✅ Stored procedure'lar
- ✅ E-posta bildirim sistemi
- ✅ Frontend arayüzü
- ✅ Admin CRUD işlemleri

## Test

API'leri test etmek için Postman veya Swagger kullanabilirsiniz.

## Lisans

Bu proje eğitim amaçlıdır.






