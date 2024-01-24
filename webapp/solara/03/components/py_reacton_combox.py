import reacton as r
import markdown
import reacton.ipyvuetify as v
import reacton.ipywidgets as w
import solara as s

@r.component
def combo_box(items: list[str]=["Item1", "Item2", "Item3", "different"]):
    selection, set_selection = r.use_state(items)

    combo_box = w.Combobox(
        options=items,
        placeholder="Otto",
        continuous_update=True,
        description=selection,
        on_value=set_selection,
    )

    
    return combo_box


# @reacton.component
# def MarkdownEditor(md : str):
#     md, set_md = reacton.use_state(md)
#     edit, set_edit = reacton.use_state(True)
#     with w.VBox() as main:
#         Markdown(md)
#         w.ToggleButton(description="Edit",
#                        value=edit,
#                        on_value=set_edit)
#         if edit:
#             w.Textarea(value=md, on_value=set_md, rows=10)
#     return main


@s.component
def Page():
    combo_box()
