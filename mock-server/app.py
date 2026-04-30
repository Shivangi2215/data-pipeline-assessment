from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

with open("data/customers.json") as f:
    customers = json.load(f)


@app.route("/api/customers", methods=["GET"])
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })


@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = next((c for c in customers if c["customer_id"] == customer_id), None)
    if not customer:
        abort(404)
    return jsonify(customer)


@app.route("/api/health", methods=["GET"])
def health():
    return {"status": "ok"}
