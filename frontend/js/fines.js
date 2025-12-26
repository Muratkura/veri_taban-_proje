// Cezaları yükle
async function loadFines() {
    const container = document.getElementById('finesContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    const totalFineEl = document.getElementById('totalFine');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        const response = await apiCall('/loans/fines');
        const data = await response.json();
        
        if (totalFineEl) {
            totalFineEl.textContent = data.total_amount.toFixed(2);
        }
        
        displayFines(data.fines || []);
        loading.style.display = 'none';
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Cezalar yüklenirken hata oluştu: ' + err.message;
        error.style.display = 'block';
    }
}

// Cezaları göster
function displayFines(finesList) {
    const container = document.getElementById('finesContainer');
    
    if (finesList.length === 0) {
        container.innerHTML = '<p>Ceza kaydınız bulunmamaktadır.</p>';
        return;
    }
    
    container.innerHTML = finesList.map(fine => `
        <div class="fine-item">
            <div class="fine-info">
                <h3>${fine.reason}</h3>
                <p><strong>Oluşturulma Tarihi:</strong> ${new Date(fine.created_at).toLocaleDateString('tr-TR')}</p>
                ${fine.paid_date ? `<p><strong>Ödenme Tarihi:</strong> ${new Date(fine.paid_date).toLocaleDateString('tr-TR')}</p>` : ''}
            </div>
            <div>
                ${fine.paid ? 
                    '<span class="paid-badge">Ödendi</span>' : 
                    `<span class="fine-amount">${fine.amount.toFixed(2)} TL</span>`
                }
            </div>
        </div>
    `).join('');
}




