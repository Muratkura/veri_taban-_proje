// Ana sayfa yüklendiğinde
document.addEventListener('DOMContentLoaded', () => {
    // Kimlik doğrulama kontrolü
    if (!checkAuth()) {
        return;
    }
    
    // Kullanıcı bilgilerini göster
    displayUserInfo();
    
    // Admin navigasyonunu göster/gizle
    updateAdminNavigation();
    
    // Admin butonlarını güncelle (varsa)
    if (typeof updateAddBookButton === 'function') {
        updateAddBookButton();
    }
    
    // Sayfa bazlı işlemler
    const currentPage = window.location.pathname.split('/').pop();
    
    if (currentPage === 'index.html' || currentPage === '') {
        // Ana sayfa - kitapları yükle
        loadBooks();
    } else if (currentPage === 'loans.html') {
        // Ödünçler sayfası
        loadLoans();
    } else if (currentPage === 'fines.html') {
        // Cezalar sayfası
        loadFines();
    } else if (currentPage === 'admin-approvals.html') {
        // Admin onay sayfası
        loadPendingLoans();
    }
});

// Admin navigasyonunu güncelle
function updateAdminNavigation() {
    const user = getUser();
    const navLinks = document.querySelectorAll('.nav-links');
    
    if (user && user.role === 'admin') {
        navLinks.forEach(nav => {
            // Admin onay linkini kontrol et, yoksa ekle
            let adminLink = nav.querySelector('a[href="admin-approvals.html"]');
            if (!adminLink) {
                // Mevcut linklerden sonra ekle
                const loansLink = nav.querySelector('a[href="loans.html"]');
                if (loansLink) {
                    adminLink = document.createElement('a');
                    adminLink.href = 'admin-approvals.html';
                    adminLink.textContent = 'Onay Bekleyenler';
                    adminLink.className = window.location.pathname.includes('admin-approvals.html') ? 'active' : '';
                    loansLink.parentNode.insertBefore(adminLink, loansLink.nextSibling);
                }
            }
        });
    } else {
        // Admin değilse admin linkini kaldır
        navLinks.forEach(nav => {
            const adminLink = nav.querySelector('a[href="admin-approvals.html"]');
            if (adminLink) {
                adminLink.remove();
            }
        });
    }
}






