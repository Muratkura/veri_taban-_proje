"""
Kullanıcı Repository
Kullanıcı veritabanı işlemlerini yönetir (CRUD işlemleri)
"""
from app import db
from app.models.user import User

class UserRepository:
    """
    Kullanıcı veritabanı işlemleri için repository sınıfı
    Tüm kullanıcı veritabanı işlemleri burada toplanmıştır
    """
    
    @staticmethod
    def find_by_id(user_id):
        """
        ID ile kullanıcı bulur
        
        Args:
            user_id (int): Aranacak kullanıcının ID'si
        
        Returns:
            User: Bulunan kullanıcı nesnesi, bulunamazsa None
        """
        return User.query.get(user_id)
    
    @staticmethod
    def find_by_username(username):
        """
        Kullanıcı adı ile kullanıcı bulur
        
        Args:
            username (str): Aranacak kullanıcı adı
        
        Returns:
            User: Bulunan kullanıcı nesnesi, bulunamazsa None
        """
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def find_by_email(email):
        """
        E-posta adresi ile kullanıcı bulur
        
        Args:
            email (str): Aranacak e-posta adresi
        
        Returns:
            User: Bulunan kullanıcı nesnesi, bulunamazsa None
        """
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def create(user_data):
        """
        Yeni kullanıcı oluşturur ve veritabanına kaydeder
        
        Args:
            user_data (dict): Kullanıcı bilgilerini içeren dictionary
                - username: Kullanıcı adı (zorunlu)
                - email: E-posta (zorunlu)
                - password: Şifre (zorunlu)
                - first_name: Ad (zorunlu)
                - last_name: Soyad (zorunlu)
                - role: Rol (opsiyonel, varsayılan: 'student')
                - phone: Telefon (opsiyonel)
                - address: Adres (opsiyonel)
        
        Returns:
            User: Oluşturulan kullanıcı nesnesi
        """
        # Yeni kullanıcı nesnesi oluştur
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            # get() metodu ile opsiyonel alanları al, yoksa varsayılan değer kullan
            role=user_data.get('role', 'student'),
            phone=user_data.get('phone'),
            address=user_data.get('address')
        )
        
        # Şifreyi hash'leyerek kaydet (güvenlik için)
        user.set_password(user_data['password'])
        
        # Veritabanına ekle ve kaydet
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update(user_id, user_data):
        """
        Kullanıcı bilgilerini günceller
        
        Args:
            user_id (int): Güncellenecek kullanıcının ID'si
            user_data (dict): Güncellenecek alanları içeren dictionary
                - first_name: Ad (opsiyonel)
                - last_name: Soyad (opsiyonel)
                - email: E-posta (opsiyonel)
                - phone: Telefon (opsiyonel)
                - address: Adres (opsiyonel)
                - password: Şifre (opsiyonel, hash'lenir)
        
        Returns:
            User: Güncellenmiş kullanıcı nesnesi, bulunamazsa None
        """
        # Kullanıcıyı bul
        user = UserRepository.find_by_id(user_id)
        if not user:
            return None
        
        # Sadece gönderilen alanları güncelle
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'phone' in user_data:
            user.phone = user_data['phone']
        if 'address' in user_data:
            user.address = user_data['address']
        # Şifre değişikliği varsa hash'le
        if 'password' in user_data:
            user.set_password(user_data['password'])
        
        # Değişiklikleri kaydet
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user_id):
        """
        Kullanıcıyı veritabanından siler
        
        Args:
            user_id (int): Silinecek kullanıcının ID'si
        
        Returns:
            bool: Silme işlemi başarılı ise True, kullanıcı bulunamazsa False
        """
        user = UserRepository.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_all():
        """
        Tüm kullanıcıları getirir
        
        Returns:
            list: Tüm kullanıcı nesnelerini içeren liste
        """
        return User.query.all()










