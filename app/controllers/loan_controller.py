from flask import Blueprint, request, jsonify
from app.services.loan_service import LoanService
from flask_jwt_extended import jwt_required, get_jwt_identity

loan_bp = Blueprint('loans', __name__)

@loan_bp.route('', methods=['GET'])
@jwt_required()
def get_loans():
    """Ödünç işlemlerini listele"""
    try:
        current_user_id = get_jwt_identity()
        # Admin ise tüm işlemleri, değilse sadece kendi işlemlerini getir
        from app.repositories.user_repository import UserRepository
        user = UserRepository.find_by_id(current_user_id)
        
        if user and user.is_admin():
            loans = LoanService.get_all_loans()
        else:
            loans = LoanService.get_user_loans(current_user_id)
        
        return jsonify(loans), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@loan_bp.route('/active', methods=['GET'])
@jwt_required()
def get_active_loans():
    """Aktif ödünç işlemlerini listele"""
    try:
        current_user_id = get_jwt_identity()
        loans = LoanService.get_active_loans(current_user_id)
        return jsonify(loans), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@loan_bp.route('', methods=['POST'])
@jwt_required()
def create_loan():
    """Kitap ödünç al"""
    try:
        data = request.get_json()
        current_user_id = get_jwt_identity()
        
        # Kullanıcı ID'sini set et
        data['user_id'] = current_user_id
        
        # Ödünç günü sayısı (varsayılan 14)
        loan_days = data.get('loan_days', 14)
        
        loan, error = LoanService.create_loan(data, loan_days)
        
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Kitap başarıyla ödünç alındı',
            'loan': loan
        }), 201
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@loan_bp.route('/<int:loan_id>/return', methods=['PUT'])
@jwt_required()
def return_loan(loan_id):
    """Kitap iade et"""
    try:
        current_user_id = get_jwt_identity()
        
        # Kullanıcının kendi ödüncü mü kontrol et
        from app.repositories.loan_repository import LoanRepository
        loan = LoanRepository.find_by_id(loan_id)
        if loan and loan.user_id != current_user_id:
            from app.repositories.user_repository import UserRepository
            user = UserRepository.find_by_id(current_user_id)
            if not user or not user.is_admin():
                return jsonify({'message': 'Bu işlemi yapmaya yetkiniz yok'}), 403
        
        returned_loan, error = LoanService.return_loan(loan_id)
        
        if error:
            return jsonify({'message': error}), 400
        
        return jsonify({
            'message': 'Kitap başarıyla iade edildi',
            'loan': returned_loan
        }), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500

@loan_bp.route('/fines', methods=['GET'])
@jwt_required()
def get_fines():
    """Kullanıcının cezalarını getir"""
    try:
        current_user_id = get_jwt_identity()
        fines_data = LoanService.get_user_fines(current_user_id)
        
        return jsonify(fines_data), 200
    except Exception as e:
        return jsonify({'message': f'Hata: {str(e)}'}), 500



