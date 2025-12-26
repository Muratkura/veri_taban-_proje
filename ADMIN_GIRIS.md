# Admin Girişi Kılavuzu

## Admin Girişi Nasıl Yapılır?

Admin girişi yapmak için **normal login sayfasını** kullanırsınız. Sistem otomatik olarak admin yetkilerini kontrol eder.

### Adımlar:

1. **Backend'in çalıştığından emin olun**
   ```bash
   python run.py
   ```

2. **Tarayıcıda login sayfasını açın**
   - `frontend/login.html` dosyasını açın
   - Veya Live Server kullanıyorsanız: `http://localhost:8000/login.html`

3. **Admin kullanıcı adı ve şifresi ile giriş yapın**
   - Eğer admin kullanıcınız yoksa, aşağıdaki yöntemlerden biriyle oluşturun

4. **Giriş yaptıktan sonra:**
   - Admin iseniz, menüde **"Onay Bekleyenler"** linki görünecek
   - Bu sayfadan ödünç taleplerini onaylayabilir/reddedebilirsiniz

---

## Admin Kullanıcı Nasıl Oluşturulur?

### Yöntem 1: Python Script ile (Önerilen) ⭐

En kolay yöntem:

```bash
python create_admin.py
```

Script size şunları soracak:
- Kullanıcı Adı
- E-posta
- Ad, Soyad
- Şifre

Örnek:
```
Kullanıcı Adı: admin
E-posta: admin@kutuphane.com
Ad: Admin
Soyad: User
Şifre: admin123
```

### Yöntem 2: Normal Kullanıcı Olarak Kayıt + Veritabanında Güncelleme

1. **Önce normal kullanıcı olarak kayıt olun:**
   - `frontend/register.html` sayfasına gidin
   - Yeni bir hesap oluşturun

2. **Veritabanında rolü admin yapın:**
   ```bash
   mysql -u root -p kutuphane_db
   ```
   
   ```sql
   -- Tüm kullanıcıları görmek için
   SELECT id, username, email, role FROM users;
   
   -- Belirli bir kullanıcıyı admin yapmak için (id veya username ile)
   UPDATE users SET role = 'admin' WHERE username = 'kullanici_adi';
   -- veya
   UPDATE users SET role = 'admin' WHERE id = 1;
   
   -- Çıkış
   EXIT;
   ```

### Yöntem 3: Doğrudan SQL ile Admin Kullanıcı Oluşturma

⚠️ **Dikkat:** Bu yöntem şifreyi hash'lemeniz gerektiği için önerilmez. Python script kullanın.

```sql
-- Şifre hash'lenmiş olmalı (örnek: 'admin123' için)
-- Python script kullanarak oluşturmanız önerilir
```

---

## Admin Yetkileri

Admin kullanıcılar şunları yapabilir:

1. ✅ **Ödünç taleplerini onaylama/reddetme**
   - `admin-approvals.html` sayfasından
   - Veya API: `PUT /api/loans/<id>/approve` ve `PUT /api/loans/<id>/reject`

2. ✅ **Tüm ödünç işlemlerini görüntüleme**
   - Normal kullanıcılar sadece kendi ödünçlerini görür
   - Adminler tüm ödünçleri görür

3. ✅ **Kullanıcı yönetimi**
   - `GET /api/admin/users` - Tüm kullanıcıları listele
   - `PUT /api/admin/users/<id>` - Kullanıcı güncelle
   - `DELETE /api/admin/users/<id>` - Kullanıcı sil

4. ✅ **Kitap, yazar, kategori yönetimi**
   - Admin panelinden yönetim yapabilir

---

## Sorun Giderme

### "Admin yetkisi gerekli" hatası alıyorum

1. Kullanıcınızın `role` alanının `admin` olduğundan emin olun:
   ```sql
   SELECT username, role FROM users WHERE username = 'kullanici_adi';
   ```

2. Çıkış yapıp tekrar giriş yapın (token yenilenmesi için)

3. Tarayıcı cache'ini temizleyin

### "Onay Bekleyenler" linki görünmüyor

1. Kullanıcınızın admin olduğundan emin olun
2. Sayfayı yenileyin (F5)
3. Tarayıcı konsolunda hata var mı kontrol edin (F12)

### Admin kullanıcı oluşturamıyorum

1. Veritabanı bağlantısının çalıştığından emin olun
2. `.env` dosyasındaki `DATABASE_URL` değerini kontrol edin
3. MySQL'in çalıştığından emin olun

---

## Hızlı Test

Admin girişini test etmek için:

1. Admin kullanıcı oluşturun: `python create_admin.py`
2. Backend'i başlatın: `python run.py`
3. `frontend/login.html` sayfasını açın
4. Admin bilgileriyle giriş yapın
5. Menüde "Onay Bekleyenler" linkini kontrol edin

---

## Örnek Admin Kullanıcı Bilgileri

Test için kullanabileceğiniz örnek admin:
- **Kullanıcı Adı:** `admin`
- **Şifre:** `admin123`
- **E-posta:** `admin@kutuphane.com`

⚠️ **Güvenlik Uyarısı:** Production ortamında mutlaka güçlü şifreler kullanın!

