"""
Ödünç (Loan) ve Ceza (Fine) modelleri
Kütüphane ödünç işlemlerini ve cezaları temsil eder
"""
from app import db
from datetime import datetime, date, timedelta

class Loan(db.Model):
    """
    Ödünç işlemi modeli
    Kullanıcıların kitapları ödünç almasını temsil eder
    """
    __tablename__ = 'loans'
    
    # Birincil anahtar: Benzersiz ödünç işlemi kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Kullanıcı ID'si: Hangi kullanıcı ödünç alıyor (Foreign Key)
    # Kullanıcı silinirse ödünç kaydı da silinir (CASCADE)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Kitap ID'si: Hangi kitap ödünç alınıyor (Foreign Key)
    # Kitap silinirse ödünç kaydı da silinir (CASCADE)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    
    # Ödünç alınma tarihi: Varsayılan olarak bugünün tarihi
    loan_date = db.Column(db.Date, nullable=False, default=date.today)
    
    # Vade tarihi: Kitabın iade edilmesi gereken son tarih
    due_date = db.Column(db.Date, nullable=False)
    
    # İade tarihi: Kitabın gerçekte iade edildiği tarih (iade edilmediyse NULL)
    return_date = db.Column(db.Date)
    
    # İşlem durumu: pending, active, returned, overdue, rejected
    status = db.Column(db.String(20), default='pending')
    
    # Onay durumu: pending (beklemede), approved (onaylandı), rejected (reddedildi)
    approval_status = db.Column(db.String(20), default='pending')
    
    # Oluşturulma tarihi: Otomatik olarak eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Güncelleme tarihi: Her güncellemede otomatik olarak güncellenir
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # İlişkiler (Relationships)
    # Bu ödünç işlemine ait cezalar: Ödünç silinirse cezalar da silinir
    fines = db.relationship('Fine', backref='loan', lazy=True, cascade='all, delete-orphan')
    
    @staticmethod
    def calculate_due_date(loan_days=14):
        """
        Vade tarihini hesaplar (bugünden itibaren belirtilen gün sayısı kadar ileri)
        
        Args:
            loan_days (int): Ödünç süresi (gün cinsinden), varsayılan 14 gün
        
        Returns:
            date: Hesaplanan vade tarihi
        """
        return date.today() + timedelta(days=loan_days)
    
    @property
    def is_overdue(self):
        """
        Ödünç işleminin vadesinin geçip geçmediğini kontrol eder
        
        Returns:
            bool: Vade geçmişse True, geçmemişse veya iade edilmişse False
        """
        # Eğer zaten iade edilmişse vadesi geçmiş sayılmaz
        if self.status == 'returned':
            return False
        # Vade tarihi bugünden önceyse vadesi geçmiş demektir
        return self.due_date < date.today()
    
    @property
    def days_overdue(self):
        """
        Gecikme günü sayısını hesaplar
        
        Returns:
            int: Gecikme günü sayısı (gecikme yoksa 0)
        """
        if not self.is_overdue:
            return 0
        # Bugün ile vade tarihi arasındaki fark
        return (date.today() - self.due_date).days
    
    def to_dict(self, include_details=False):
        """
        Ödünç işlemi modelini dictionary formatına çevirir
        
        Args:
            include_details (bool): Detaylı bilgileri (kitap, kullanıcı) dahil etmek için True
        
        Returns:
            dict: Ödünç işlemi bilgilerini içeren dictionary
        """
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'loan_date': self.loan_date.isoformat() if self.loan_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'status': self.status,
            'approval_status': self.approval_status,
            'is_overdue': self.is_overdue,
            'days_overdue': self.days_overdue,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        
        # Detaylı bilgi isteniyorsa kitap ve kullanıcı bilgilerini ekle
        if include_details:
            data['book'] = self.book.to_dict() if self.book else None
            data['user'] = self.user.to_dict() if self.user else None
        
        return data
    
    def __repr__(self):
        """
        Ödünç işlemi nesnesinin string temsilini döndürür
        
        Returns:
            str: Ödünç işlemi ID'sini içeren string
        """
        return f'<Loan {self.id}>'


class Fine(db.Model):
    """
    Ceza modeli
    Kullanıcıların geç iade veya diğer nedenlerden dolayı aldığı cezaları temsil eder
    """
    __tablename__ = 'fines'
    
    # Birincil anahtar: Benzersiz ceza kimliği
    id = db.Column(db.Integer, primary_key=True)
    
    # Ödünç işlemi ID'si: Hangi ödünç işleminden kaynaklanıyor (Foreign Key)
    # Ödünç silinirse ceza da silinir (CASCADE)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id', ondelete='CASCADE'), nullable=False)
    
    # Kullanıcı ID'si: Hangi kullanıcıya ait (Foreign Key)
    # Kullanıcı silinirse ceza da silinir (CASCADE)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Ceza miktarı: Decimal formatında (toplam 10 basamak, 2 ondalık)
    amount = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    
    # Ceza nedeni: Neden ceza verildiği açıklaması
    reason = db.Column(db.String(255), nullable=False)
    
    # Ödeme durumu: Ceza ödendi mi?
    paid = db.Column(db.Boolean, default=False)
    
    # Ödeme tarihi: Ceza ödendiğinde tarih eklenir
    paid_date = db.Column(db.Date)
    
    # Oluşturulma tarihi: Otomatik olarak eklenir
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def mark_as_paid(self):
        """
        Ceza ödemesini işaretler
        Ödeme tarihini bugünün tarihi olarak ayarlar
        """
        self.paid = True
        self.paid_date = date.today()
    
    def to_dict(self):
        """
        Ceza modelini dictionary formatına çevirir
        
        Returns:
            dict: Ceza bilgilerini içeren dictionary
        """
        return {
            'id': self.id,
            'loan_id': self.loan_id,
            'user_id': self.user_id,
            # Decimal tipini float'a çevir
            'amount': float(self.amount) if self.amount else 0.00,
            'reason': self.reason,
            'paid': self.paid,
            'paid_date': self.paid_date.isoformat() if self.paid_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        """
        Ceza nesnesinin string temsilini döndürür
        
        Returns:
            str: Ceza ID'si ve miktarını içeren string
        """
        return f'<Fine {self.id} - {self.amount} TL>'






