from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Inventory list (temporary storage)
inventory = []


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify({"inventory": inventory})


@app.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    expiration_date = data.get("expiration_date")  # Get expiration date

    if name and quantity and expiration_date:
        inventory.append({"name": name, "quantity": quantity, "expiration_date": expiration_date})
        return jsonify({"message": "Item added!", "inventory": inventory})
    else:
        return jsonify({"error": "Invalid data"}), 400


if __name__ == "__main__":
    app.run(debug=True)