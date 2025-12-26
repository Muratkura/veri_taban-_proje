// Ana sayfa yüklendiğinde
document.addEventListener('DOMContentLoaded', () => {
    // Kimlik doğrulama kontrolü
    if (!checkAuth()) {
        return;
    }
    
    // Kullanıcı bilgilerini göster
    displayUserInfo();
    
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
    }
});




