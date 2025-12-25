# Kurulum Kılavuzu

## Gereksinimler

1. Python 3.8 veya üzeri
2. MySQL 8.0 veya üzeri
3. pip (Python paket yöneticisi)

## Adım 1: MySQL Kurulumu

1. MySQL'i kurun: https://dev.mysql.com/downloads/mysql/
2. MySQL'i başlatın
3. Yeni bir veritabanı oluşturun:

```bash
mysql -u root -p
CREATE DATABASE kutuphane_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

## Adım 2: Proje Kurulumu

1. Proje klasörüne gidin:
```bash
cd veri_tabanı_proje
```

2. Virtual environment oluşturun (önerilir):
```bash
python -m venv venv
```

3. Virtual environment'ı aktifleştirin:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Adım 3: Veritabanı Kurulumu

1. `.env` dosyası oluşturun ve düzenleyin:
```env
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/kutuphane_db
JWT_SECRET_KEY=super-secret-key-change-in-production
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
FLASK_APP=run.py
FLASK_ENV=development
```

**ÖNEMLİ**: `DATABASE_URL` satırındaki `root:root` kısmını kendi MySQL kullanıcı adı ve şifrenizle değiştirin!

2. Veritabanı şemasını oluşturun:
```bash
mysql -u root -p kutuphane_db < database/schema.sql
```

## Adım 4: Uygulamayı Çalıştırma

1. Backend'i başlatın:
```bash
python run.py
```

Backend http://localhost:5001 adresinde çalışacaktır.

2. Frontend'i açın:
   - Tarayıcınızda `frontend/login.html` dosyasını açın
   - Veya bir web sunucusu kullanın (Live Server gibi)

## Adım 5: İlk Kullanıcı Oluşturma

### Yöntem 1: Frontend ile Kayıt
1. `frontend/register.html` sayfasına gidin
2. Yeni bir kullanıcı kaydı oluşturun
3. Admin yetkisi için veritabanında kullanıcının `role` alanını `admin` olarak güncelleyin

### Yöntem 2: Veritabanı ile
```sql
-- MySQL'de admin kullanıcı oluştur
-- Şifre: admin123 (hash'lenmiş hali gerekli, bu sadece örnek)
-- Gerçek uygulamada şifreyi hash'leyerek eklemelisiniz
```

### Yöntem 3: Python Script ile
```python
from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    admin = User(
        username='admin',
        email='admin@example.com',
        first_name='Admin',
        last_name='User',
        role='admin'
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
```

## Test

1. Postman veya başka bir API test aracı ile endpoint'leri test edin
2. Frontend'den giriş yapıp işlemleri test edin

## Sorun Giderme

### Veritabanı Bağlantı Hatası
- MySQL'in çalıştığından emin olun
- `.env` dosyasındaki `DATABASE_URL` değerini kontrol edin
- Veritabanı kullanıcı adı ve şifresinin doğru olduğundan emin olun
- MySQL'in UTF-8 karakter setini desteklediğinden emin olun (utf8mb4 önerilir)

### Import Hatası
- Virtual environment'ın aktif olduğundan emin olun
- Tüm paketlerin yüklendiğinden emin olun: `pip install -r requirements.txt`

### Port Kullanımda
- 5001 portu kullanılıyorsa `run.py` dosyasındaki port numarasını değiştirin

## Notlar

- Production ortamında mutlaka `JWT_SECRET_KEY` ve diğer hassas bilgileri güvenli tutun
- E-posta ayarları opsiyoneldir, geç iade bildirimleri için gerekli
- Gmail kullanıyorsanız "Uygulama Şifresi" oluşturmanız gerekebilir
- MySQL'de karakter seti olarak `utf8mb4` kullanılması önerilir (Türkçe karakter desteği için)

