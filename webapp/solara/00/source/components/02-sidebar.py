import solara

list_ph2: list[str] = ['TME', 'VSE', 'DIM', 'MOB']
selection_ph2: str = solara.reactive('TME')

@solara.component
def Page():
    with solara.Head():
        solara.Title("Orders dashboard")

    with solara.Column():
        with solara.Sidebar():
            with solara.Card(title="Filter by PH2", subtitle="Pick from dropdown"):
                solara.Select(label='PH2', value=selection_ph2, values=list_ph2, dense=False)
            with solara.Card():
                selection = selection_ph2.value
                solara.Markdown(f"<h3> Selected: {selection} </h3>")
