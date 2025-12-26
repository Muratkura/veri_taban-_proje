# Kütüphane Yönetim Sistemi

Modern web teknolojileri kullanılarak geliştirilmiş kapsamlı bir kütüphane yönetim sistemidir. Flask backend ve vanilla JavaScript frontend ile katmanlı mimari prensiplerine uygun olarak tasarlanmıştır.

## 🚀 Özellikler

### Kullanıcı Özellikleri
- ✅ JWT tabanlı kimlik doğrulama
- ✅ Kullanıcı kaydı ve girişi
- ✅ Kitap arama ve listeleme
- ✅ Kitap ödünç alma (admin onayı ile)
- ✅ Ödünç geçmişi görüntüleme
- ✅ Ceza takibi

### Admin Özellikleri
- ✅ Ödünç taleplerini onaylama/reddetme
- ✅ Kullanıcı yönetimi
- ✅ Kitap, yazar, kategori yönetimi
- ✅ Sistem istatistikleri
- ✅ Tüm ödünç işlemlerini görüntüleme

### Veritabanı Özellikleri
- ✅ Trigger'lar (otomatik ceza hesaplama, kopya sayısı güncelleme)
- ✅ Stored Procedure'lar (istatistikler, ceza hesaplama)
- ✅ İlişkisel veritabanı tasarımı
- ✅ Index'ler (performans optimizasyonu)

## 🛠️ Teknolojiler

### Backend
- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **Flask-JWT-Extended** - JWT kimlik doğrulama
- **Flask-Mail** - E-posta gönderimi
- **MySQL** - Veritabanı
- **PyMySQL** - MySQL driver

### Frontend
- **HTML5** - Yapı
- **CSS3** - Stil
- **JavaScript (Vanilla)** - İşlevsellik
- **Fetch API** - API çağrıları

## 📁 Proje Yapısı

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
│   ├── init_sample_data.sql  # Örnek veriler
│   └── migration_add_approval_status.sql  # Migration dosyası
├── frontend/              # Frontend uygulaması
│   ├── index.html         # Ana sayfa
│   ├── login.html         # Giriş sayfası
│   ├── register.html      # Kayıt sayfası
│   ├── loans.html         # Ödünçler sayfası
│   ├── fines.html         # Cezalar sayfası
│   ├── admin-approvals.html  # Admin onay sayfası
│   ├── css/               # Stil dosyaları
│   └── js/                # JavaScript dosyaları
├── requirements.txt       # Python bağımlılıkları
├── run.py                 # Uygulama başlatma dosyası
├── create_admin.py        # Admin kullanıcı oluşturma scripti
├── populate_database.py   # Veritabanı doldurma scripti
└── README.md              # Bu dosya
```

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- MySQL 8.0+
- pip (Python paket yöneticisi)

### Adım 1: Proje Kurulumu

1. Proje klasörüne gidin:
```bash
cd veri_tabanı_proje
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

### Adım 2: Veritabanı Kurulumu

1. MySQL'de veritabanı oluşturun:
```bash
mysql -u root -p
```

