import reacton
import markdown
import reacton.ipywidgets as w
import solara as s

@reacton.component
def Markdown(md: str):
    html = markdown.markdown(md)
    return w.HTML(value=html)


@reacton.component
def MarkdownEditor(md : str):
    md, set_md = reacton.use_state(md)
    edit, set_edit = reacton.use_state(True)
    with w.VBox() as main:
        Markdown(md)
        w.ToggleButton(description="Edit",
                       value=edit,
                       on_value=set_edit)
        if edit:
            w.Textarea(value=md, on_value=set_md, rows=10)
    return main



@s.component
def Page():
    Markdown("# Reacton rocks\nSeriously **bold** idea!")
    MarkdownEditor("# Reacton rocks\nSeriously **bold** idea!")
