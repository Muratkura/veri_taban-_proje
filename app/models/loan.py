from app import db
from datetime import datetime, date, timedelta

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    loan_date = db.Column(db.Date, nullable=False, default=date.today)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # İlişkiler
    fines = db.relationship('Fine', backref='loan', lazy=True, cascade='all, delete-orphan')
    
    @staticmethod
    def calculate_due_date(loan_days=14):
        """Vade tarihini hesapla (varsayılan 14 gün)"""
        return date.today() + timedelta(days=loan_days)
    
    @property
    def is_overdue(self):
        """Vadesi geçmiş mi?"""
        if self.status == 'returned':
            return False
        return self.due_date < date.today()
    
    @property
    def days_overdue(self):
        """Gecikme günü sayısı"""
        if not self.is_overdue:
            return 0
        return (date.today() - self.due_date).days
    
    def to_dict(self, include_details=False):
        """Model'i dictionary'ye çevir"""
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'loan_date': self.loan_date.isoformat() if self.loan_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'status': self.status,
            'is_overdue': self.is_overdue,
            'days_overdue': self.days_overdue,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        
        if include_details:
            data['book'] = self.book.to_dict() if self.book else None
            data['user'] = self.user.to_dict() if self.user else None
        
        return data
    
    def __repr__(self):
        return f'<Loan {self.id}>'


class Fine(db.Model):
    __tablename__ = 'fines'
    
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    reason = db.Column(db.String(255), nullable=False)
    paid = db.Column(db.Boolean, default=False)
    paid_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def mark_as_paid(self):
        """Ceza ödemesini işaretle"""
        self.paid = True
        self.paid_date = date.today()
    
    def to_dict(self):
        """Model'i dictionary'ye çevir"""
        return {
            'id': self.id,
            'loan_id': self.loan_id,
            'user_id': self.user_id,
            'amount': float(self.amount) if self.amount else 0.00,
            'reason': self.reason,
            'paid': self.paid,
            'paid_date': self.paid_date.isoformat() if self.paid_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
    
    def __repr__(self):
        return f'<Fine {self.id} - {self.amount} TL>'




