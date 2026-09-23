const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const loginView = document.getElementById('login-view');
const dashboardView = document.getElementById('dashboard-view');
const errorMsg = document.getElementById('login-error');

const API_URL = 'http://localhost:5000/api';

loginBtn.addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if(!username || !password) {
        errorMsg.textContent = "Please fill in all fields.";
        return;
    }

    loginBtn.textContent = 'Verifying...';
    errorMsg.textContent = '';

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            // Login success
            loginView.classList.remove('active');
            dashboardView.classList.add('active');
            // Clear inputs
            document.getElementById('password').value = '';
        } else {
            // Login failed
            errorMsg.textContent = data.message || 'Login failed.';
        }
    } catch (err) {
        console.error(err);
        errorMsg.textContent = 'Could not connect to the backend server. Is Python running?';
    } finally {
        loginBtn.textContent = 'Login';
    }
});

logoutBtn.addEventListener('click', () => {
    dashboardView.classList.remove('active');
    loginView.classList.add('active');
    document.getElementById('password').value = '';
});

// Menu Cards Navigation
document.querySelectorAll('.menu-card').forEach(card => {
    card.addEventListener('click', () => {
        // Find the target view ID based on the menu card's ID
        // e.g., 'menu-customer' -> 'customer-view'
        const viewId = card.id.replace('menu-', '') + '-view';
        const targetView = document.getElementById(viewId);
        
        if (targetView) {
            dashboardView.classList.remove('active');
            targetView.classList.add('active');
            
            // Firing data fetches based on view opened
            if(viewId === 'customer-view') {
                fetchCustomers();
            } else if (viewId === 'room-view') {
                fetchRooms();
            } else if (viewId === 'details-view') {
                fetchDetails();
            } else if (viewId === 'payment-view') {
                fetchPayments();
            }
        }
    });
});

async function fetchCustomers() {
    const tbody = document.querySelector('#customer-table tbody');
    tbody.innerHTML = '<tr><td colspan="11">Loading customers...</td></tr>';
    try {
        const response = await fetch(`${API_URL}/customers`);
        const data = await response.json();
        
        if(data.success) {
            tbody.innerHTML = '';
            data.data.forEach(cust => {
                tbody.innerHTML += `
                    <tr>
                        <td>${cust.ref || ''}</td>
                        <td>${cust.Name || ''}</td>
                        <td>${cust.mother || ''}</td>
                        <td>${cust.gender || ''}</td>
                        <td>${cust.PostCode || ''}</td>
                        <td>${cust.Mobile || ''}</td>
                        <td>${cust.Email || ''}</td>
                        <td>${cust.Nationality || ''}</td>
                        <td>${cust.Idproof || ''}</td>
                        <td>${cust.Idnumber || ''}</td>
                        <td>${cust.Address || ''}</td>
                    </tr>
                `;
            });
        } else {
            tbody.innerHTML = `<tr><td colspan="11" style="color:var(--error)">${data.message}</td></tr>`;
        }
    } catch(err) {
        tbody.innerHTML = `<tr><td colspan="11" style="color:var(--error)">Error fetching data.</td></tr>`;
    }
}

async function fetchRooms() {
    const tbody = document.querySelector('#room-table tbody');
    tbody.innerHTML = '<tr><td colspan="7">Loading rooms...</td></tr>';
    try {
        const response = await fetch(`${API_URL}/rooms`);
        const data = await response.json();
        
        if(data.success) {
            tbody.innerHTML = '';
            data.data.forEach(room => {
                tbody.innerHTML += `
                    <tr>
                        <td>${room.Contact || ''}</td>
                        <td>${room.check_in || ''}</td>
                        <td>${room.check_out || ''}</td>
                        <td>${room.roomtype || ''}</td>
                        <td>${room.roomavailable || ''}</td>
                        <td>${room.meal || ''}</td>
                        <td>${room.noOfdays || ''}</td>
                    </tr>
                `;
            });
        } else {
            tbody.innerHTML = `<tr><td colspan="7" style="color:var(--error)">${data.message}</td></tr>`;
        }
    } catch(err) {
        tbody.innerHTML = `<tr><td colspan="7" style="color:var(--error)">Error fetching data.</td></tr>`;
    }
}

// Back Buttons Navigation
document.querySelectorAll('.back-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Find the closest view and hide it
        const currentView = e.target.closest('.view');
        if (currentView) {
            currentView.classList.remove('active');
        }
        // Show dashboard
        dashboardView.classList.add('active');
    });
});

