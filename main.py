from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevSecOps!!!"

# Dangerous route using eval()
@app.route("/danger")
def danger():
    user_input = request.args.get("code")
    return str(eval(user_input))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
