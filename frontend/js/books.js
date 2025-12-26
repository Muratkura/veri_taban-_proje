let books = [];

// Kitapları yükle
async function loadBooks() {
    const container = document.getElementById('booksContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        const response = await apiCall('/books');
        books = await response.json();
        
        displayBooks(books);
        loading.style.display = 'none';
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Kitaplar yüklenirken hata oluştu: ' + err.message;
        error.style.display = 'block';
    }
}

// Kitapları göster
function displayBooks(booksList) {
    const container = document.getElementById('booksContainer');
    
    if (booksList.length === 0) {
        container.innerHTML = '<p>Kitap bulunamadı.</p>';
        return;
    }
    
    container.innerHTML = booksList.map(book => `
        <div class="book-card">
            <h3>${book.title}</h3>
            <p class="author">Yazar: ${book.author ? book.author.full_name : 'Bilinmiyor'}</p>
            <p>Kategori: ${book.category ? book.category.name : 'Bilinmiyor'}</p>
            <p>ISBN: ${book.isbn || 'Yok'}</p>
            <p>Müsait Kopya: ${book.available_copies} / ${book.total_copies}</p>
            <span class="status ${book.is_available ? 'available' : 'unavailable'}">
                ${book.is_available ? 'Müsait' : 'Müsait Değil'}
            </span>
            ${book.is_available ? `
                <button class="btn btn-success" style="margin-top: 10px; width: 100%;" 
                        onclick="borrowBook(${book.id})">
                    Ödünç Al
                </button>
            ` : ''}
        </div>
    `).join('');
}

// Kitap ara
async function searchBooks(query) {
    const container = document.getElementById('booksContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        const response = await apiCall(`/books?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        
        displayBooks(results);
        loading.style.display = 'none';
    } catch (err) {
        loading.style.display = 'none';
        error.textContent = 'Arama yapılırken hata oluştu: ' + err.message;
        error.style.display = 'block';
    }
}

// Kitap ödünç al
async function borrowBook(bookId) {
    if (!confirm('Bu kitabı ödünç almak istediğinizden emin misiniz?')) {
        return;
    }
    
    try {
        const response = await apiCall('/loans', {
            method: 'POST',
            body: JSON.stringify({
                book_id: bookId,
                loan_days: 14
            })
        });
        
        if (response.ok) {
            alert('Kitap başarıyla ödünç alındı!');
            loadBooks(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Ödünç alma işlemi başarısız'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

// Arama butonu event listener
document.addEventListener('DOMContentLoaded', () => {
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    
    if (searchBtn) {
        searchBtn.addEventListener('click', () => {
            const query = searchInput.value.trim();
            if (query) {
                searchBooks(query);
            } else {
                loadBooks();
            }
        });
    }
    
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const query = searchInput.value.trim();
                if (query) {
                    searchBooks(query);
                } else {
                    loadBooks();
                }
            }
        });
    }
    
    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', () => {
            searchInput.value = '';
            loadBooks();
        });
    }
});




