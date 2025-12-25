# 🚀 Basit Kurulum - Adım Adım

## 1️⃣ MySQL Veritabanı Hazırlama

### MySQL Kurulu Değilse:
1. İndirin: https://dev.mysql.com/downloads/mysql/
2. Kurulum sırasında root kullanıcısı için şifre belirleyin (örnek: `root`)
3. MySQL Workbench veya komut satırını kullanabilirsiniz

### Veritabanı Oluşturma:

**Yöntem A: MySQL Workbench ile (Görsel Arayüz)**
1. MySQL Workbench'i açın
2. Local instance'a bağlanın (root şifrenizi girin)
3. Sol tarafta "Schemas" bölümüne sağ tıklayın
4. "Create Schema" seçin
5. Schema name: `kutuphane_db` yazın
6. Default Collation: `utf8mb4_unicode_ci` seçin
7. "Apply" butonuna tıklayın

**Yöntem B: Komut Satırı ile**
```bash
# CMD veya PowerShell'de
mysql -u root -p
```
Şifrenizi girdikten sonra:
```sql
CREATE DATABASE kutuphane_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### Veritabanı Şemasını Yükleme:

**Yöntem A: MySQL Workbench ile**
1. `kutuphane_db` veritabanını seçin (çift tıklayın)
2. "File" > "Open SQL Script" seçin
3. `database/schema.sql` dosyasını açın
4. "Execute" (⚡) butonuna tıklayın

**Yöntem B: Komut Satırı ile**
```bash
mysql -u root -p kutuphane_db < database\schema.sql
```

---

## 2️⃣ .env Dosyasını Düzenleme

1. Proje klasöründe `.env` dosyasını açın (Notepad++ veya VS Code ile)
2. **ÖNEMLİ**: İlk satırdaki şifreyi değiştirin:

```env
DATABASE_URL=mysql+pymysql://root:SIFRENIZ@localhost:3306/kutuphane_db
```

`SIFRENIZ` yerine MySQL kurulumunda belirlediğiniz root şifresini yazın!

Örnek: Eğer şifreniz `123456` ise:
```env
DATABASE_URL=mysql+pymysql://root:123456@localhost:3306/kutuphane_db
```

---

## 3️⃣ Python Paketlerini Yükleme

PowerShell veya CMD'de proje klasöründe:

```bash
pip install -r requirements.txt
```

Eğer hata alırsanız:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 4️⃣ Backend'i Başlatma

```bash
python run.py
```

Başarılı olduysa şunu göreceksiniz:
```
 * Running on http://127.0.0.1:5001
```

**Bu pencereyi açık tutun!** Backend çalışırken kapamayın.

---

## 5️⃣ Frontend'i Açma

### En Kolay Yöntem:
1. Windows Dosya Gezgini'nde `frontend` klasörüne gidin
2. `login.html` dosyasına **çift tıklayın**
3. Tarayıcıda açılacak!

### Alternatif (VS Code ile):
1. VS Code'da `frontend/login.html` dosyasını açın
2. Sağ tıklayın
3. "Open with Live Server" seçin (Live Server eklentisi gerekli)

---

## 6️⃣ İlk Kullanıcı Oluşturma

1. Tarayıcıda açılan `login.html` sayfasında **"Kayıt Ol"** linkine tıklayın
2. Formu doldurun:
   - Kullanıcı adı
   - E-posta
   - Ad, Soyad
   - Şifre
3. **"Kayıt Ol"** butonuna tıklayın
4. Giriş sayfasına yönlendirileceksiniz
5. Oluşturduğunuz kullanıcı adı ve şifre ile giriş yapın

---

## ✅ Tamamlandı!

Artık projeniz çalışıyor! 🎉

### Yapabilecekleriniz:
- ✅ Kitap listesini görüntüleme
- ✅ Kitap arama
- ✅ Kitap ödünç alma
- ✅ Kitap iade etme
- ✅ Ceza görüntüleme

---

## 🔧 Sorun mu Yaşıyorsunuz?

### Backend çalışmıyor:
- MySQL'in çalıştığından emin olun (Başlat > Servisler > MySQL80 veya MySQL)
- `.env` dosyasındaki şifrenin doğru olduğundan emin olun
- Port 5001 kullanımda mı kontrol edin

### "ModuleNotFoundError" hatası:
```bash
pip install -r requirements.txt
```

### Veritabanı bağlantı hatası:
- `.env` dosyasındaki `DATABASE_URL`'yi kontrol edin
- MySQL servisinin çalıştığından emin olun
- MySQL kullanıcı adı ve şifresinin doğru olduğundan emin olun

### Frontend API'ye bağlanamıyor:
- Backend'in çalıştığından emin olun (adım 4)
- Tarayıcı konsolunda (F12) hataları kontrol edin

---

## 📝 Önemli Notlar

1. **Backend her zaman çalışıyor olmalı** - Terminal penceresini kapatmayın
2. **MySQL servisi çalışıyor olmalı** - Windows Servisler'den kontrol edin
3. **E-posta ayarları opsiyonel** - Sadece geç iade bildirimleri için gerekli
4. **MySQL karakter seti** - `utf8mb4` kullanılması Türkçe karakter desteği için önemlidir

Başarılar! 🚀

