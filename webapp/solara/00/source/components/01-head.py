import solara as sol

@sol.component
def head_nav():
    with sol.AppBarTitle():
        sol.Text("Hi there")
        sol.Route(path="/")
        sol.Button("Click me", classes=["info mx-2"])


@sol.component
def Page():
    head_nav()
