from typing import Callable, List, Tuple
import reacton
import reacton.ipyvuetify as rv
import reacton.ipywidgets as w
import dataclasses


# our model for a todo item, immutable/frozen avoids common bugs
@dataclasses.dataclass(frozen=True)
class TodoItem:
    text: str
    done: bool

        
@reacton.component
def TodoListItem(item: TodoItem, on_item_change:Callable[[TodoItem], None], on_delete:Callable[[], None]):
    """Displays a single todo item"""
    def on_change_done(done: bool):
        on_item_change(dataclasses.replace(item, done=done))

    def on_change_text(text: str):
        on_item_change(dataclasses.replace(item, text=text))
    
    with rv.ListItem() as main:
        with rv.Btn(icon=True) as button_delete:
            rv.Icon(children=["mdi-delete"])
        rv.use_event(button_delete, 'click', lambda *ignore_events: on_delete())
        rv.Checkbox(v_model=item.done, on_v_model=on_change_done, color="success")
        rv.TextField(v_model=item.text, on_v_model=on_change_text)
    return main


@reacton.component
def TodoNew(on_new_item: Callable[[TodoItem], None]):
    """Component that managed entering new todo items"""
    new_text, set_new_text = reacton.use_state("")
    text_field = rv.TextField(v_model=new_text, on_v_model=set_new_text, label="Enter a new todo item")
    def create_new_item(*ignore_args):
        if not new_text:
            return
        # add it
        new_item = TodoItem(text=new_text, done=False)
        on_new_item(new_item)
        # reset text
        set_new_text("")
    rv.use_event(text_field, "keydown.enter", create_new_item)
    return text_field


@reacton.component
def TodoStatus(items: List[TodoItem]):
    """Status of our todo list"""
    count = len(items)
    items_done = [item for item in items if item.done]
    count_done = len(items_done)

    if count != count_done:
        with rv.Row(style_="margin 5px") as main:
            layout = w.Layout(margin="0")
            w.HTML(value=f"<b>Remaining: {count-count_done}</b>", layout=layout)
            rv.Divider(vertical=True, style_="margin: 10px")
            w.HTML(value=f"<b>Completed: {count_done}</b>", layout=layout)
            progress = 100 * count_done // count
            rv.Spacer()
            rv.ProgressCircular(value=progress, color="green" if progress > 50 else "orange")
    else:
        main = rv.Alert(type="success", children=["All done, awesome!"], dense=True)
    return main


@reacton.component
def TodoApp(items: List[TodoItem]):
    items, set_items = reacton.use_state(items)
    
    def on_new_item(new_item: TodoItem):
        new_items = [new_item, *items]
        set_items(new_items)

    with rv.Container() as main:
        TodoNew(on_new_item=on_new_item)

        if items:
            TodoStatus(items)
            for index, item in enumerate(items):
                def on_item_change(changed_item, index=index):
                    new_items = items.copy() # copy because we mutate
                    new_items[index] = changed_item
                    set_items(new_items)

                def on_delete(index=index):
                    new_items = items.copy()  # copy because we mutate
                    new_items.pop(index)
                    set_items(new_items)

                TodoListItem(item, on_item_change, on_delete)
        else:
            rv.Alert(type="info", children=[
                "No todo items, enter some text above, and hit enter"
            ])
    return main


initial_items = [
    TodoItem("Learn reacton", done=True),
    TodoItem("Implement React in Python", done=False),
    TodoItem("Write documentation", done=False),
]

TodoApp(initial_items)
