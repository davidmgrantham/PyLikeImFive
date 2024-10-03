from flask import Flask, render_template



# Create a Flask app
app = Flask(__name__)

# Define a route to the home page
@app.route("/")
def home():
    return render_template("index.html")

