from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Temporary storage for pantry items
pantry = []

# Helper function to check expiration alerts
def check_expiration(item):
    expiration_date = datetime.strptime(item["expiration_date"], "%Y-%m-%d")
    if datetime.now() > expiration_date:
        return "Expired"
    elif (expiration_date - datetime.now()).days <= 3:
        return "Expiring Soon"
    return "Fresh"

# Route to add an item to the pantry
@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    expiration_date = data.get("expiration_date")

    if name and quantity and expiration_date:
        item = {
            "name": name,
            "quantity": quantity,
            "expiration_date": expiration_date,
            "status": check_expiration({"expiration_date": expiration_date})
        }
        pantry.append(item)
        return jsonify({"message": "Item added!", "item": item})
    else:
        return jsonify({"error": "Invalid data"}), 400

# Route to get all pantry items

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"pantry": pantry})

# Route to delete an item by name
@app.route("/remove-item/<name>", methods=["DELETE"])
def delete_item(name):
    global pantry
    pantry = [item for item in pantry if item["name"] != name]
    return jsonify({"message": f"Item {name} deleted!", "pantry": pantry})

# Spoonacular API key
API_KEY = "e75081b66b18488bbf5857d9bfaa3c5a"

# Route to fetch recipes based on pantry ingredients
@app.route("/get-recipes", methods=["GET"])
def get_recipes():
    try:
        # Get ingredients from pantry
        ingredients = [item["name"] for item in pantry]
        if not ingredients:
            return jsonify({"error": "No ingredients in pantry"}), 400

        # Call Spoonacular API
        url = f"https://api.spoonacular.com/recipes/findByIngredients"
        params = {
            "ingredients": ",".join(ingredients),
            "apiKey": API_KEY,
            "number": 5  # Number of recipes to fetch
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch recipes"}), 500

        # Return recipes to frontend
        recipes = response.json()
        return jsonify({"recipes": recipes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)