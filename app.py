from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
   data = pd.read_csv("Titanic-Dataset.csv")
    return f"Rows in dataset: {len(data)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
