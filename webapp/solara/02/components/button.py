import solara as sol
from pathlib import Path

css = Path('02/src/style.css')

@sol.component
def button_neat(label: str = "default"):
    sol.Style(css)
    sol.Button(label=label, classes=["mybutton"])
