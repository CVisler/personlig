import solara as sol

@sol.component
def quick_links():
    with sol.Row(gap="0px", justify="end", classes=["quick-links"]):
        with sol.Link('/'):
            sol.Button(icon_name="mdi-home", classes=["mx-2 quick-btns"])
        with sol.Link('/TME'):
            sol.Button(icon_name="mdi-television", classes=["mx-2 quick-btns"])
        with sol.Link('/VSE'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 quick-btns"])
        with sol.Link('/DIM'):
            sol.Button(icon_name="mdi-camera", classes=["mx-2 quick-btns"])
        with sol.Link('/MOB'):
            sol.Button(icon_name="mdi-cellphone", classes=["mx-2 quick-btns"])

@sol.component
def Page():
    quick_links()
