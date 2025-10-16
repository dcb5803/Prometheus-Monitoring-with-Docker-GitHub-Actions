from flask import Flask
from metrics import setup_metrics

app = Flask(__name__)
setup_metrics(app)

@app.route("/")
def home():
    return "Hello from monitored app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
