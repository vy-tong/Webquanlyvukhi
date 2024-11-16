// Initialize DataTables
document.addEventListener('DOMContentLoaded', function() {
    const tables = document.querySelectorAll('.data-table');
    tables.forEach(table => {
        new DataTable(table, {
            language: {
                url: '/static/js/datatables-vi.json'
            },
            responsive: true,
            pageLength: 10
        });
    });
});

// Form validation
const validateForm = (formElement) => {
    const inputs = formElement.querySelectorAll('input[required]');
    let isValid = true;
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });
    return isValid;
};

// Sidebar controls
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}

// Dropdown toggle
function toggleDropdown() {
    var dropdownContent = document.querySelector(".dropdown-container");
    dropdownContent.style.display = dropdownContent.style.display === "none" ? "block" : "none";
}

// API handlers
const api = {
    async get(endpoint) {
        const response = await fetch(endpoint);
        return response.json();
    },
    
    async post(endpoint, data) {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
}; 