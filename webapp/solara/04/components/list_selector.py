import reacton.ipyvuetify as rv

with rv.Combobox(
    on_v_model="chips",
    prepend_icon="mdi-filter-variant",
    label="Select relevant columns",
    clearable=True,
    multiple=True,
    solo=True,
    items=["Material", "Period", "QTY", "P3b", "P4", "P5"],
):
    rv.Chip(
        input_value="chips",
        draggable=True,
        close_=True,
    )
    button = rv.Btn(children='ads', color="primary", max_width="11%")
    rv.use_event(button, "click", my_click_handler)
    sol.Markdown(f"### Selected columns: {column_slct}")
