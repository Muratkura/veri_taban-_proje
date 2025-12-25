from app import db
from app.models.loan import Loan, Fine
from app.models.book import Book
from datetime import date

class LoanRepository:
    @staticmethod
    def find_by_id(loan_id):
        """ID ile ödünç işlemi bul"""
        return Loan.query.get(loan_id)
    
    @staticmethod
    def get_all():
        """Tüm ödünç işlemlerini getir"""
        return Loan.query.order_by(Loan.loan_date.desc()).all()
    
    @staticmethod
    def get_by_user(user_id):
        """Kullanıcının ödünç işlemlerini getir"""
        return Loan.query.filter_by(user_id=user_id).order_by(Loan.loan_date.desc()).all()
    
    @staticmethod
    def get_active_loans(user_id=None):
        """Aktif ödünç işlemlerini getir"""
        query = Loan.query.filter(Loan.status == 'active')
        if user_id:
            query = query.filter(Loan.user_id == user_id)
        return query.all()
    
    @staticmethod
    def get_overdue_loans():
        """Vadesi geçmiş ödünç işlemlerini getir"""
        return Loan.query.filter(
            Loan.status == 'overdue',
            Loan.return_date.is_(None)
        ).all()
    
    @staticmethod
    def create(loan_data, loan_days=14):
        """Yeni ödünç işlemi oluştur"""
        # Kitabın müsait olduğunu kontrol et
        book = Book.query.get(loan_data['book_id'])
        if not book or book.available_copies <= 0:
            return None
        
        loan = Loan(
            user_id=loan_data['user_id'],
            book_id=loan_data['book_id'],
            loan_date=date.today(),
            due_date=Loan.calculate_due_date(loan_days),
            status='active'
        )
        
        db.session.add(loan)
        db.session.commit()
        return loan
    
    @staticmethod
    def return_loan(loan_id):
        """Kitabı iade et"""
        loan = LoanRepository.find_by_id(loan_id)
        if not loan or loan.status == 'returned':
            return None
        
        loan.status = 'returned'
        loan.return_date = date.today()
        
        db.session.commit()
        return loan
    
    @staticmethod
    def update_overdue_status():
        """Vadesi geçen kitapları güncelle"""
        today = date.today()
        loans = Loan.query.filter(
            Loan.status == 'active',
            Loan.due_date < today,
            Loan.return_date.is_(None)
        ).all()
        
        for loan in loans:
            loan.status = 'overdue'
        
        db.session.commit()
        return len(loans)


class FineRepository:
    @staticmethod
    def find_by_id(fine_id):
        """ID ile ceza bul"""
        return Fine.query.get(fine_id)
    
    @staticmethod
    def get_by_user(user_id, paid=None):
        """Kullanıcının cezalarını getir"""
        query = Fine.query.filter_by(user_id=user_id)
        if paid is not None:
            query = query.filter_by(paid=paid)
        return query.all()
    
    @staticmethod
    def get_by_loan(loan_id):
        """Ödünç işlemine ait cezaları getir"""
        return Fine.query.filter_by(loan_id=loan_id).all()
    
    @staticmethod
    def get_total_unpaid(user_id):
        """Kullanıcının toplam ödenmemiş cezası"""
        from sqlalchemy import func
        result = db.session.query(func.sum(Fine.amount)).filter(
            Fine.user_id == user_id,
            Fine.paid == False
        ).scalar()
        return float(result) if result else 0.00
    
    @staticmethod
    def mark_as_paid(fine_id):
        """Cezayı ödendi olarak işaretle"""
        fine = FineRepository.find_by_id(fine_id)
        if fine:
            fine.mark_as_paid()
            db.session.commit()
            return fine
        return None



