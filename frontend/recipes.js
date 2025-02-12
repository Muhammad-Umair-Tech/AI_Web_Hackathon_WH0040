// Sample Inventory Data (REPLACE WITH YOUR ACTUAL INVENTORY)
const inventory = [
    "Pasta", "Eggs", "Bacon", "Parmesan Cheese", "Salt", "Pepper", "Oil", "Garlic", "Onion" // Example ingredients
  ];

  // Sample Recipe Data (REPLACE WITH YOUR ACTUAL RECIPES)
  const recipes = [
    {
      name: "Spaghetti Carbonara",
      ingredients: ["Pasta", "Eggs", "Bacon", "Parmesan Cheese", "Salt", "Pepper"],
      instructions: "Cook pasta. Fry bacon. Whisk eggs and cheese. Combine and serve."
    },
    {
      name: "Garlic Pasta",
      ingredients: ["Pasta", "Garlic", "Oil", "Salt", "Pepper"],
      instructions: "Cook pasta. Saute garlic in oil. Combine and serve."
    },
    {
      name: "Bacon and Egg Pasta",
      ingredients: ["Pasta", "Eggs", "Bacon", "Salt", "Pepper"],
      instructions: "Cook pasta. Fry bacon. Fry eggs. Combine and serve."
    },
    {
      name: "Onion Omelette",
      ingredients: ["Eggs", "Onion", "Salt", "Pepper", "Oil"],
      instructions: "Saute onion. Whisk eggs. Cook omelette."
    },
    {
      name: "Fancy Omelette",
      ingredients: ["Eggs", "Onion", "Salt", "Pepper", "Oil", "Bacon", "Parmesan Cheese"],
      instructions: "Saute onion and bacon. Whisk eggs and cheese. Cook omelette."
    },
     {
      name: "Simple Salad",
      ingredients: ["Onion", "Salt", "Pepper", "Oil"],
      instructions: "Chop ingredients and mix."
    },
  ];

  const recipeList = document.getElementById("recipe-list");

  function suggestRecipes(availableIngredients) {
    recipeList.innerHTML = ""; // Clear previous suggestions

    recipes.forEach(recipe => {
      let canMake = true;
      recipe.ingredients.forEach(ingredient => {
        if (!availableIngredients.includes(ingredient)) {
          canMake = false;
        }
      });

      if (canMake) {
        const recipeDiv = document.createElement("div");
        recipeDiv.classList.add("recipe");

        let ingredientsList = "<ul>";
        recipe.ingredients.forEach(ingredient => {
          ingredientsList += `<li>${ingredient}</li>`;
        });
        ingredientsList += "</ul>";

        recipeDiv.innerHTML = `
          <h2>${recipe.name}</h2>
          <div class="ingredients">Ingredients: ${ingredientsList}</div>
          <p>Instructions: ${recipe.instructions}</p>
        `;
        recipeList.appendChild(recipeDiv);
      }
    });
      if (recipeList.innerHTML === "") {
          recipeList.innerHTML = "<p>No recipes found matching your available ingredients.</p>";
      }
  }


  // Initial recipe suggestions based on current inventory
  suggestRecipes(inventory);


  // Example of how to trigger suggestions (e.g., after updating inventory)
  // You'll need to adapt this to your specific inventory update mechanism
  // For example, if you have a button to update inventory:

  const updateButton = document.getElementById("update-inventory-button");
  updateButton.addEventListener("click", () => {
      // ... code to update the 'inventory' array ...
      suggestRecipes(inventory); // Then re-suggest recipes
  });