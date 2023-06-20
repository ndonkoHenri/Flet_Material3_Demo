import flet as ft
from .section import Section, SubSection

# Actions Components

cb_width = 127
cb_width_icon = cb_width - 20
cb_height = 35
common_buttons = ft.Row(
    [
        ft.Column(
            [
                ft.ElevatedButton("Elevated", width=cb_width, height=cb_height),
                ft.FilledButton("Filled", width=cb_width, height=cb_height),
                ft.FilledTonalButton("Filled tonal", width=cb_width, height=cb_height),
                ft.OutlinedButton("Outlined", width=cb_width, height=cb_height),
                ft.TextButton("Text", width=cb_width, height=cb_height)
            ]
        ),
        ft.Column(
            [
                ft.ElevatedButton("Icon", icon=ft.icons.ADD, width=cb_width_icon, height=cb_height),
                ft.FilledButton("Icon", icon=ft.icons.ADD, width=cb_width_icon, height=cb_height),
                ft.FilledTonalButton("Icon", icon=ft.icons.ADD, width=cb_width_icon, height=cb_height),
                ft.OutlinedButton("Icon", icon=ft.icons.ADD, width=cb_width_icon, height=cb_height),
                ft.TextButton("Icon", icon=ft.icons.ADD, width=cb_width_icon, height=cb_height)
            ]
        ),
        ft.Column(
            [
                ft.ElevatedButton("Elevated", width=cb_width, height=cb_height),
                ft.FilledButton("Filled", width=cb_width, height=cb_height, disabled=True),
                ft.FilledTonalButton("Filled tonal", width=cb_width, height=cb_height, disabled=True),
                ft.OutlinedButton("Outlined", width=cb_width, height=cb_height),
                ft.TextButton("Text", width=cb_width, height=cb_height)
            ],
            disabled=True
        )
    ]
)

floating_action_buttons = ft.Row(
    controls=[
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Small", mini=True),
        ft.FloatingActionButton("Create", icon=ft.icons.ADD, tooltip="Extended"),
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Standard"),
        ft.FloatingActionButton(content=ft.Icon(ft.icons.ADD, size=35), tooltip="Large", height=92, width=90),
    ],
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
    alignment=ft.MainAxisAlignment.CENTER
)

icon_buttons = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED, disabled=True),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED, disabled=True),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED, disabled=True),
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED, disabled=True),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    ]
)


# Communication Components

def play_progress_indicators(e):
    if not progress_indicators.controls[1].value:
        progress_indicators.controls[1].value = progress_indicators.controls[2].value = 0.7
    else:
        progress_indicators.controls[1].value = progress_indicators.controls[2].value = None

    progress_indicators.update()


progress_indicators = ft.Row(
    controls=[
        ft.IconButton(ft.icons.PLAY_ARROW, on_click=play_progress_indicators),
        ft.ProgressRing(value=0.7),
        ft.ProgressBar(value=0.7, width=290)
    ]
)

snackbar = ft.TextButton("Show snackbar")

# Containment Components

bottom_sheet = ft.Row(
    [
        ft.TextButton("Show modal bottom sheet"),
        ft.TextButton("Show bottom sheet")
    ]
)

cards = ft.Text("To be Done")

alert_dialog = ft.AlertDialog(
    title=ft.Text("What is a Dialog?"),
    content=ft.Text(
        "A dialog is a type of modal window that appears in front of app content to provide critical information, or prompt for a decision to be made."),
    actions=[
        ft.TextButton("Okay"),
        ft.ElevatedButton("Dismiss")
    ]
)

dialogs = ft.Row(
    [
        ft.TextButton("Show dialog"),
        ft.TextButton("Show full-screen dialog")
    ]
)

dividers = ft.Divider(height=5, thickness=1)

# Navigation Components
# TBD

