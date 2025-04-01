from flask import Flask, request, jsonify
from flask_cors import CORS
from database import collection
from bson import ObjectId

app = Flask(__name__)
CORS(app)
app.app_context().push()

@app.route("/invoices", methods=["POST"])
def add_invoice():
    data = request.json
    invoice = {
        "customer": data.get("customer"),
        "amount": data.get("amount"),
        "status": data.get("status"),
        "date": data.get("date")
    }
    result = collection.insert_one(invoice)
    return jsonify({"message": "Invoice added", "id": str(result.inserted_id)}), 201

@app.route("/invoices", methods=["GET"])
def get_invoices():
    invoices = []
    for invoice in collection.find():
        invoices.append({
            "id": str(invoice["_id"]),
            "customer": invoice["customer"],
            "amount": invoice["amount"],
            "status": invoice["status"],
            "date": invoice["date"]
        })
    return jsonify(invoices)

@app.route("/invoices/<invoice_id>", methods=["PUT"])
def update_invoice(invoice_id):
    data = request.json
    collection.update_one({"_id": ObjectId(invoice_id)}, {"$set": data})
    return jsonify({"message": "Invoice updated"}), 200

@app.route("/invoices/<invoice_id>", methods=["DELETE"])
def delete_invoice(invoice_id):
    collection.delete_one({"_id": ObjectId(invoice_id)})
    return jsonify({"message": "Invoice deleted"}), 200

#  Ensure Gunicorn can find the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
