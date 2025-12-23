from flask import Flask, request, jsonify

app = Flask(__name__)
cart = {}

@app.route("/cart", methods=["GET"])
def get_cart():
    total = sum(v["price"] * v["qty"] for v in cart.values())
    return {"cart": cart, "total": total}

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.json
    name = item["name"]

    if name in cart:
        cart[name]["qty"] += 1
    else:
        cart[name] = {
            "price": item["price"],
            "qty": 1
        }
    return jsonify({"message": "added", "cart": cart})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
