import solara as sol
import pandas as pd
from sys import path
path.append('/home/visler/projects/webapp/solara/04/')
# from components import py_reacton_combox
from components import file_drop
from components import echarts
from components import navigation_cluster
from pathlib import Path
import reacton.ipyvuetify as rv

css = Path('assets/style.css')

""" Reactive variables """
items = "item1 item2 item3".split()
items_selected = sol.reactive([])
chips = sol.reactive([items[0]])

""" Import graphs """
pie = echarts.pandas_df
line = echarts.line

@sol.component
def Home():
    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            navigation_cluster.quick_links()
        with sol.Column(align="end", classes=["quick-links"]):
            pass
        with sol.Sidebar():
            pass
    with sol.ColumnsResponsive(6, large=[1, 4, 8]):
        sol.FigureEcharts(option=pie["trial"])
        sol.FigureEcharts(option=line["kekkers"])


@sol.component
def TME():
    columns, set_columns = sol.use_state(["Material", "Period"])
    # look_for = '<p tag="p" class="yoink">test</p>'
    # soup = BeautifulSoup(look_for, 'html.parser')
    # eles = soup.find_all('p')


    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            navigation_cluster.quick_links()
        with sol.Sidebar():
            pass
    with sol.ColumnsResponsive(6, large=[4, 8]):
        vue_chips()
    with sol.ColumnsResponsive(6, large=[4, 8]):
        rv.Html(tag="p", class_="yoink", children=['Placeholder'])
    # with sol.ColumnsResponsive(6, large=[4, 8]):
    #     sol.HTML(tag="script", unsafe_innerHTML="const homebrew = document.getElementsByClassName('yoink')\nconsole.log(homebrew[0].innerHTML)")



@sol.component
def VSE():
    items, set_items = sol.use_state(["Material", "Period"])
    chips, set_chips = sol.use_state([])

    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            navigation_cluster.quick_links()
    with sol.ColumnsResponsive(6, large=[4, 8]):
        cb = rv.Combobox(
            v_model=chips,
            items=items,
            chips=True,
            clearable=True,
            placeholder="Select relevant columns",
            multiple=True,
            prepend_icon="mdi-variant",
            solo=True,
            # Implement the set_chips function to assign the selected chips to the chips state
            v_slots=[{
                "name": "selection",
                "variable": "set_chips",
                "children": rv.Chip()
            }])

    sol.Markdown(f"### Chips: {cb.value_property}")
    sol.Markdown(f"### Items: {items}")


@sol.component
def DIM():
    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            navigation_cluster.quick_links()
    with sol.ColumnsResponsive(6, large=[4, 8]):
        count, set_count = sol.use_state(0)
        button = rv.Btn(color="primary", children=["Click me", f": {count}"])

        rv.use_event(button, "click", lambda *ignore_args: set_count(count + 1))



@sol.component
def MOB():
    tezt = file_drop.reactive_var
    def on_change(widget, event, data):
        chips.set(items_selected.value)

    with sol.AppBar():
        sol.Style(css)
        navigation_cluster.quick_links()
        with sol.Sidebar():
            pass

    with sol.ColumnsResponsive([4, 8]):
        sol.Markdown(f"#### items_slct: {items_selected.value}")
        rv.Combobox(
            v_model=items_selected.value,
            on_v_model=items_selected.set,
            items=tezt.value,
            chips=True,
            deletable_chips=True,
            multiple=True,
            autofocus=True,
            prepend_inner_icon="mdi-filter-variant",
            placeholder="Select relevant columns")
    with sol.ColumnsResponsive([4, 8]):
        file_drop.FileDropperBoi()
        sol.Markdown(f"#### tezt: {tezt.value}")


routes = [
    sol.Route(path="", component=Home, label="HOME - SONY BRAVIA"),
    sol.Route(path="VSE", component=VSE, label="VIDEO AND SOUND"),
    sol.Route(path="TME", component=TME, label="TV"),
    sol.Route(path="DIM", component=DIM, label="DIGITAL IMAGING"),
    sol.Route(path="MOB", component=MOB, label="MOBILE"),
]
