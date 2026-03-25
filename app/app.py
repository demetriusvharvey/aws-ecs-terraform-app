from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud Engineer Project 1: AWS + Terraform + Docker + ECS is live!"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)