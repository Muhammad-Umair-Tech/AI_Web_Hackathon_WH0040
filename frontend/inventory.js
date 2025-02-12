const API_URL = "http://localhost:3000";

// Function to add an item
async function addItem() {
    let name = document.getElementById("itemName").value;
    let quantity = document.getElementById("itemQuantity").value;

    if (!name || !quantity || !expiry) {
        alert("Please fill all fields.");
        return;
    }

    let response = await fetch(`${API_URL}/add-item`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, quantity})
    });

    let result = await response.json();
    alert(result.message);
    fetchItems();
}

// Function to remove an item
async function removeItem() {
    let name = document.getElementById("removeName").value;

    if (!name) {
        alert("Enter an item name to remove.");
        return;
    }

    let response = await fetch(`${API_URL}/remove-item/${name}`, {
        method: "DELETE"
    });

    let result = await response.json();
    alert(result.message);
    fetchItems();
}

// Function to fetch and display items
async function fetchItems() {
    let response = await fetch(`${API_URL}/items`);
    let items = await response.json();
    
    let inventoryList = document.getElementById("inventoryList");
    inventoryList.innerHTML = "";

    items.forEach(item => {
        let card = `<div class="item-card">
            <h3>${item.name}</h3>
            <p>Quantity: ${item.quantity}</p>
        </div>`;
        inventoryList.innerHTML += card;
    });
}
