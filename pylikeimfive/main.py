from flask import Flask, render_template
from pygments import highlight
from pygments.lexers.agile import PythonLexer
from pygments.formatters import HtmlFormatter
from pylikeimfive.helper import code_styler, title_stripper

# Create a Flask app
app = Flask(__name__)

# Define a route to the home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guides/<folder>/<filename>")
def guide(folder, filename):

    with open(f"guides/{folder}/{filename}") as f:
        code_content = f.read()

    highlighted_code, style = code_styler(code_content)

    return render_template("guide.html", title=title_stripper(filename), code=highlighted_code, style=style)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

