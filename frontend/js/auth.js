// API Base URL
const API_BASE_URL = 'http://localhost:5001/api';

// Token ve kullanıcı bilgilerini al
function getToken() {
    return localStorage.getItem('token');
}

function getUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}

// API çağrısı yap (token ile)
async function apiCall(url, options = {}) {
    const token = getToken();
    
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers
    };
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    const response = await fetch(`${API_BASE_URL}${url}`, {
        ...options,
        headers
    });
    
    // Token geçersizse çıkış yap
    if (response.status === 401) {
        logout();
        throw new Error('Oturum süresi doldu');
    }
    
    return response;
}

// Çıkış yap
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = 'login.html';
}

// Kullanıcı bilgilerini göster
function displayUserInfo() {
    const user = getUser();
    const userInfoEl = document.getElementById('userInfo');
    const logoutBtn = document.getElementById('logoutBtn');
    
    if (user && userInfoEl) {
        userInfoEl.textContent = `Hoş geldiniz, ${user.first_name} ${user.last_name}`;
    }
    
    if (logoutBtn) {
        logoutBtn.style.display = 'inline-block';
        logoutBtn.addEventListener('click', logout);
    }
}

// Sayfa yüklendiğinde kontrol et
function checkAuth() {
    const token = getToken();
    const currentPage = window.location.pathname.split('/').pop();
    
    // Login ve register sayfaları hariç token kontrolü yap
    if (currentPage !== 'login.html' && currentPage !== 'register.html' && !token) {
        window.location.href = 'login.html';
        return false;
    }
    
    // Login sayfasındaysa ve token varsa ana sayfaya yönlendir
    if ((currentPage === 'login.html' || currentPage === 'register.html') && token) {
        window.location.href = 'index.html';
        return false;
    }
    
    return true;
}


