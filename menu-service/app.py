from flask import Flask

app = Flask(__name__)

@app.route("/menu")
def menu():
    return {
        "items": ["Rice", "Milk", "Bread", "Vegetables"]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

