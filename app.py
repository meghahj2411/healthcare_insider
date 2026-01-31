from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load ML results CSV
df = pd.read_csv("results/final_insider_risk_report.csv")

@app.route("/api/users")
def get_users():
    return jsonify(df.to_dict(orient="records"))

@app.route("/api/explanation/<user_id>")
def get_explanation(user_id):
    row = df[df["user_id"] == user_id].iloc[0]
    return jsonify(row.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
