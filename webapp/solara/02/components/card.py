import solara as sol
from pathlib import Path

css = Path('02/src/style.css')

@sol.component
def card_std(title: str = "default"):
    sol.Style(css)
    sol.Card(title=title, classes=["mycard"])