# Selection Components
checkboxes = ft.ListView(
    controls=[
        ft.ListTile(title=ft.Text("Option 1"), trailing=ft.Checkbox(value=True, tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 2"), trailing=ft.Checkbox(value=True, tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 3"), trailing=ft.Checkbox(tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 4"), trailing=ft.Checkbox(value=False), disabled=True)
    ]
)

date_picker = ft.TextButton("Show date picker")


def dropdown_change(e):
    i = menus.controls[1].controls[2]
    if e.control.data == "icon":
        i.icon = e.control.value.lower()
    elif e.control.data == "color":
        i.color = e.control.value.lower()
    menus.update()


menus = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.PopupMenuButton(
                    ft.FilledTonalButton("Show menu"),
                    items=[
                        ft.PopupMenuItem(icon=ft.icons.PERSON_2, content=ft.Text("Item 1")),
                        ft.PopupMenuItem(icon=ft.icons.PANORAMA_FISHEYE, content=ft.Text("Item 2")),
                        ft.PopupMenuItem(icon=ft.icons.RESTART_ALT, content=ft.Text("Item 3"))
                    ]
                ),
                ft.PopupMenuButton(
                    ft.Icon(ft.icons.MENU),
                    items=[
                        ft.PopupMenuItem(content=ft.Text("Menu 1")),
                        ft.PopupMenuItem(content=ft.Text("Menu 2")),
                        ft.PopupMenuItem(content=ft.Text("Menu 3"), )
                    ]
                )
            ]
        ),
        ft.Row(
            controls=[
                ft.Dropdown(
                    label="Color",
                    options=[
                        ft.dropdown.Option("Blue"),
                        ft.dropdown.Option("Pink"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Yellow"),
                        ft.dropdown.Option("Grey", disabled=True),
                    ],
                    on_change=dropdown_change,
                    data="color",
                    width=100
                ),
                ft.Dropdown(
                    label="Icon",
                    prefix_icon=ft.icons.SEARCH,
                    options=[
                        # ft.dropdown.Option("Smile"),
                        ft.dropdown.Option("Cloud"),
                        ft.dropdown.Option("Brush"),
                        ft.dropdown.Option("Heart"),
                    ],
                    value="Cloud",
                    on_change=dropdown_change,
                    data="icon"
                ),
                ft.Icon(ft.icons.CLOUD)
            ]
        )
    ]
)

radio_buttons = ft.RadioGroup(
    content=ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text("Option 1"), leading=ft.Radio(value="1"), toggle_inputs=True),
            ft.ListTile(title=ft.Text("Option 2"), leading=ft.Radio(value="2"), toggle_inputs=True),
            ft.ListTile(title=ft.Text("Option 3"), leading=ft.Radio(value="3"), disabled=True),
        ]
    ),
    value="1"
)

sliders = ft.Column(
    controls=[
        ft.Slider(min=0, max=100),
        ft.Slider(min=0, max=100, divisions=5)
    ]
)

switches = ft.Row(
    controls=[
        ft.Column(
            controls=[
                ft.Switch(value=False),
                ft.Switch(value=False, disabled=True)
            ]
        ),
        ft.Column(
            controls=[
                ft.Switch(value=True),
                ft.Switch(value=True, disabled=True)
            ]
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
)

time_picker = ft.TextButton("Show time picker")

# Text Input Components
text_inputs = ft.Column(
    controls=[
        ft.TextField(
            helper_text="supporting text"
        )
    ]
)

# Classifying Sections and SubSections

actions_section = Section(
    "Actions",
    [
        SubSection(
            "Common buttons",
            "Use ElevatedButton, FilledButton, FilledTonalButton, OutlinedButton or TextButton",
            common_buttons
        ),
        SubSection(
            "Floating buttons",
            "Use FloatingActionButton",
            floating_action_buttons
        ),
        SubSection(
            "Icon buttons",
            "Use ElevatedButton, FilledButton, FilledTonalButton, OutlinedButton or TextButton and set icon property",
            icon_buttons
        ),
    ]
)

communication_section = Section(
    "Communication",
    [
        SubSection(
            "Progress Indicators",
            "Use ProgressBar or ProgressRing",
            progress_indicators
        ),
        SubSection(
            "Snackbar",
            "Use page.show_snackbar with Snackbar",
            snackbar
        ),
    ]
)

containment_section = Section(
    "Containment",
    [
        SubSection(
            "Bottom sheet",
            "Use page.show_bottom_sheet with BottomSheet",
            bottom_sheet
        ),
        SubSection(
            "Dialog",
            "Use page.show_dialog with AlertDialog",
            dialogs
        ),
        SubSection(
            "Divider",
            "Use Divider or VerticalDivider",
            dividers
        )
    ]
)

navigation_section = Section(
    "Navigation",
    [

    ]
)

selection_section = Section(
    "Selection",
    [
        SubSection(
            "Checkboxes",
            "Use Checkbox",
            checkboxes
        ),
        SubSection(
            "Date picker",
            "Use ...",
            date_picker
        ),
        SubSection(
            "Menus",
            "Use PopupMenuButton, PopupMenuItem, and Dropdown",
            menus
        ),
        SubSection(
            "Radio buttons",
            "Use Radio and RadioGroup",
            radio_buttons
        ),
        SubSection(
            "Sliders",
            "Use Slider",
            sliders
        ),
        SubSection(
            "Switches",
            "Use Switch",
            switches
        ),
        SubSection(
            "Time picker",
            "Use ...",
            time_picker
        )

    ]
)

text_inputs_section = Section(
    "Text Inputs",
    [

    ]
)
