import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/inventory/*": {"origins": "*"}})  # Allow all requests

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


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Inventory list (temporary storage)
inventory = []


@app.route("/inventory", methods=["GET"])
def get_inventory():
    records = sheet.get_all_records()  # Read all data from Google Sheets
    return jsonify({"inventory": records})


@app.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    expiration_date = data.get("expiration_date")

    if name and quantity and expiration_date:
        sheet.append_row([name, quantity, expiration_date])  # Add new row in Google Sheets
        return jsonify({"message": "Item added!", "inventory": sheet.get_all_records()})
    else:
        return jsonify({"error": "Invalid data"}), 400


if __name__ == "__main__":
    app.run(debug=True)