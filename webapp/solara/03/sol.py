import solara
from solara.website.pages.examples.utilities import calculator


@solara.component
def Home():
    solara.Markdown("Home")


@solara.component
def About():
    solara.Markdown("About")


routes = [
    solara.Route(path="/", component=Home, label="Home"),
    solara.Route(path="calculator", module=calculator, label="Calculator"),
    solara.Route(path="about", component=About, label="About"),
]
