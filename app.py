# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from datetime import datetime, timedelta
# import requests

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend-backend communication

# # Temporary storage for pantry items
# pantry = []

# # Helper function to check expiration alerts
# def check_expiration(item):
#     expiration_date = datetime.strptime(item["expiration_date"], "%Y-%m-%d")
#     if datetime.now() > expiration_date:
#         return "Expired"
#     elif (expiration_date - datetime.now()).days <= 3:
#         return "Expiring Soon"
#     return "Fresh"

# # Route to add an item to the pantry
# @app.route("/add-item", methods=["POST"])
# def add_item():
#     data = request.json
#     name = data.get("name")
#     quantity = data.get("quantity")
#     expiration_date = data.get("expiration_date")

#     if name and quantity and expiration_date:
#         item = {
#             "name": name,
#             "quantity": quantity,
#             "expiration_date": expiration_date,
#             "status": check_expiration({"expiration_date": expiration_date})
#         }
#         pantry.append(item)
#         return jsonify({"message": "Item added!", "item": item})
#     else:
#         return jsonify({"error": "Invalid data"}), 400

# # Route to get all pantry items

# @app.route("/items", methods=["GET"])
# def get_items():
#     return jsonify({"pantry": pantry})

# # Route to delete an item by name
# @app.route("/remove-item/<name>", methods=["DELETE"])
# def delete_item(name):
#     global pantry
#     pantry = [item for item in pantry if item["name"] != name]
#     return jsonify({"message": f"Item {name} deleted!", "pantry": pantry})

# # Spoonacular API key
# API_KEY = "e75081b66b18488bbf5857d9bfaa3c5a"

# # Route to fetch recipes based on pantry ingredients
# @app.route("/get-recipes", methods=["GET"])
# def get_recipes():
#     try:
#         # Get ingredients from pantry
#         ingredients = [item["name"] for item in pantry]
#         if not ingredients:
#             return jsonify({"error": "No ingredients in pantry"}), 400

#         # Call Spoonacular API
#         url = f"https://api.spoonacular.com/recipes/findByIngredients"
#         params = {
#             "ingredients": ",".join(ingredients),
#             "apiKey": API_KEY,
#             "number": 5  # Number of recipes to fetch
#         }
#         response = requests.get(url, params=params)
#         if response.status_code != 200:
#             return jsonify({"error": "Failed to fetch recipes"}), 500

#         # Return recipes to frontend
#         recipes = response.json()
#         return jsonify({"recipes": recipes})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the full path of the credentials file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")

# Google Sheets API Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)  # Load credentials
client = gspread.authorize(creds)

# Open the Google Sheet
SHEET_ID = "1Bvo6GG1Y9e5UPdyrkTvIjNoBKESyoMgZLxP4-Vt2i_4"  # Replace with your actual Sheet ID
sheet = client.open_by_key(SHEET_ID).sheet1

# Helper function to check expiration alerts
def check_expiration(item):
    expiration_date = datetime.strptime(item["expiration_date"], "%Y-%m-%d")
    if datetime.now() > expiration_date:
        return "Expired"
    elif (expiration_date - datetime.now()).days <= 3:
        return "Expiring Soon"
    return "Fresh"

# Route to get all pantry items from Google Sheets
@app.route("/items", methods=["GET"])
def get_items():
    records = sheet.get_all_records()  # Read all data from Google Sheets
    return jsonify({"pantry": records})

# Route to add an item to the pantry (Google Sheets)
@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    expiration_date = data.get("expiration_date")

    if name and quantity and expiration_date:
        # Add the item to Google Sheets
        sheet.append_row([name, quantity, expiration_date])
        # Return the updated inventory
        records = sheet.get_all_records()
        return jsonify({"message": "Item added!", "inventory": records})
    else:
        return jsonify({"error": "Invalid data"}), 400

# Route to delete an item by name from Google Sheets
@app.route("/remove-item/<name>", methods=["DELETE"])
def delete_item(name):
    try:
        # Get all records from the sheet
        records = sheet.get_all_records()
        # Find the row to delete
        row_to_delete = None
        for i, record in enumerate(records):
            if record["name"] == name:
                row_to_delete = i + 2  # Rows in Google Sheets are 1-indexed, and the first row is headers
                break

        if row_to_delete:
            # Delete the row from Google Sheets
            sheet.delete_rows(row_to_delete)
            return jsonify({"message": f"Item {name} deleted!", "inventory": sheet.get_all_records()})
        else:
            return jsonify({"error": "Item not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Spoonacular API key
API_KEY = "e75081b66b18488bbf5857d9bfaa3c5a"

# Route to fetch recipes based on pantry ingredients
@app.route("/get-recipes", methods=["GET"])
def get_recipes():
    try:
        # Get ingredients from Google Sheets
        records = sheet.get_all_records()
        ingredients = [item["name"] for item in records]
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

# Route to get expiring items within the next 3 days
@app.route("/expiring-items", methods=["GET"])
def get_expiring_items():
    try:
        # Get all records from Google Sheets
        records = sheet.get_all_records()
        
        # Get today's date and the date 3 days from now
        today = datetime.now()
        three_days_from_now = today + timedelta(days=3)
        
        # Filter items expiring within the next 3 days
        expiring_items = []
        for item in records:
            expiration_date = datetime.strptime(item["expiration_date"], "%Y-%m-%d")
            if today <= expiration_date <= three_days_from_now:
                expiring_items.append({
                    "name": item["name"],
                    "expiryDate": item["expiration_date"]
                })
        
        return jsonify({"expiring_items": expiring_items})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(debug=True)