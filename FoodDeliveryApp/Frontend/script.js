// script.js
const API_URL = 'http://127.0.0.1:8000';

async function fetchRestaurants() {
    try {
        const response = await fetch(`${API_URL}/restaurants/`);
        const data = await response.json();
        
        const grid = document.getElementById('restaurant-list');
        if (!grid) return;
        
        grid.innerHTML = data.map(r => `
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">${r.restaurant_name}</h3>
                    <p class="card-text">Cuisine: ${r.cuisine}</p>
                    <p class="card-text">Rating: ⭐️ ${r.rating}</p>
                    <button class="btn-primary" onclick="viewMenu('${r.restaurant_name}')">View Menu</button>
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error fetching restaurants:', error);
    }
}

function viewMenu(restaurantName) {
    // Redirect or fetch menu (simplified for now)
    alert(`View menu for ${restaurantName}`);
}

function searchFood() {
    const query = document.getElementById('search-input').value;
    alert(`Searching for: ${query}`);
}

// Load data on page load
document.addEventListener('DOMContentLoaded', () => {
    fetchRestaurants();
});
