from app import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def find_by_id(user_id):
        """ID ile kullanıcı bul"""
        return User.query.get(user_id)
    
    @staticmethod
    def find_by_username(username):
        """Kullanıcı adı ile kullanıcı bul"""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def find_by_email(email):
        """E-posta ile kullanıcı bul"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def create(user_data):
        """Yeni kullanıcı oluştur"""
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            role=user_data.get('role', 'student'),
            phone=user_data.get('phone'),
            address=user_data.get('address')
        )
        user.set_password(user_data['password'])
        
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update(user_id, user_data):
        """Kullanıcı bilgilerini güncelle"""
        user = UserRepository.find_by_id(user_id)
        if not user:
            return None
        
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
        if 'password' in user_data:
            user.set_password(user_data['password'])
        
        db.session.commit()
        return user
    
    @staticmethod
    def delete(user_id):
        """Kullanıcıyı sil"""
        user = UserRepository.find_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_all():
        """Tüm kullanıcıları getir"""
        return User.query.all()










