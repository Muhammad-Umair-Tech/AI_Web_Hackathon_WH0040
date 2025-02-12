const API_URL = "http://127.0.0.1:5000"; // Correct API URL

// Function to add an item from input fields
function addItemFromInput() {
    let name = document.getElementById("itemName").value;
    let quantity = document.getElementById("itemQuantity").value;
    let expiry = document.getElementById("itemExpiration").value; // Correct ID

    if (!name || !quantity || !expiry) {
        alert("Please fill all fields.");
        return;
    }

    addItem(name, quantity, expiry);
}

// Function to add an item
async function addItem(name, quantity, expiry) {
    try {
        let response = await fetch(`${API_URL}/inventory`, { // Correct endpoint
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, quantity, expiration_date: expiry }) // Use expiration_date
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        let result = await response.json();
        alert(result.message);
        fetchItems(); // Refresh inventory list
    } catch (error) {
        console.error("Error adding item:", error);
    }
}

// Function to remove an item
async function removeItem() {
    let name = document.getElementById("removeName").value;

    if (!name) {
        alert("Enter an item name to remove.");
        return;
    }

    let response = await fetch(`${API_URL}/inventory/${name}`, { // Correct endpoint
        method: "DELETE"
    });

    let result = await response.json();
    alert(result.message);
    fetchItems();
}

// Function to fetch and display items
async function fetchItems() {
    let response = await fetch(`${API_URL}/inventory`); // Correct API URL
    let data = await response.json();
    let items = data.inventory; // Extract inventory list

    let inventoryList = document.getElementById("inventoryList");
    inventoryList.innerHTML = "";

    items.forEach(item => {
        let card = `<div class="item-card">
            <h3>${item.name}</h3>
            <p>Quantity: ${item.quantity}</p>
            <p>Expires on: ${item.expiration_date}</p> <!-- Use expiration_date -->
        </div>`;
        inventoryList.innerHTML += card;
    });
}
