from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevSecOps!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
