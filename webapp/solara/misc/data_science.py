import plotly.express as px
import pandas as pd
import solara

df = px.data.iris()

columns = list(df.columns)
x_axis = solara.reactive("sepal_length")
y_axis = solara.reactive("sepal_width")

@solara.component
def Page():
    # Create a scatter plot by passing "x_axis.value" to px.scatter
    # This will automatically make the component listen to changes in x_axis
    # and re-execute this function when x_axis value changes
    fig = px.scatter(df, x_axis.value, y_axis.value)
    solara.FigurePlotly(fig)

    # Pass x_axis to Select component
    # The select will control the x_axis reactive variable
    solara.Select(label="X-axis", value=x_axis, values=columns)
    solara.Select(label="Y-axis", value=y_axis, values=columns)
