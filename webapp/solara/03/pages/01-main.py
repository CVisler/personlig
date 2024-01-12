import solara as sol
import numpy as np
import pandas as pd
from io import StringIO
import sys
sys.path.append('/home/visler/projects/webapp/solara/03/components/')
from navigation_cluster import clustered_navigation_links
from pathlib import Path
from solara.components.file_drop import FileInfo
import textwrap

css = Path('src/style.css')
html = """
<p>Hello World</p>
"""


@sol.component
def FileDropperBoi():
    df, set_df = sol.use_state(None)
    filename, set_filename = sol.use_state("")

    def on_file(file: FileInfo):
        set_filename(file["name"])
        f = file["file_obj"]
        data = f.read()

        # Assuming the data is in csv format
        s = str(data, 'utf-8')
        data = StringIO(s) 

        # Convert the data to a pandas DataFrame
        df = pd.read_csv(data)
        set_df(df)

    with sol.Div() as main:
        sol.FileDrop(
            label="Drag and drop a .csv file here",
            on_file=on_file,
            lazy=True,  # We will only read the file when needed
        )
        if df is not None:
            sol.Info(f"File {filename} has been loaded into a DataFrame with {df.shape[0]} rows and {df.shape[1]} columns.")
            sol.DataFrame(df)

    return main


@sol.component
def Home():
    with sol.AppBar():
        sol.Style(css)
        with sol.Column(align="end"):
            clustered_navigation_links()
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)
    with sol.ColumnsResponsive():
        sol.HTML(unsafe_innerHTML=html)
        FileDropperBoi()



@sol.component
def TME():
    with sol.AppBar():
        sol.Style(css)
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
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)


@sol.component
def VSE():
    with sol.AppBar():
        sol.Style(css)
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
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)


@sol.component
def DIM():
    with sol.AppBar():
        sol.Style(css)
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
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)


@sol.component
def MOB():
    with sol.AppBar():
        sol.Style(css)
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
        with sol.Sidebar():
            sol.HTML(unsafe_innerHTML=html)




# @sol.component
# def Page():
#     Home()
#     VSE()


routes = [
    sol.Route(path="", component=Home, label="HOME"),
    sol.Route(path="VSE", component=VSE, label="VIDEO AND SOUND"),
    sol.Route(path="TME", component=TME, label="TV"),
    sol.Route(path="DIM", component=DIM, label="DIGITAL IMAGING"),
    sol.Route(path="MOB", component=MOB, label="MOBILE"),
]
