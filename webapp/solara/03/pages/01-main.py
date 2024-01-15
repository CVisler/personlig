import solara as sol
# import pandas as pd
from sys import path
path.append('/home/visler/projects/webapp/solara/03/')
from components import file_drop
from components import echarts
from components import navigation_cluster
from pathlib import Path
# from solara.components.file_drop import FileInfo
# from io import StringIO
# import reacton.ipyvuetify as rv # testing validity - so far seems redundant when we have solara components

css = Path('assets/style.css')
html = """
<p>Hello World</p>
"""

""" Import graphs """
pie = echarts.pandas_df
line = echarts.line


@sol.component_vue('../components/nav.vue')
def vue_nav():
    pass


@sol.component_vue('../components/play.vue')
def vue_play():
    pass


# VI SKAL HAVE SÅDAN EN SMART MENU, HVOR MAN KAN VÆLGE/FRAVÆLGE ELEMENTER, SOM F.EKS. HEADERS I DEN FIL, DER BLIVER DROPPET IND


@sol.component
def Home():
    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            pass
        with sol.Sidebar():
            pass
    with sol.ColumnsResponsive(6, large=[1, 4, 8]):
        vue_nav()
        sol.FigureEcharts(option=pie["trial"])
        sol.FigureEcharts(option=line["kekkers"])


@sol.component
def TME():
    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end", classes=["quick-links"]):
            navigation_cluster.quick_links()
        with sol.Sidebar():
            pass
    with sol.ColumnsResponsive(6, large=[1, 4, 8]):
        pass
    vue_play()


@sol.component
def VSE():
    with sol.AppBar():
        sol.Style(css)
        with sol.Link('/'):
            sol.Button(icon_name="mdi-home", classes=["mx-2 navs"])
        with sol.Link('/TME'):
            sol.Button(icon_name="mdi-television", classes=["mx-2 navs"])
        with sol.Link('/VSE'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 navs"])
        with sol.Link('/DIM'):
            sol.Button(icon_name="mdi-camera", classes=["mx-2 navs"])
        with sol.Link('/MOB'):
            sol.Button(icon_name="mdi-cellphone", classes=["mx-2 navs"])
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)


@sol.component
def DIM():
    with sol.AppBar():
        sol.Style(css)
        with sol.Link('/'):
            sol.Button(icon_name="mdi-home", classes=["mx-2 navs"])
        with sol.Link('/TME'):
            sol.Button(icon_name="mdi-television", classes=["mx-2 navs"])
        with sol.Link('/VSE'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 navs"])
        with sol.Link('/DIM'):
            sol.Button(icon_name="mdi-camera", classes=["mx-2 navs"])
        with sol.Link('/MOB'):
            sol.Button(icon_name="mdi-cellphone", classes=["mx-2 navs"])
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)


@sol.component
def MOB():
    with sol.AppBar():
        sol.Style(css)
        with sol.Link('/'):
            sol.Button(icon_name="mdi-home", classes=["mx-2 navs"])
        with sol.Link('/TME'):
            sol.Button(icon_name="mdi-television", classes=["mx-2 navs"])
        with sol.Link('/VSE'):
            sol.Button(icon_name="mdi-headphones", classes=["mx-2 navs"])
        with sol.Link('/DIM'):
            sol.Button(icon_name="mdi-camera", classes=["mx-2 navs"])
        with sol.Link('/MOB'):
            sol.Button(icon_name="mdi-cellphone", classes=["mx-2 navs"])
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)




routes = [
    sol.Route(path="", component=Home, label="HOME - SONY BRAVIA"),
    sol.Route(path="VSE", component=VSE, label="VIDEO AND SOUND"),
    sol.Route(path="TME", component=TME, label="TV"),
    sol.Route(path="DIM", component=DIM, label="DIGITAL IMAGING"),
    sol.Route(path="MOB", component=MOB, label="MOBILE"),
]
