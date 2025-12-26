# Kurulum Kılavuzu

Bu kılavuz, Kütüphane Yönetim Sistemini adım adım kurmanız için hazırlanmıştır.

## Gereksinimler

- Python 3.8 veya üzeri
- MySQL 8.0 veya üzeri
- pip (Python paket yöneticisi)

## Adım 1: MySQL Kurulumu

1. MySQL'i kurun: https://dev.mysql.com/downloads/mysql/
2. MySQL'i başlatın
3. Yeni bir veritabanı oluşturun:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE kutuphane_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

## Adım 2: Proje Kurulumu

1. Proje klasörüne gidin:
```bash
cd veri_tabanı_proje
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Adım 3: Ortam Değişkenleri (.env)

1. Proje klasöründe `.env` dosyası oluşturun:

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

**ÖNEMLİ:** `DATABASE_URL` satırındaki `SIFRENIZ` kısmını kendi MySQL root şifrenizle değiştirin!

## Adım 4: Veritabanı Şemasını Oluşturma

1. SQL şemasını çalıştırın:
```bash
mysql -u root -p kutuphane_db < database/schema.sql
```

2. (Opsiyonel) Örnek verileri yükleyin:
```bash
mysql -u root -p kutuphane_db < database/init_sample_data.sql
```

## Adım 5: Uygulamayı Çalıştırma

1. Backend'i başlatın:
```bash
python run.py
```

Backend http://localhost:5001 adresinde çalışacaktır.

2. Frontend'i açın:
   - Tarayıcınızda `frontend/login.html` dosyasını açın
   - Veya bir web sunucusu kullanın (Live Server gibi)

## Adım 6: İlk Kullanıcı Oluşturma

### Normal Kullanıcı
1. `frontend/register.html` sayfasına gidin
2. Yeni bir hesap oluşturun

### Admin Kullanıcı
```bash
python create_admin.py
```

Script size kullanıcı bilgilerini soracak ve admin kullanıcı oluşturacaktır.

## Sorun Giderme

### Veritabanı Bağlantı Hatası
- MySQL'in çalıştığından emin olun
- `.env` dosyasındaki `DATABASE_URL` değerini kontrol edin
- MySQL kullanıcı adı ve şifresinin doğru olduğundan emin olun

### Port Kullanımda
- 5001 portu kullanılıyorsa `run.py` dosyasındaki port numarasını değiştirin

### Import Hatası
- Tüm paketlerin yüklendiğinden emin olun: `pip install -r requirements.txt`