// --- CUSTOMER LOGIC ---
const addCustomerForm = document.getElementById('add-customer-form');
if(addCustomerForm) {
    addCustomerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
            ref: document.getElementById('cust-ref').value,
            Name: document.getElementById('cust-name').value,
            mother: document.getElementById('cust-mother').value,
            gender: document.getElementById('cust-gender').value,
            PostCode: document.getElementById('cust-postcode').value,
            Mobile: document.getElementById('cust-mobile').value,
            Email: document.getElementById('cust-email').value,
            Nationality: document.getElementById('cust-nationality').value,
            Idproof: document.getElementById('cust-idproof').value,
            Idnumber: document.getElementById('cust-idnumber').value,
            Address: document.getElementById('cust-address').value
        };

        try {
            const resp = await fetch(`${API_URL}/customers`, {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(payload)
            });
            const data = await resp.json();
            if(data.success) {
                alert(data.message);
                addCustomerForm.reset();
                fetchCustomers(); // Refresh table
            } else {
                alert(data.message);
            }
        } catch(err) {
            alert("Error adding customer.");
        }
    });
}

// --- DETAILS LOGIC ---
async function fetchDetails() {
    const tbody = document.querySelector('#details-table tbody');
    tbody.innerHTML = '<tr><td colspan="3">Loading details...</td></tr>';
    try {
        const response = await fetch(`${API_URL}/details`);
        const data = await response.json();
        
        if(data.success) {
            tbody.innerHTML = '';
            data.data.forEach(room => {
                tbody.innerHTML += `
                    <tr>
                        <td>${room.Floor || ''}</td>
                        <td>${room.RoomNo || ''}</td>
                        <td>${room.RoomType || ''}</td>
                    </tr>
                `;
            });
        }
    } catch(err) {
        tbody.innerHTML = `<tr><td colspan="3" style="color:var(--error)">Error fetching data.</td></tr>`;
    }
}

// --- PAYMENT LOGIC ---
const fetchBillBtn = document.getElementById('btn-fetch-bill');
if(fetchBillBtn) {
    fetchBillBtn.addEventListener('click', async () => {
        const contact = document.getElementById('pay-contact').value;
        if(!contact) return alert("Enter contact first!");

        fetchBillBtn.textContent = "...";
        try {
            const resp = await fetch(`${API_URL}/payment/calculate`, {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({contact})
            });
            const data = await resp.json();
            if(data.success) {
                document.getElementById('pay-name').value = data.data.name;
                document.getElementById('pay-roomno').value = data.data.roomno;
                document.getElementById('pay-total').value = "Rs." + data.data.total;
                document.getElementById('pay-amount').value = data.data.total; // Default full pay
            } else {
                alert(data.message);
            }
        } catch(err) {
            alert("Connection error.");
        } finally {
            fetchBillBtn.textContent = "Fetch";
        }
    });
}

const paymentForm = document.getElementById('payment-form');
if(paymentForm) {
    paymentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const payload = {
            contact: document.getElementById('pay-contact').value,
            name: document.getElementById('pay-name').value,
            roomno: document.getElementById('pay-roomno').value,
            total_amount: document.getElementById('pay-total').value,
            method: document.getElementById('pay-method').value,
            amount_paid: document.getElementById('pay-amount').value
        };

        if(!payload.name) return alert("Please fetch bill first!");

        try {
            const resp = await fetch(`${API_URL}/payment`, {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(payload)
            });
            const data = await resp.json();
            if(data.success) {
                alert("Payment saved successfully!");
                paymentForm.reset();
                fetchPayments(); // refresh table
            } else {
                alert(data.message);
            }
        } catch(err) {
            alert("Error saving payment.");
        }
    });
}

async function fetchPayments() {
    const tbody = document.querySelector('#payment-table tbody');
    tbody.innerHTML = '<tr><td colspan="7">Loading...</td></tr>';
    try {
        const response = await fetch(`${API_URL}/payments`);
        const data = await response.json();
        
        if(data.success) {
            tbody.innerHTML = '';
            data.data.forEach(pay => {
                tbody.innerHTML += `
                    <tr>
                        <td>${pay.contact || ''}</td>
                        <td>${pay.name || ''}</td>
                        <td>${pay.roomno || ''}</td>
                        <td>${pay.total_amount || ''}</td>
                        <td>${pay.method || ''}</td>
                        <td>${pay.amount_paid || ''}</td>
                        <td>${pay.date || ''}</td>
                    </tr>
                `;
            });
        }
    } catch(err) {
        tbody.innerHTML = `<tr><td colspan="7" style="color:var(--error)">Error fetching logic</td></tr>`;
    }
}
