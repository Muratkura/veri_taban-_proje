from app.repositories.book_repository import BookRepository, AuthorRepository, CategoryRepository
from app.repositories.loan_repository import LoanRepository, FineRepository
from app.repositories.user_repository import UserRepository

class AdminRepository:
    """Admin işlemleri için repository"""
    
    @staticmethod
    def get_statistics():
        """Sistem istatistiklerini getir"""
        from app import db
        from app.models.book import Book
        from app.models.loan import Loan, Fine
        from sqlalchemy import func
        
        stats = {
            'total_books': Book.query.count(),
            'total_loans': Loan.query.count(),
            'active_loans': Loan.query.filter_by(status='active').count(),
            'overdue_loans': Loan.query.filter_by(status='overdue').count(),
            'total_fines': float(db.session.query(func.sum(Fine.amount))
                                .filter(Fine.paid == False).scalar() or 0),
            'total_users': len(UserRepository.get_all())
        }
        
        return stats

