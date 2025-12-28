let books = [];
let categories = [];
let selectedCategoryId = null;

// Kategorileri yükle
async function loadCategories() {
    try {
        const response = await apiCall('/books/categories');
        categories = await response.json();
        
        const categoryFilter = document.getElementById('categoryFilter');
        const bookCategory = document.getElementById('bookCategory');
        
        // Filtre dropdown'ını doldur
        if (categoryFilter) {
            categoryFilter.innerHTML = '<option value="">Tüm Kategoriler</option>';
            categories.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat.id;
                option.textContent = cat.name;
                categoryFilter.appendChild(option);
            });
        }
        
        // Kitap ekleme formundaki kategori dropdown'ını doldur
        if (bookCategory) {
            bookCategory.innerHTML = '<option value="">Kategori Seçin</option>';
            categories.forEach(cat => {
                const option = document.createElement('option');
                option.value = cat.id;
                option.textContent = cat.name;
                bookCategory.appendChild(option);
            });
        }
    } catch (err) {
        console.error('Kategoriler yüklenirken hata:', err);
    }
}

// Kitapları yükle
async function loadBooks() {
    const container = document.getElementById('booksContainer');
    const loading = document.getElementById('loadingMessage');
    const error = document.getElementById('errorMessage');
    
    try {
        loading.style.display = 'block';
        error.style.display = 'none';
        
        // Kategori filtresi varsa kategori parametresi ekle
        let url = '/books';
        const categoryFilter = document.getElementById('categoryFilter');
        if (categoryFilter && categoryFilter.value) {
            url += `?category_id=${categoryFilter.value}`;
            selectedCategoryId = categoryFilter.value;
        }
        
        const response = await apiCall(url);
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
    
    // Kullanıcının admin olup olmadığını kontrol et
    const user = getUser();
    const isAdmin = user && user.role === 'admin';
    
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
            <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
                ${book.is_available ? `
                    <button class="btn btn-success" style="width: 100%;" 
                            onclick="borrowBook(${book.id})">
                        📖 Ödünç Al
                    </button>
                ` : ''}
                ${isAdmin ? `
                    <button class="btn btn-danger" style="width: 100%;" 
                            onclick="deleteBook(${book.id}, '${book.title.replace(/'/g, "\\'")}')">
                        🗑️ Sil
                    </button>
                ` : ''}
            </div>
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
            const data = await response.json();
            alert(data.message || 'Ödünç talebi oluşturuldu. Admin onayı bekleniyor.');
            loadBooks(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Ödünç alma işlemi başarısız'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

// Kitap sil (Admin)
async function deleteBook(bookId, bookTitle) {
    // Onay mesajı göster
    if (!confirm(`"${bookTitle}" adlı kitabı silmek istediğinizden emin misiniz?\n\nBu işlem geri alınamaz!`)) {
        return;
    }
    
    // Çift onay (güvenlik için)
    if (!confirm('Son bir kez onaylıyor musunuz? Kitap kalıcı olarak silinecektir.')) {
        return;
    }
    
    try {
        const response = await apiCall(`/books/${bookId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            const data = await response.json();
            alert(data.message || 'Kitap başarıyla silindi.');
            loadBooks(); // Liste güncellensin
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Kitap silinemedi'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

// Kategoriye göre filtreleme
function filterByCategory() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.value = ''; // Arama terimini temizle
    }
    loadBooks();
}

// Kitap ekleme modal'ını aç
function openAddBookModal() {
    const modal = document.getElementById('addBookModal');
    if (modal) {
        modal.style.display = 'block';
        loadCategories(); // Kategorileri tekrar yükle
    }
}

// Kitap ekleme modal'ını kapat
function closeAddBookModal() {
    const modal = document.getElementById('addBookModal');
    if (modal) {
        modal.style.display = 'none';
        document.getElementById('addBookForm').reset();
    }
}

// Yeni kitap ekle
async function addBook(event) {
    event.preventDefault();
    
    // Form verilerini al
    const title = document.getElementById('bookTitle').value;
    const isbn = document.getElementById('bookIsbn').value;
    const authorFirstName = document.getElementById('authorFirstName').value;
    const authorLastName = document.getElementById('authorLastName').value;
    const categoryId = parseInt(document.getElementById('bookCategory').value);
    const publisher = document.getElementById('bookPublisher').value;
    const publicationDate = document.getElementById('bookPublicationDate').value;
    const totalCopies = parseInt(document.getElementById('bookTotalCopies').value);
    const description = document.getElementById('bookDescription').value;
    
    try {
        // Önce yazarı oluştur veya mevcut yazarı bul
        let authorId = null;
        
        try {
            // Yazar oluşturmayı dene
            const authorResponse = await apiCall('/admin/authors', {
                method: 'POST',
                body: JSON.stringify({
                    first_name: authorFirstName,
                    last_name: authorLastName
                })
            });
            
            if (authorResponse.ok) {
                const authorData = await authorResponse.json();
                authorId = authorData.author.id;
            } else {
                // Yazar zaten var olabilir, hata mesajı göster
                const errorData = await authorResponse.json();
                if (errorData.message && errorData.message.includes('zaten')) {
                    // Yazar zaten varsa, tüm yazarları al ve eşleşen yazarı bul
                    const allAuthorsResponse = await apiCall('/admin/authors');
                    if (allAuthorsResponse.ok) {
                        const allAuthors = await allAuthorsResponse.json();
                        const existingAuthor = allAuthors.find(a => 
                            a.first_name.toLowerCase() === authorFirstName.toLowerCase() && 
                            a.last_name.toLowerCase() === authorLastName.toLowerCase()
                        );
                        if (existingAuthor) {
                            authorId = existingAuthor.id;
                        } else {
                            alert('Yazar bulunamadı ve oluşturulamadı: ' + errorData.message);
                            return;
                        }
                    } else {
                        alert('Yazarlar listelenirken hata oluştu: ' + errorData.message);
                        return;
                    }
                } else {
                    alert('Yazar oluşturulamadı: ' + errorData.message);
                    return;
                }
            }
        } catch (err) {
            alert('Yazar işlemi sırasında hata: ' + err.message);
            return;
        }
        
        // Kitap verilerini hazırla
        const bookData = {
            title: title,
            isbn: isbn || null,
            author_id: authorId,
            category_id: categoryId,
            publisher: publisher || null,
            publication_date: publicationDate || null,
            total_copies: totalCopies,
            description: description || null
        };
        
        // Kitabı oluştur
        const response = await apiCall('/books', {
            method: 'POST',
            body: JSON.stringify(bookData)
        });
        
        if (response.ok) {
            const data = await response.json();
            alert(data.message || 'Kitap başarıyla eklendi!');
            closeAddBookModal();
            loadBooks(); // Listeyi güncelle
        } else {
            const data = await response.json();
            alert('Hata: ' + (data.message || 'Kitap eklenemedi'));
        }
    } catch (err) {
        alert('Hata: ' + err.message);
    }
}

// Admin butonunu göster/gizle
function updateAddBookButton() {
    const user = getUser();
    const addBookBtn = document.getElementById('addBookBtn');
    
    if (addBookBtn) {
        if (user && user.role === 'admin') {
            addBookBtn.style.display = 'block';
        } else {
            addBookBtn.style.display = 'none';
        }
    }
}

// Arama butonu event listener
document.addEventListener('DOMContentLoaded', () => {
    // Kategorileri yükle
    loadCategories();
    
    // Admin butonunu güncelle
    updateAddBookButton();
    
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    const categoryFilter = document.getElementById('categoryFilter');
    
    // Kategori filtresi değiştiğinde
    if (categoryFilter) {
        categoryFilter.addEventListener('change', filterByCategory);
    }
    
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
            if (categoryFilter) {
                categoryFilter.value = '';
            }
            loadBooks();
        });
    }
});