```sql
CREATE DATABASE kutuphane_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

2. Veritabanı şemasını yükleyin:
```bash
mysql -u root -p kutuphane_db < database/schema.sql
```

3. (Opsiyonel) Örnek verileri yükleyin:
```bash
mysql -u root -p kutuphane_db < database/init_sample_data.sql
```

### Adım 3: Ortam Değişkenleri

`.env` dosyası oluşturun:
```env
DATABASE_URL=mysql+pymysql://root:SIFRENIZ@localhost:3306/kutuphane_db
JWT_SECRET_KEY=super-secret-key-change-in-production
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=
MAIL_PASSWORD=
FLASK_APP=run.py
FLASK_ENV=development
```

**ÖNEMLİ:** `DATABASE_URL` satırındaki `SIFRENIZ` kısmını kendi MySQL şifrenizle değiştirin!

### Adım 4: Uygulamayı Çalıştırma

1. Backend'i başlatın:
```bash
python run.py
```

Backend http://localhost:5001 adresinde çalışacaktır.

2. Frontend'i açın:
- Tarayıcınızda `frontend/login.html` dosyasını açın
- Veya Live Server kullanın

### Adım 5: İlk Kullanıcı Oluşturma

#### Normal Kullanıcı
1. `frontend/register.html` sayfasına gidin
2. Yeni bir hesap oluşturun

#### Admin Kullanıcı
```bash
python create_admin.py
```

Script size kullanıcı bilgilerini soracak ve admin kullanıcı oluşturacaktır.

## 📚 API Endpoints

### Kimlik Doğrulama
- `POST /api/auth/register` - Kullanıcı kaydı
- `POST /api/auth/login` - Giriş yapma
- `GET /api/auth/me` - Mevcut kullanıcı bilgisi

### Kitaplar
- `GET /api/books` - Tüm kitapları listele
- `GET /api/books?q=<query>` - Kitap ara
- `GET /api/books/<id>` - Kitap detayı
- `POST /api/books` - Yeni kitap ekle (Admin)
- `PUT /api/books/<id>` - Kitap güncelle (Admin)
- `DELETE /api/books/<id>` - Kitap sil (Admin)

### Ödünç İşlemleri
- `GET /api/loans` - Ödünç listesi
- `GET /api/loans/active` - Aktif ödünçler
- `GET /api/loans/pending` - Onay bekleyen ödünçler (Admin)
- `POST /api/loans` - Kitap ödünç al (onay bekliyor)
- `PUT /api/loans/<id>/approve` - Ödünç onayla (Admin)
- `PUT /api/loans/<id>/reject` - Ödünç reddet (Admin)
- `PUT /api/loans/<id>/return` - Kitap iade et
- `GET /api/loans/fines` - Ceza listesi

### Admin İşlemleri
- `GET /api/admin/statistics` - Sistem istatistikleri
- `GET /api/admin/users` - Kullanıcı listesi
- `PUT /api/admin/users/<id>` - Kullanıcı güncelle
- `DELETE /api/admin/users/<id>` - Kullanıcı sil
- `GET /api/admin/authors` - Yazar listesi
- `POST /api/admin/authors` - Yazar ekle
- `GET /api/admin/categories` - Kategori listesi
- `POST /api/admin/categories` - Kategori ekle

## 🗄️ Veritabanı Şeması

### Tablolar
- `users` - Kullanıcılar (student, staff, admin rolleri)
- `books` - Kitaplar
- `authors` - Yazarlar
- `categories` - Kategoriler
- `loans` - Ödünç işlemleri (pending, approved, rejected durumları)
- `fines` - Ceza kayıtları

### Önemli Özellikler
- **Admin Onay Sistemi:** Tüm ödünç talepleri admin onayı bekler
- **Otomatik Ceza Hesaplama:** Geç iade edilen kitaplar için otomatik ceza
- **Trigger'lar:** Kopya sayısı otomatik güncelleme
- **Stored Procedure'lar:** İstatistik ve raporlama

## 🏗️ Mimari

Proje katmanlı mimari prensibine uygun olarak geliştirilmiştir:

1. **Model/Entity Katmanı:** Veritabanı modelleri (SQLAlchemy)
2. **Repository Katmanı:** Veritabanı işlemleri (CRUD)
3. **Service Katmanı:** İş mantığı
4. **Controller Katmanı:** API endpoints (REST)

## 🔒 Güvenlik

- JWT token tabanlı kimlik doğrulama
- Şifreler Werkzeug ile hash'leniyor
- Rol tabanlı yetkilendirme (admin, student, staff)
- CORS desteği
- SQL injection koruması (SQLAlchemy ORM)

## 📝 Kullanım

### Normal Kullanıcı
1. Kayıt olun veya giriş yapın
2. Kitapları arayın ve listeleyin
3. Kitap ödünç alın (admin onayı bekler)
4. Ödünç geçmişinizi görüntüleyin
5. Ceza durumunuzu kontrol edin

### Admin
1. Admin kullanıcı ile giriş yapın
2. "Onay Bekleyenler" sayfasından ödünç taleplerini onaylayın/reddedin
3. Kullanıcı, kitap, yazar ve kategori yönetimi yapın
4. Sistem istatistiklerini görüntüleyin

## 🐛 Sorun Giderme

### Veritabanı Bağlantı Hatası
- MySQL'in çalıştığından emin olun
- `.env` dosyasındaki `DATABASE_URL` değerini kontrol edin
- MySQL kullanıcı adı ve şifresinin doğru olduğundan emin olun

### Port Kullanımda
- 5001 portu kullanılıyorsa `run.py` dosyasındaki port numarasını değiştirin

### Admin Yetkisi Hatası
- Kullanıcının `role` alanının `admin` olduğundan emin olun
- Çıkış yapıp tekrar giriş yapın

## 📄 Lisans

Bu proje eğitim amaçlıdır.
