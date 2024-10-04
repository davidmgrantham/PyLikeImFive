from pygments import highlight
from pygments.lexers.agile import PythonLexer
from pygments.formatters import HtmlFormatter
from pylikeimfive.constants import PYGMENT_STYLE

def code_styler(code_content):
    """
    Highlights the code content using the Python lexer and a specified style.

    Args:
        code_content (str): The content of the code.

    Returns:
        str: The highlighted code content.
        str: The style of the highlighted code.
    """

    highlighted_code = highlight(code_content, PythonLexer(), HtmlFormatter())
    style = HtmlFormatter(style=PYGMENT_STYLE).get_style_defs('.highlight')

    return highlighted_code, style

def title_stripper(title):
    """
    Strips the file extension from the title and capitalizes the first letter of each word.

    Args:
        title (str): The title of the file.

    Returns:
        str: The stripped and capitalized title.
    """
    return title.split('.')[0].replace('_', ' ').title()
