import solara as s
import reacton.ipyvuetify as v

items = "item1 item2 item3".split()
chips = s.reactive([items[0]])

@s.component
def Page():

    def on_change(widget, event, data):
        chips.set(['uhm'])

    def false_pos(widget, event, data):
        chips.set(['FALSE'])

    with s.ColumnsResponsive(10, large=[6,6]):
        cb = v.Combobox(
            solo=True,
            items=items,
            chips=True,
            deletable_chips=True,
            multiple=True,
            autofocus=True,
            prepend_inner_icon="mdi-filter-variant",
            placeholder="Select relevant items",)

        btn = v.Btn(children=['CHECK'])
        v.use_event(btn, 'click', on_change)
        s.Markdown(f"### Selected: {chips.value}")
        #
        #
        # _items = [v.ListItem(children=[v.ListItemTitle(children=[f"Click me {i}"])]) for i in range(1, 5)]
        #
        # menu = v.Menu(
        #     offset_y=True,
        #     v_slots=[
        #         {
        #             "name": "activator",
        #             "variable": "menuData",
        #             "children": v.Btn(
        #                 v_on="menuData.on",
        #                 color="primary",
        #                 children=["menu", v.Icon(right=True, children=["mdi-menu-down"])],
        #             ),
        #         }
        #     ],
        #     children=[v.List(children=_items)],
        # )
