// Onay bekleyen ödünç işlemlerini yükle
async function loadPendingLoans() {
    const container = document.getElementById('pendingLoansContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        const response = await apiCall('/loans/pending');
        
        if (!response.ok) {
            if (response.status === 403) {
                error.textContent = 'Bu sayfaya erişmek için admin yetkisi gereklidir.';
                error.style.display = 'block';
                loading.style.display = 'none';
                return;
            }
            throw new Error('Onay bekleyen ödünçler yüklenirken hata oluştu');
        }
        
        const loans = await response.json();
        displayPendingLoans(loans);
        loading.style.display = 'none';
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Hata: ' + err.message;
        error.style.display = 'block';
    }
}

// Onay bekleyen ödünç işlemlerini göster
function displayPendingLoans(loansList) {
    const container = document.getElementById('pendingLoansContainer');
    
    if (loansList.length === 0) {
        container.innerHTML = '<p>Onay bekleyen ödünç talebi bulunmamaktadır.</p>';
        return;
    }
    
    container.innerHTML = loansList.map(loan => {
        return `
            <div class="loan-item">
                <div class="loan-info">
                    <h3>${loan.book ? loan.book.title : 'Bilinmeyen Kitap'}</h3>
                    <p><strong>Yazar:</strong> ${loan.book && loan.book.author ? loan.book.author.full_name : 'Bilinmiyor'}</p>
                    <p><strong>Kullanıcı:</strong> ${loan.user ? `${loan.user.first_name} ${loan.user.last_name}` : 'Bilinmiyor'}</p>
                    <p><strong>E-posta:</strong> ${loan.user ? loan.user.email : 'Bilinmiyor'}</p>
                    <p><strong>Talep Tarihi:</strong> ${new Date(loan.created_at).toLocaleDateString('tr-TR')}</p>
                    <p><strong>Ödünç Alınacak Tarih:</strong> ${new Date(loan.loan_date).toLocaleDateString('tr-TR')}</p>
                    <p><strong>Vade Tarihi:</strong> ${new Date(loan.due_date).toLocaleDateString('tr-TR')}</p>
                </div>
                <div class="loan-status">
                    <span class="status-badge pending">Onay Bekliyor</span>
                    <div style="margin-top: 10px;">
                        <button class="btn btn-success" onclick="approveLoan(${loan.id})" style="margin-right: 10px;">
                            Onayla
                        </button>
                        <button class="btn btn-danger" onclick="rejectLoan(${loan.id})">
                            Reddet
                        </button>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// Ödünç işlemini onayla
async function approveLoan(loanId) {
    if (!confirm('Bu ödünç talebini onaylamak istediğinizden emin misiniz?')) {
        return;
    }
    
    try {
        const response = await apiCall(`/loans/${loanId}/approve`, {
            method: 'PUT'
        });
        
        if (response.ok) {
            alert('Ödünç talebi başarıyla onaylandı!');
            loadPendingLoans(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Onay işlemi başarısız'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

// Ödünç işlemini reddet
async function rejectLoan(loanId) {
    if (!confirm('Bu ödünç talebini reddetmek istediğinizden emin misiniz?')) {
        return;
    }
    
    try {
        const response = await apiCall(`/loans/${loanId}/reject`, {
            method: 'PUT'
        });
        
        if (response.ok) {
            alert('Ödünç talebi reddedildi!');
            loadPendingLoans(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Red işlemi başarısız'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

