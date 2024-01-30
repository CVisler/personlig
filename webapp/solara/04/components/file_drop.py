import solara as sol
import pandas as pd
from io import StringIO
from solara.components.file_drop import FileInfo

test = "test"
reactive_var = sol.reactive(["one", "two", "three"])

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
        reactive_var.set(df.columns.tolist())

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
