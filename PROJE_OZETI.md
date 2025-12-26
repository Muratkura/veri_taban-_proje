# Kütüphane Yönetim Sistemi - Proje Özeti

## Proje Hakkında

Bu proje, kütüphane işlemlerini otomatikleştiren modern bir web uygulamasıdır. Flask (Python) backend ve HTML/CSS/JavaScript frontend kullanılarak, katmanlı mimari prensiplerine uygun olarak geliştirilmiştir.

## Tamamlanan Özellikler

### 1. Kimlik Doğrulama ve Yetkilendirme
- ✅ JWT tabanlı kullanıcı kaydı ve girişi
- ✅ Token tabanlı kimlik doğrulama
- ✅ Rol tabanlı yetkilendirme (admin, student, staff)
- ✅ Güvenli şifre hash'leme

### 2. Kitap Yönetimi
- ✅ Kitap listeleme ve arama
- ✅ Kitap detay görüntüleme
- ✅ Kitap ekleme, güncelleme, silme (Admin)
- ✅ Yazar ve kategori yönetimi

### 3. Ödünç İşlemleri
- ✅ Kitap ödünç alma talebi oluşturma
- ✅ **Admin onay sistemi** (yeni özellik)
- ✅ Ödünç taleplerini onaylama/reddetme (Admin)
- ✅ Kitap iade etme
- ✅ Ödünç geçmişi görüntüleme
- ✅ Vade takibi

### 4. Ceza Sistemi
- ✅ Geç iade cezası otomatik hesaplama (Trigger)
- ✅ Ceza listeleme
- ✅ Ceza ödeme takibi

### 5. Admin Paneli
- ✅ Ödünç taleplerini onaylama/reddetme
- ✅ Kullanıcı yönetimi (listeleme, güncelleme, silme)
- ✅ Yazar ve kategori yönetimi
- ✅ Sistem istatistikleri

### 6. Veritabanı Özellikleri
- ✅ Trigger'lar:
  - Otomatik ceza hesaplama
  - Kopya sayısı güncelleme (onaylandığında)
  - Vadesi geçen kitapları işaretleme
- ✅ Stored Procedure'lar:
  - Sistem istatistikleri
  - Kullanıcı ceza hesaplama
  - Vadesi geçen kitapları güncelleme
- ✅ İlişkisel veritabanı tasarımı
- ✅ Index'ler (performans optimizasyonu)

### 7. E-posta Bildirimleri
- ✅ Geç iade bildirimleri (hazır)
- ✅ Vade yaklaşma bildirimleri (hazır)

## Teknolojiler

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

## Mimari

Proje katmanlı mimari prensibine uygun olarak geliştirilmiştir:

1. **Model/Entity Katmanı**: Veritabanı modelleri (SQLAlchemy)
2. **Repository Katmanı**: Veritabanı işlemleri (CRUD)
3. **Service Katmanı**: İş mantığı
4. **Controller Katmanı**: API endpoints (REST)

## Veritabanı Şeması

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

## Güvenlik

- ✅ JWT token tabanlı kimlik doğrulama
- ✅ Şifreler Werkzeug ile hash'leniyor
- ✅ Rol tabanlı yetkilendirme
- ✅ CORS desteği
- ✅ SQL injection koruması (SQLAlchemy ORM)

## Geliştirme Notları

- Tüm endpoint'ler RESTful API standartlarına uygun
- Hata yönetimi ve validasyon yapılmış
- Frontend ve backend ayrı çalışabilir
- Kod yapısı temiz ve bakımı kolay

## İyileştirme Önerileri

1. **Güvenlik**
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
   - Admin dashboard grafikleri

4. **Test**
   - Unit testler
   - Integration testler
   - E2E testler

## Lisans

Bu proje eğitim amaçlıdır.
