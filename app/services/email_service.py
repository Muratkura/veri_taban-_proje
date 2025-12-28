from flask_mail import Message
from app import mail

class EmailService:
    @staticmethod
    def send_overdue_notification(user, loan, days_overdue):
        """Geç iade bildirimi gönder"""
        try:
            subject = f"Geç İade Bildirimi - {loan.book.title}"
            body = f"""
Sayın {user.first_name} {user.last_name},

{loan.book.title} adlı kitabı {days_overdue} gün geç iade ettiğiniz için 
sistemimize ceza kaydı eklenmiştir.

Ödünç Alınan Tarih: {loan.loan_date}
Vade Tarihi: {loan.due_date}
İade Tarihi: {loan.return_date}
Gecikme Süresi: {days_overdue} gün
Hesaplanan Ceza: {days_overdue * 5.00} TL

Lütfen cezanızı kütüphane müdürlüğüne ödeyiniz.

Saygılarımızla,
Kütüphane Yönetim Sistemi
            """
            
            msg = Message(
                subject=subject,
                recipients=[user.email],
                body=body
            )
            
            mail.send(msg)
            return True
        except Exception as e:
            print(f"E-posta gönderilirken hata: {e}")
            return False
    
    @staticmethod
    def send_loan_reminder(user, loan, days_until_due):
        """Vade yaklaşıyor bildirimi gönder"""
        try:
            subject = f"Vade Yaklaşıyor - {loan.book.title}"
            body = f"""
Sayın {user.first_name} {user.last_name},

{loan.book.title} adlı kitabın vade tarihi {days_until_due} gün sonra.
Lütfen zamanında iade ediniz.

Vade Tarihi: {loan.due_date}

Saygılarımızla,
Kütüphane Yönetim Sistemi
            """
            
            msg = Message(
                subject=subject,
                recipients=[user.email],
                body=body
            )
            
            mail.send(msg)
            return True
        except Exception as e:
            print(f"E-posta gönderilirken hata: {e}")
            return False











