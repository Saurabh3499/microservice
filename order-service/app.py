from flask import Flask
import requests

app = Flask(__name__)

@app.route("/order")
def order():
    cart = requests.get("http://cart-service:8080/cart").json()

    return {
        "order_id": 101,
        "status": "CONFIRMED",
        "cart_details": cart
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

