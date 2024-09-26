import os

from fasthtml.common import *

# Add the HighlightJS built-in header
hdrs = (HighlightJS(langs=["python", "javascript", "html", "css"]),)

# Instantiates a FastHTML app with fast_app() This provides really userful defaults used later in the app.
# live=True sets live reloading to on, which is useful for development.
app, rt = fast_app(hdrs=hdrs, live=True)


# The rt decorator is used to define routes. It tells the app to run the function when the route is accessed.
@rt("/")
def home():

    # List all .py files in the guides folder
    guide_files = [f for f in os.listdir("guides") if f.endswith(".py")]

    # Create list items for each guide
    guide_links = [
        Li(A(f.replace("_", " ").replace(".py", "").title(), href=f"/guides/{f}"))
        for f in guide_files
    ]

    return Div(
        Titled(
            "PylikeImFive",
            H4("Welcome to PylikeImFive!"),
            P("This is a simple web app that explains Python concepts like you're five."),
            P("Click on the links below to get started!"),
            Ul(*guide_links),
        )
    )


@rt("/guides/{guide}")
def guide_page(guide: str):
    print(os.getcwd())
    # Construct the full file path
    file_path = f"guides/{guide}"

    # Check if the file exists
    if not os.path.exists(file_path):
        return Titled("Not Found", P(f"Sorry, the guide {guide} was not found."))

    # Read the content of the guide file
    with open(file_path, "r") as file:
        code_content = file.read()

    # Render the guide content
    return Titled(
        guide.replace("_", " ").replace(".py", "").title(),
        P(f"This is the guide for {guide.replace('_', ' ').replace('.py', '').title()}."),
        Pre(Code(code_content)),
        P(A("Back to Home", href="/", style="display: inline-block; padding: 10px 20px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px; text-decoration: none; color: #333;")
        ),
    )


serve()  # Starts the server