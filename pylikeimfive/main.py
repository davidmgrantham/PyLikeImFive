import os

from fasthtml.common import *

# Add the HighlightJS built-in header
# https://highlightjs.org/
hdrs = (HighlightJS(langs='python'))

# Instantiates a FastHTML app with fast_app() This provides really userful defaults used later in the app.
# live=True sets live reloading to on, which is useful for development.

css = Style(open('bootstrap.css').read(), type="text/css", rel="stylesheet")
js = Script(open('bootstrap.bundle.js').read())
app, rt = fast_app(pico=False, hdrs=[hdrs, css, js], live=True)


# The rt decorator is used to define routes. It tells the app to run the function when the route is accessed.
@rt("/")
def home():

    # Dynamically find all folders in the guides directory
    categories = [folder for folder in os.listdir("guides") if os.path.isdir(f"guides/{folder}")]

    category_links = []
    for folder in categories:
        # Generate category name from folder (replace underscores, capitalize)
        category_name = folder.replace("_", " ").title()

        # Generate links for the guides inside the folder
        guide_links = generate_guide_links(folder)

        # Only add the category if there are guides in it
        if guide_links:
            category_links.append(
                Div(
                    H4(category_name),
                    Ul(*guide_links),
                    style="margin-left: auto; margin-right: auto; width: 20em"
                )
            )

    offcanvas = Div(
        Div(
            H5("PylikeImFive!", cls="offcanvas-title", id="offcanvasExampleLabel"),
            Button(
                "",
                type="button",
                cls="btn-close text-reset",
                data_bs_dismiss="offcanvas",
                aria_label="Close"
            ),
            cls="offcanvas-header"
        ),
        Div(
            Div(
                Button(
                    "Basics",
                    type="button",
                    id="dropdownMenuButton",
                    cls="btn btn-secondary dropdown-toggle",
                    data_bs_toggle="dropdown"
                ),
                Ul(
                    Li(A("Varibles", href="/guides/basics/varibles.py", cls="dropdown-item")),
                    Li(A("Strings", href="/guides/basics/strings.py", cls="dropdown-item")),
                    Li(A("Integers", href="/guides/basics/integers.py", cls="dropdown-item list-unstyled")),
                    cls="dropdown-menu",
                    aria_labelledby="dropdownMenuButton"
                ),
                cls="dropdown mt-3"
            ),
            Div(
                Button(
                    "Collections",
                    type="button",
                    id="dropdownMenuButton",
                    cls="btn btn-secondary dropdown-toggle",
                    data_bs_toggle="dropdown"
                ),
                Ul(
                    Li(A("Lists", href="/guides/collections/lists.py", cls="dropdown-item")),
                    Li(A("Dictionary", href="/guides/basics/strings.py", cls="dropdown-item")),
                    Li(A("Tuples", href="/guides/basics/integers.py", cls="dropdown-item")),
                    cls="dropdown-menu",
                    aria_labelledby="dropdownMenuButton"
                ),
                cls="dropdown mt-3"
            ),
            cls="offcanvas-body"
        ),
        cls="offcanvas offcanvas-start",
        tabindex="-1",
        id="offcanvasExample",
        aria_labelledby="offcanvasExampleLabel"
    )

    content = Div(
        Div(
            H3("Welcome to PylikeImFive!"),
            Button(
                "Learn Now",
                type="button",
                cls="btn btn-primary btn-lg",
                data_bs_toggle="offcanvas",
                data_bs_target="#offcanvasExample",
                aria_controls="offcanvasExample"
            ),
            cls="text-center"
        ),
        cls="d-flex flex-column justify-content-center align-items-center vh-100"
    )




    return Div(offcanvas, content)

# Helper function to generate guide links for a specific folder
def generate_guide_links(folder_name):
    guide_files = [
        f for f in os.listdir(f"guides/{folder_name}") if f.endswith(".py")
    ]
    return [
        Li(A(f.replace("_", " ").replace(".py", "").title(),
             href=f"/guides/{folder_name}/{f}"))
        for f in guide_files
    ]


# Route to handle guide page for specific folder and guide
@rt("/guides/{folder}/{guide}")
def guide_page(folder: str, guide: str):

    # Construct the full file path
    file_path = f"guides/{folder}/{guide}"

    # Read the content of the guide file
    with open(file_path, "r") as file:
        code_content = file.read()

    # Render the guide content
    return Titled(
        guide.replace("_", " ").replace(".py", "").title(),
        Pre(Code(code_content)),
        P(A("Back to Home", href="/", style="display: inline-block; padding: 10px 20px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px; text-decoration: none; color: #333")
        )
    )


serve()  # Starts the server