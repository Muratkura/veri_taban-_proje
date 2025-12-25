@echo off
echo ========================================
echo Kutuphane Yonetim Sistemi - Hizli Baslangic
echo ========================================
echo.

echo [1/3] Python paketleri yukleniyor...
python -m pip install -r requirements.txt
echo.

echo [2/3] .env dosyasi kontrol ediliyor...
if not exist .env (
    echo .env dosyasi bulunamadi, olusturuluyor...
    (
        echo DATABASE_URL=mysql+pymysql://root:root@localhost:3306/kutuphane_db
        echo JWT_SECRET_KEY=super-secret-key-change-in-production-12345
        echo MAIL_SERVER=smtp.gmail.com
        echo MAIL_PORT=587
        echo MAIL_USE_TLS=True
        echo MAIL_USERNAME=
        echo MAIL_PASSWORD=
        echo FLASK_APP=run.py
        echo FLASK_ENV=development
    ) > .env
    echo .env dosyasi olusturuldu!
    echo ONEMLI: .env dosyasinda DATABASE_URL'deki sifreyi kendi MySQL sifrenizle degistirin!
) else (
    echo .env dosyasi mevcut.
)
echo.

echo [3/3] Backend baslatiliyor...
echo.
echo Backend http://localhost:5001 adresinde calisacak
echo Tarayicida frontend/login.html dosyasini acin
echo.
echo Cikmak icin Ctrl+C basin
echo.

python run.py

pause


