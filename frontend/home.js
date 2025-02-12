// Home Page JavaScript
document.addEventListener("DOMContentLoaded", function () {
    console.log("Home Page Loaded Successfully");

    // Example: Adding an event listener for the newsletter subscription form
    const newsletterForm = document.querySelector(".newsletter-form");

    if (newsletterForm) {
        newsletterForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent form submission
            const emailInput = newsletterForm.querySelector("input[type='email']");
            
            if (emailInput.value.trim() !== "") {
                alert("Thank you for subscribing!");
                emailInput.value = ""; // Clear input field
            } else {
                alert("Please enter a valid email address.");
            }
        });
    }
});

// Animated Stats Counter
function animateValue(id, start, end, duration) {
    let obj = document.getElementById(id);
    let range = end - start;
    let increment = range / (duration / 50);
    let current = start;
    let timer = setInterval(function () {
        current += increment;
        obj.innerText = Math.floor(current) + "+";
        if (current >= end) {
            obj.innerText = end + "+";
            clearInterval(timer);
        }
    }, 50);
}

window.onload = function () {
    animateValue("recipesCount", 0, 150, 2000);
    animateValue("inventoryCount", 0, 80, 2000);
    animateValue("usersCount", 0, 500, 2000);
};

