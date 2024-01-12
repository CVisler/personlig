import solara as sol
from pathlib import Path


css = Path('03/src/style.css')


@sol.component
def clustered_navigation_links(children=[], css: Path=css):
    # sol.Style(css)
    with sol.HBox(children=children, align_items="center", classes=["navcluster"]):
        with sol.Link('/'):
            sol.Button(icon_name="mdi-home", classes=["mx-2 mycard"])
        with sol.Link('/TME'):
            sol.Button(icon_name="mdi-television", classes=["mx-2 mycard"])
        with sol.Link('/VSE'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 mycard"])
        with sol.Link('/DIM'):
            sol.Button(icon_name="mdi-camera", classes=["mx-2 mycard"])
        with sol.Link('/MOB'):
            sol.Button(icon_name="mdi-cellphone", classes=["mx-2 mycard"])

# @sol.component
# def Page():
#     clustered_navigation_links()
