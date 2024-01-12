import solara as sol
from pathlib import Path
from components.button import button_neat
from components.card import card_std
from components.cmp_html import mobile_message

title = "This is a Sony Nordic Dashboard app - Sony BRAVIA"
css = Path('02/src/style.css')


@sol.component_vue('components/dashboard-card.vue')
def dsh_card(labels=['JAN', 'FEB', 'MAR', 'APR', 'MAY'], value=[3, 5, 12, 9, 4], height=150, width=500):
    pass

 
@sol.component_vue('components/mini-nav.vue')
def mininav():
    pass


@sol.component_vue('components/bottom-nav.vue')
def bottomnav(color: str="#F5F7F8"):
    pass


@sol.component
def Second():
    dsh_card()
    bottomnav()


@sol.component
def Home():
    with sol.AppBar():
        sol.Style(css)
        with sol.Link('second'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 mycard"])
        sol.Button(icon_name="mdi-television", classes=["mx-2 mycard"])
        sol.Button(icon_name="mdi-camera", classes=["mx-2 mycard"])
        with sol.Sidebar():
            mobile_message()
            card_std("SONY BRAVIA")
            button_neat("SONY BRAVIA")
    with sol.Columns([1,2,1], gutters_dense=True, classes=["mycard"]):
        with sol.Row(classes=["mybutton"]):
            with sol.Card(title="Card 1", subtitle="Subtitle 1"):
                sol.Text("This is a card")
        with sol.Row(classes=["mybutton"]):
            dsh_card()
        with sol.Card(title="Card title", subtitle="Card subtitle"):
            sol.Markdown(
                "Lorem ipsum dolor sit amet consectetur adipisicing elit. "\
                "Commodi, ratione debitis quis est labore voluptatibus! "\
                "Eaque cupiditate minima, at placeat totam, magni doloremque "\
                "veniam neque porro libero rerum unde voluptatem!"
            )
            with sol.CardActions():
                sol.Button("Action 1", text=True)
                sol.Button("Action 2", text=True)



routes = [
    sol.Route(path="/", component=Home, label="Home"),
    sol.Route(path="second", component=Second, label="Second"),
]
