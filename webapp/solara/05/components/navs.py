import solara as s
import reacton.ipyvuetify as v

@s.component
def quick_links():
    with s.Row(gap="0px", justify="end", classes=["quick-links"]):
        with s.Tooltip('Home'):
            with s.Link('/'):
                s.Button(icon_name="mdi-home", classes=["mx-2 quick-btns"])
        with s.Tooltip('TV'):
            with s.Link('/TME'):
                s.Button(icon_name="mdi-television", classes=["mx-2 quick-btns"])
        v.Tooltip(transition="smooth", open_delay=500, bottom=True, children=["HOVER PLEASE"],
                  v_slots=[{
                    "name": "activator",
                    "variable": "tooltip",
                # If we wanted to have two buttons with the same tooltip, we would need to use a v-for loop like below
                # However, the tooltip pops up under first button only. To fix this, we need to add a v-if statement to the v-for loop like below
                  "children": [v.Btn(href="/VSE", link=True, v_on='tooltip.on', dark=True, children=["HOVER PLEASE"]) for i in range(3)]
                # In order to route the user to "/VSE" on click, we need to add the href and link attributes to the button
                # To add a customr function to the button, we need to add the v_on attribute to the button and set it equal to the function we want to call
                    }])
        # Explanation of v_slots:
        # v_slots is a list of dictionaries, each of which describes a slot in the component
        # slots in vue are like children in react, they are a way to pass custom components to a component
        # the name of the slot is the name of the dictionary key
        # the variable is the name of the variable that will be passed to the slot
        # the children are the components that will be passed to the slot
        # in this case, the slot is called "activator", the variable is called "tooltip" and the children are the button
        # the v_on is a special attribute that allows you to bind a vue event to a python function
        # in this case, the event is "tooltip.on" and the function is "set_tooltip"
        # the set_tooltip function is defined in the python code below
        with s.Tooltip('DIM'):
            with s.Link('/DIM'):
                s.Button(icon_name="mdi-camera", classes=["mx-2 quick-btns"])
        with s.Tooltip('MOBILE'):
            with s.Link('/MOB'):
                s.Button(icon_name="mdi-cellphone", classes=["mx-2 quick-btns"])


@s.component
def Page():
    quick_links()
