import solara as sol

@sol.component
def head_nav():
    with sol.AppBarTitle():
        sol.Text("what")
        sol.Button("Click me", classes=["info mx-2"])

@sol.component
def body():
    with sol.Columns([1,2]):
        with sol.Row(margin=10, justify="center"):
            with sol.Card():
                sol.Markdown("This is a card")
                sol.Button("Click me")
            with sol.Card():
                sol.Markdown("This is a card")
                sol.Button("Click me")
            with sol.Card():
                sol.Markdown("This is a card")
                sol.Button("Click me")
        with sol.Row():
            with sol.Card():
                sol.Markdown("This is a card")
                sol.Button("Click me")
            with sol.Card():
                sol.Markdown("This is a card")
                sol.Button("Click me")
            with sol.Card():
                with sol.Column():
                    sol.Markdown("This is a card")
                    sol.Button("Click me")
                    with sol.Link("/fruit/banana"):
                        sol.Button("Go to banana")

@sol.component
def Page():
    head_nav()
    body()
