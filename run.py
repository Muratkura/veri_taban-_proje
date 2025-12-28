"""
Flask uygulamasının giriş noktası
Bu dosya uygulamayı başlatır ve çalıştırır
"""
from app import create_app

# Flask uygulamasını oluştur
app = create_app()

# Eğer bu dosya doğrudan çalıştırılıyorsa (python run.py gibi)
if __name__ == '__main__':
    # Uygulamayı debug modunda çalıştır
    # host='0.0.0.0': Tüm ağ arayüzlerinden erişilebilir
    # port=5001: Uygulama 5001 portunda çalışacak
    app.run(debug=True, host='0.0.0.0', port=5001)


