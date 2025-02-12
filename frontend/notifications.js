// Sample Inventory Data (REPLACE WITH YOUR ACTUAL INVENTORY DATA)
const inventory = [
    { name: "Milk", expiryDate: "2024-04-20" }, // Example: Expires in about 10 days
    { name: "Eggs", expiryDate: "2024-04-25" }, // Example: Expires in about 15 days
    { name: "Bread", expiryDate: "2024-04-10" }, // Example: Expires in about 2 days
    { name: "Cheese", expiryDate: "2024-05-01" }, // Example: Expires in about 20 days
    { name: "Apples", expiryDate: "2024-04-08" }, // Example: Expires tomorrow
  ];

  const notificationsDiv = document.getElementById("notifications");
  const noNotificationsDiv = document.getElementById("no-notifications");


  function displayNotifications(items) {
    notificationsDiv.innerHTML = ""; // Clear previous notifications
    noNotificationsDiv.innerHTML = "";

    const today = new Date();
    const tenDaysFromNow = new Date();
    tenDaysFromNow.setDate(today.getDate() + 10);

    let expiringSoon = [];

    items.forEach(item => {
      const expiry = new Date(item.expiryDate);
      if (expiry <= tenDaysFromNow) {
        expiringSoon.push(item);
      }
    });

    if (expiringSoon.length === 0) {
        noNotificationsDiv.textContent = "No items expiring soon.";
        return;
    }

    expiringSoon.forEach(item => {
      const notificationDiv = document.createElement("div");
      notificationDiv.classList.add("notification");

      const expiryDateFormatted = new Date(item.expiryDate).toLocaleDateString(); // Format date

      notificationDiv.innerHTML = `
        <h2>${item.name}</h2>
        <p>Expires: <span class="warning">${expiryDateFormatted}</span></p>
      `;
      notificationsDiv.appendChild(notificationDiv);
    });
  }

  displayNotifications(inventory); // Initial display

  // Example: You would call displayNotifications(updatedInventory) when your inventory data changes
  // ... code to update inventory ...
  // displayNotifications(updatedInventory);