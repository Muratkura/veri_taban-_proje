// Ödünç işlemlerini yükle
async function loadLoans() {
    const container = document.getElementById('loansContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        const response = await apiCall('/loans');
        const loans = await response.json();
        
        displayLoans(loans);
        loading.style.display = 'none';
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Ödünçler yüklenirken hata oluştu: ' + err.message;
        error.style.display = 'block';
    }
}

// Ödünç işlemlerini göster
function displayLoans(loansList) {
    const container = document.getElementById('loansContainer');
    
    if (loansList.length === 0) {
        container.innerHTML = '<p>Ödünç aldığınız kitap bulunmamaktadır.</p>';
        return;
    }
    
    container.innerHTML = loansList.map(loan => {
        const statusClass = loan.status === 'active' ? 'active' : 
                          loan.status === 'overdue' ? 'overdue' : 'returned';
        const statusText = loan.status === 'active' ? 'Aktif' : 
                          loan.status === 'overdue' ? 'Vadesi Geçmiş' : 'İade Edildi';
        
        return `
            <div class="loan-item">
                <div class="loan-info">
                    <h3>${loan.book ? loan.book.title : 'Bilinmeyen Kitap'}</h3>
                    <p><strong>Yazar:</strong> ${loan.book && loan.book.author ? loan.book.author.full_name : 'Bilinmiyor'}</p>
                    <p><strong>Ödünç Alınan Tarih:</strong> ${new Date(loan.loan_date).toLocaleDateString('tr-TR')}</p>
                    <p><strong>Vade Tarihi:</strong> ${new Date(loan.due_date).toLocaleDateString('tr-TR')}</p>
                    ${loan.return_date ? `<p><strong>İade Tarihi:</strong> ${new Date(loan.return_date).toLocaleDateString('tr-TR')}</p>` : ''}
                    ${loan.days_overdue > 0 ? `<p style="color: #e74c3c;"><strong>Gecikme:</strong> ${loan.days_overdue} gün</p>` : ''}
                </div>
                <div class="loan-status">
                    <span class="status-badge ${statusClass}">${statusText}</span>
                    ${loan.status === 'active' ? `
                        <button class="btn btn-success" onclick="returnLoan(${loan.id})">
                            İade Et
                        </button>
                    ` : ''}
                </div>
            </div>
        `;
    }).join('');
}

// Kitap iade et
async function returnLoan(loanId) {
    if (!confirm('Bu kitabı iade etmek istediğinizden emin misiniz?')) {
        return;
    }
    
    try {
        const response = await apiCall(`/loans/${loanId}/return`, {
            method: 'PUT'
        });
        
        if (response.ok) {
            alert('Kitap başarıyla iade edildi!');
            loadLoans(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'İade işlemi başarısız'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}




