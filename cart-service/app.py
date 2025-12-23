from flask import Flask

app = Flask(__name__)

@app.route("/cart")
def cart():
    return {
        "cart": ["Milk", "Bread"],
        "total": 120
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

