# 🚀 Projeyi Çalıştırma Kılavuzu

## Hızlı Başlangıç (Adım Adım)

### Adım 1: MySQL Kurulumu ve Veritabanı Oluşturma

1. **MySQL'i indirin ve kurun** (Eğer kurulu değilse):
   - https://dev.mysql.com/downloads/mysql/
   - Kurulum sırasında root kullanıcısı için bir şifre belirleyin (örn: `root`)

2. **MySQL'i başlatın** (Genellikle otomatik başlar)

3. **Komut satırından veritabanı oluşturun**:
   ```bash
   # PowerShell veya CMD'yi açın
   mysql -u root -p
   ```
   
   MySQL'e giriş yaptıktan sonra (şifrenizi girin):
   ```sql
   CREATE DATABASE kutuphane_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   EXIT;
   ```

### Adım 2: Python Paketlerini Yükleme

1. **Proje klasörüne gidin**:
   ```bash
   cd C:\Users\hp\Desktop\veri_tabanı_proje
   ```

2. **Gerekli paketleri yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

   Eğer hata alırsanız:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

### Adım 3: Ortam Değişkenlerini Ayarlama (.env dosyası)

1. **Proje klasöründe `.env` dosyası oluşturun** (Not: Dosya adı `.env` olmalı, başında nokta var!)

   Windows'ta oluşturma:
   ```powershell
   # PowerShell'de
   New-Item -Path .env -ItemType File
   ```
   
   Veya Notepad++ veya VS Code ile oluşturun.

2. **`.env` dosyasına şu içeriği ekleyin**:
   ```env
   DATABASE_URL=mysql+pymysql://root:root@localhost:3306/kutuphane_db
   JWT_SECRET_KEY=super-secret-key-change-in-production-12345
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=
   MAIL_PASSWORD=
   FLASK_APP=run.py
   FLASK_ENV=development
   ```

   **ÖNEMLİ**: `DATABASE_URL` satırındaki `root:root` kısmını kendi MySQL kullanıcı adı ve şifrenizle değiştirin!
   - Format: `mysql+pymysql://kullanici_adi:sifre@localhost:3306/kutuphane_db`

### Adım 4: Veritabanı Şemasını Oluşturma

1. **SQL şemasını çalıştırın**:
   ```bash
   mysql -u root -p kutuphane_db < database\schema.sql
   ```

   Şifre isterse, MySQL root şifrenizi girin.

   Eğer hata alırsanız, tam yol belirtin:
   ```bash
   mysql -u root -p kutuphane_db < "C:\Users\hp\Desktop\veri_tabanı_proje\database\schema.sql"
   ```

2. **(Opsiyonel) Örnek verileri yükleyin**:
   ```bash
   mysql -u root -p kutuphane_db < database\init_sample_data.sql
   ```

### Adım 5: Backend'i Başlatma

1. **Backend sunucusunu başlatın**:
   ```bash
   python run.py
   ```

2. **Başarılı olduysa şunu göreceksiniz**:
   ```
   * Running on http://127.0.0.1:5001
   * Running on http://0.0.0.0:5001
   ```

   Backend artık çalışıyor! 🎉

### Adım 6: Frontend'i Açma

**Yöntem 1: Doğrudan tarayıcıda açma (Basit)**
1. Dosya gezgininde `frontend` klasörüne gidin
2. `login.html` dosyasına çift tıklayın
3. Tarayıcıda açılacaktır

**Yöntem 2: Live Server kullanma (Önerilen)**
- VS Code'da "Live Server" eklentisini yükleyin
- `login.html` dosyasına sağ tıklayıp "Open with Live Server" seçin

**Yöntem 3: Python HTTP Server**
```bash
# frontend klasörüne gidin
cd frontend
python -m http.server 8000
# Tarayıcıda http://localhost:8000/login.html açın
```

## İlk Kullanıcı Oluşturma

1. **Tarayıcıda** `login.html` sayfasını açın
2. **"Kayıt Ol"** linkine tıklayın
3. **Yeni bir hesap oluşturun**:
   - Kullanıcı adı
   - E-posta
   - Ad, Soyad
   - Şifre
4. **Giriş yapın**

### Admin Yetkisi Verme (Opsiyonel)

Admin olmak için veritabanında kullanıcı rolünü güncelleyin:

```bash
mysql -u root -p kutuphane_db
```

```sql
-- Kullanıcıları görmek için
SELECT id, username, email, role FROM users;

-- Belirli bir kullanıcıyı admin yapmak için (id numarasını değiştirin)
UPDATE users SET role = 'admin' WHERE id = 1;

-- Çıkış
EXIT;
```

## Sorun Giderme

### ❌ "ModuleNotFoundError" hatası alıyorsanız:
```bash
pip install -r requirements.txt
```

### ❌ Veritabanı bağlantı hatası:
- MySQL'in çalıştığından emin olun (Servisler'e bakın)
- `.env` dosyasındaki `DATABASE_URL`'yi kontrol edin
- Kullanıcı adı ve şifrenin doğru olduğundan emin olun
- MySQL'in UTF-8 karakter setini desteklediğinden emin olun

### ❌ Port 5001 kullanımda:
`run.py` dosyasını açın ve port numarasını değiştirin:
```python
app.run(debug=True, host='0.0.0.0', port=5002)  # 5001 yerine 5002
```

### ❌ CORS hatası alıyorsanız:
Backend'in çalıştığından emin olun. Frontend JavaScript'te API URL'ini kontrol edin:
`frontend/js/auth.js` dosyasında `API_BASE_URL` değişkenini kontrol edin.

### ❌ "mysql: command not found":
MySQL'in PATH'e eklenmemiş olabilir. Tam yolu kullanın:
```bash
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

### ❌ "Access denied for user" hatası:
- MySQL root şifresinin doğru olduğundan emin olun
- `.env` dosyasındaki `DATABASE_URL`'deki şifreyi kontrol edin

## Test Etme

1. **Backend API Testi**:
   Tarayıcıda açın: http://localhost:5001/
   Şunu görmelisiniz: `{"message": "Kütüphane Yönetim Sistemi API", "version": "1.0"}`

2. **Frontend Testi**:
   - Kayıt ol
   - Giriş yap
   - Kitapları görüntüle
   - Kitap ödünç al

## Notlar

- Backend ve Frontend ayrı çalışır
- Backend her zaman çalışıyor olmalı (port 5001)
- Frontend sadece HTML dosyaları, herhangi bir web sunucusuyla açılabilir
- E-posta ayarları opsiyoneldir (geç iade bildirimleri için)
- MySQL'de `utf8mb4` karakter seti kullanılması Türkçe karakter desteği için önemlidir

## Başarılar! 🎉

Projeniz çalışıyor olmalı. Sorun yaşarsanız hata mesajını paylaşın, yardımcı olayım!

