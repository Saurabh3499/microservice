from flask import Flask

app = Flask(__name__)

@app.route("/menu")
def menu():
    return {
        "items": [
            {"name": "Rice", "price": 50, "image": "https://via.placeholder.com/100?text=Rice"},
            {"name": "Milk", "price": 30, "image": "https://via.placeholder.com/100?text=Milk"},
            {"name": "Banana", "price": 10, "image": "https://via.placeholder.com/100?text=Banana"}
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
