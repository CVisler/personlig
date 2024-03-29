import solara as s
import reacton.ipyvuetify as v

items = "item1 item2 item3".split()
items_selected = s.reactive([])

chips = s.reactive([items[0]])

@s.component
def Page():

    def on_change(widget, event, data):
        chips.set(items_selected.value)

    with s.ColumnsResponsive(10, large=[6,6]):
        cb = v.Combobox(
            v_model=items_selected.value,
            on_v_model=items_selected.set,
            solo=True,
            items=items,
            chips=True,
            deletable_chips=True,
            multiple=True,
            autofocus=True,
            prepend_inner_icon="mdi-filter-variant",
            placeholder="Select relevant items",
        )

        btn = v.Btn(children=['CHECK'])
        v.use_event(btn, 'click', on_change)
        s.Markdown(f"Selected: {chips.value}")
