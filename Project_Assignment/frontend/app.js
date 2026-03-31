const API_BASE = '/api/v1';
let jwtToken = localStorage.getItem('jwt_token');
let userEmail = localStorage.getItem('user_email');

// Initial Load
document.addEventListener('DOMContentLoaded', () => {
    checkHealth();
    updateUIState();
    if (jwtToken) {
        loadRecords();
    }

    // Refresh every 30 seconds
    setInterval(checkHealth, 30000);
});

function updateUIState() {
    const authSection = document.getElementById('auth-section');
    const deploySection = document.getElementById('deploy-section');
    const userDisplay = document.getElementById('user-display');
    const logoutBtn = document.getElementById('logout-btn');
    const recordsList = document.getElementById('records-list');

    if (jwtToken) {
        authSection.style.display = 'none';
        deploySection.style.display = 'block';
        userDisplay.innerText = `User: ${userEmail}`;
        userDisplay.style.display = 'inline';
        logoutBtn.style.display = 'inline';
    } else {
        authSection.style.display = 'block';
        deploySection.style.display = 'none';
        userDisplay.style.display = 'none';
        logoutBtn.style.display = 'none';
        recordsList.innerHTML = '<div class="record-item" style="border: none; justify-content: center; color: var(--text-muted);"><p>Please log in to view items.</p></div>';
    }
}

function logout() {
    localStorage.removeItem('jwt_token');
    localStorage.removeItem('user_email');
    jwtToken = null;
    userEmail = null;
    updateUIState();
}

// Authentication Forms
document.getElementById('auth-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('login-btn');
    btn.innerText = 'Logging in...';
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    const formData = new URLSearchParams();
    formData.append('username', email); // OAuth2 expects username
    formData.append('password', password);

    try {
        const response = await fetch(`${API_BASE}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            jwtToken = data.access_token;
            userEmail = email;
            localStorage.setItem('jwt_token', jwtToken);
            localStorage.setItem('user_email', email);
            updateUIState();
            loadRecords();
        } else {
            alert('Authentication failed: Invalid credentials');
        }
    } catch(err) {
        alert('Authentication failed: Network error');
    } finally {
        btn.innerText = 'Log In';
    }
});

document.getElementById('register-btn').addEventListener('click', async () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    if(!email || !password) return alert('Enter email and password to register');

    try {
        const response = await fetch(`${API_BASE}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        if (response.ok) {
            alert('Registered successfully! You can now log in.');
        } else {
            const err = await response.json();
            alert(`Registration failed: ${err.detail}`);
        }
    } catch(err) {
        alert('Registration failed: Network error');
    }
});


// Check API Health
async function checkHealth() {
    const statusText = document.getElementById('status-text');
    const statusBadge = document.getElementById('api-status');

    try {
        const response = await fetch(`${API_BASE}/health`);
        if (response.ok) {
            statusBadge.style.color = '#00ff00';
            statusBadge.style.background = 'rgba(0, 255, 0, 0.1)';
            statusBadge.style.borderColor = 'rgba(0, 255, 0, 0.2)';
            statusText.innerText = 'Backend Online';
        } else {
            throw new Error();
        }
    } catch (error) {
        statusBadge.style.color = '#ff4444';
        statusBadge.style.background = 'rgba(255, 68, 68, 0.1)';
        statusBadge.style.borderColor = 'rgba(255, 68, 68, 0.2)';
        statusText.innerText = 'Backend Offline';
    }
}

// Load All Records
async function loadRecords() {
    if (!jwtToken) return;
    const recordsList = document.getElementById('records-list');
    
    try {
        const response = await fetch(`${API_BASE}/records`, {
            headers: { 'Authorization': `Bearer ${jwtToken}` }
        });

        if (response.status === 401) {
            logout();
            return;
        }

        const records = await response.json();
        
        if (records.length === 0) {
            recordsList.innerHTML = '<div class="record-item" style="border: none; justify-content: center; color: var(--text-muted);"><p>No items found.</p></div>';
            return;
        }

        recordsList.innerHTML = records.map(record => `
            <div class="record-item">
                <div class="record-info">
                    <h3>${record.name}</h3>
                    <p>${record.description}</p>
                </div>
                <div class="record-date">ID: ${record.id || 'X'}</div>
            </div>
        `).join('');
    } catch (error) {
        recordsList.innerHTML = '<div class="record-item" style="border: none; justify-content: center; color: #ff4444;"><p>Failed to connect to data stream.</p></div>';
    }
}

// Handle Form Submission
document.getElementById('record-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!jwtToken) return;
    
    const submitBtn = document.getElementById('submit-btn');
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;

    submitBtn.innerText = 'SAVING...';
    submitBtn.disabled = true;

    try {
        const response = await fetch(`${API_BASE}/records`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${jwtToken}`
            },
            body: JSON.stringify({ name, description })
        });

        if (response.ok) {
            document.getElementById('record-form').reset();
            await loadRecords();
            showNotification('Item saved successfully');
        } else if (response.status === 401) {
            logout();
        } else {
            alert('Failed to save item. Please try again.');
        }
    } catch (error) {
        alert('Network error: Could not save item.');
    } finally {
        submitBtn.innerText = 'Save Item';
        submitBtn.disabled = false;
    }
});

function showNotification(msg) {
    console.log(msg);
}
