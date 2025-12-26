from app.repositories.loan_repository import LoanRepository, FineRepository
from app.repositories.book_repository import BookRepository
from app.repositories.user_repository import UserRepository
from app.services.email_service import EmailService
from datetime import date

class LoanService:
    @staticmethod
    def get_all_loans():
        """Tüm ödünç işlemlerini getir"""
        loans = LoanRepository.get_all()
        return [loan.to_dict(include_details=True) for loan in loans]
    
    @staticmethod
    def get_user_loans(user_id):
        """Kullanıcının ödünç işlemlerini getir"""
        loans = LoanRepository.get_by_user(user_id)
        return [loan.to_dict(include_details=True) for loan in loans]
    
    @staticmethod
    def get_active_loans(user_id=None):
        """Aktif ödünç işlemlerini getir"""
        loans = LoanRepository.get_active_loans(user_id)
        return [loan.to_dict(include_details=True) for loan in loans]
    
    @staticmethod
    def create_loan(loan_data, loan_days=14):
        """Yeni ödünç işlemi oluştur"""
        # Kitap kontrolü
        book = BookRepository.find_by_id(loan_data['book_id'])
        if not book:
            return None, "Kitap bulunamadı"
        
        if not book.is_available:
            return None, "Kitap şu anda müsait değil"
        
        # Kullanıcı kontrolü
        user = UserRepository.find_by_id(loan_data['user_id'])
        if not user:
            return None, "Kullanıcı bulunamadı"
        
        # Ödünç işlemi oluştur
        loan = LoanRepository.create(loan_data, loan_days)
        if not loan:
            return None, "Ödünç işlemi oluşturulamadı"
        
        return loan.to_dict(include_details=True), None
    
    @staticmethod
    def return_loan(loan_id):
        """Kitabı iade et"""
        loan = LoanRepository.find_by_id(loan_id)
        if not loan:
            return None, "Ödünç işlemi bulunamadı"
        
        if loan.status == 'returned':
            return None, "Bu kitap zaten iade edilmiş"
        
        # İade işlemi
        returned_loan = LoanRepository.return_loan(loan_id)
        if not returned_loan:
            return None, "İade işlemi gerçekleştirilemedi"
        
        # Eğer geç iade edildiyse, e-posta gönder (trigger ile ceza oluşturuldu)
        if returned_loan.return_date and returned_loan.due_date:
            if returned_loan.return_date > returned_loan.due_date:
                days_overdue = (returned_loan.return_date - returned_loan.due_date).days
                # E-posta gönder (asenkron olarak çalışabilir)
                try:
                    user = UserRepository.find_by_id(returned_loan.user_id)
                    EmailService.send_overdue_notification(user, returned_loan, days_overdue)
                except Exception as e:
                    print(f"E-posta gönderilemedi: {e}")
        
        return returned_loan.to_dict(include_details=True), None
    
    @staticmethod
    def check_overdue_loans():
        """Vadesi geçen kitapları kontrol et"""
        updated_count = LoanRepository.update_overdue_status()
        return updated_count
    
    @staticmethod
    def get_user_fines(user_id):
        """Kullanıcının cezalarını getir"""
        fines = FineRepository.get_by_user(user_id, paid=False)
        total = FineRepository.get_total_unpaid(user_id)
        
        return {
            'fines': [fine.to_dict() for fine in fines],
            'total_amount': total
        }


class FineService:
    @staticmethod
    def get_user_fines(user_id):
        """Kullanıcının cezalarını getir"""
        fines = FineRepository.get_by_user(user_id)
        total = FineRepository.get_total_unpaid(user_id)
        
        return {
            'fines': [fine.to_dict() for fine in fines],
            'total_unpaid': total
        }
    
    @staticmethod
    def pay_fine(fine_id):
        """Cezayı öde"""
        fine = FineRepository.mark_as_paid(fine_id)
        if not fine:
            return None, "Ceza bulunamadı"
        return fine.to_dict(), None




