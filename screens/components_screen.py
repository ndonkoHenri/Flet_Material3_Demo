import flet as ft
from Flet_Material3_Demo.utilities import ComponentSubSection, ComponentSection, BottomSheetButton, CardContainer, InputFields

# Actions Components

_cb_width = 125
_cb_width_icon = _cb_width - 25
_cb_height = 35
common_buttons = ft.Container(
    ft.Row(
        [
            ft.Column(
                [
                    ft.ElevatedButton("Elevated", width=_cb_width, height=_cb_height),
                    ft.FilledButton("Filled", width=_cb_width, height=_cb_height),
                    ft.FilledTonalButton("Filled tonal", width=_cb_width, height=_cb_height),
                    ft.OutlinedButton("Outlined", width=_cb_width, height=_cb_height),
                    ft.TextButton("Text", width=_cb_width, height=_cb_height)
                ],
            ),
            ft.Column(
                [
                    ft.ElevatedButton("Icon", icon=ft.icons.ADD, width=_cb_width_icon, height=_cb_height),
                    ft.FilledButton("Icon", icon=ft.icons.ADD, width=_cb_width_icon, height=_cb_height),
                    ft.FilledTonalButton("Icon", icon=ft.icons.ADD, width=_cb_width_icon, height=_cb_height),
                    ft.OutlinedButton("Icon", icon=ft.icons.ADD, width=_cb_width_icon, height=_cb_height),
                    ft.TextButton("Icon", icon=ft.icons.ADD, width=_cb_width_icon, height=_cb_height)
                ],
            ),
            ft.Column(
                [
                    ft.ElevatedButton("Elevated", width=_cb_width, height=_cb_height),
                    ft.FilledButton("Filled", width=_cb_width, height=_cb_height, disabled=True),
                    ft.FilledTonalButton("Filled tonal", width=_cb_width, height=_cb_height, disabled=True),
                    ft.OutlinedButton("Outlined", width=_cb_width, height=_cb_height),
                    ft.TextButton("Text", width=_cb_width, height=_cb_height)
                ],
                disabled=True,
            )
        ],
    ),
    padding=ft.Padding(2, 0, 5, 0)
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
        ft.IconButton(ft.icons.PLAY_ARROW, on_click=play_progress_indicators, expand=1),
        ft.ProgressRing(value=0.7, expand=1),
        ft.ProgressBar(value=0.7, expand=8)
    ]
)

snackbar = ft.TextButton(
    "Show snackbar",
    on_click=lambda e: e.page.show_snack_bar(
        ft.SnackBar(
            ft.Text("This is a snackbar.", color=ft.colors.SURFACE),
            action="Close",
        )
    )
)

# Containment Components

bs_func = lambda e: e.page.show_bottom_sheet(
    ft.BottomSheet(
        ft.Container(
            ft.Row(
                [
                    BottomSheetButton(ft.icons.SHARE_OUTLINED, "Share"),
                    BottomSheetButton(ft.icons.ADD, "Add to"),
                    BottomSheetButton(ft.icons.TRANSIT_ENTEREXIT_SHARP, "Trash"),
                    BottomSheetButton(ft.icons.ARCHIVE_OUTLINED, "Archive"),
                    BottomSheetButton(ft.icons.SETTINGS_OUTLINED, "Settings"),
                    BottomSheetButton(ft.icons.FAVORITE_BORDER, "Favorite"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            padding=25,
            height=125
        ),
        # on_dismiss=bs_dismissed,
        dismissible=True,
        show_drag_handle=True,  # if ... modal or not,
        enable_drag=True,
    )
)

bottom_sheet = ft.Row(
    [
        ft.TextButton("Show modal bottom sheet", on_click=bs_func),
        ft.TextButton("Show bottom sheet", on_click=bs_func)
    ]
)

_card_width = 115

cards = ft.Row(
    controls=[
        ft.Card(
            width=_card_width,
            content=CardContainer("Elevated")
        ),
        ft.Card(
            color=ft.colors.SURFACE_VARIANT,
            elevation=0,
            width=_card_width,
            content=CardContainer("Filled")
        ),
        ft.Card(
            width=_card_width,
            elevation=0,
            content=CardContainer("Outlined")
        )
    ]
)


def close_dlg(e: ft.ControlEvent):
    e.control.page.dialog.open = False
    e.control.page.update()


alert_dialog = ft.AlertDialog(
    title=ft.Text("What is a Dialog?"),
    content=ft.Text(
        "A dialog is a type of modal window that appears in front of app content to provide critical information, or prompt for a decision to be made."),
    actions=[
        ft.TextButton("Okay", on_click=close_dlg),
        ft.ElevatedButton("Dismiss", on_click=close_dlg)
    ],
    actions_alignment=ft.MainAxisAlignment.END
)


def show_dlg(e: ft.ControlEvent):
    if e.control.data == 1:
        e.control.page.dialog = alert_dialog
    else:
        # e.control.page.dialog = full_screen_dialog
        pass
    e.control.page.dialog.open = True
    e.control.page.update()


dialogs = ft.Row(
    [
        ft.TextButton("Show dialog", on_click=show_dlg, data=1),
        ft.TextButton("Show full-screen dialog", on_click=show_dlg)
    ],
    alignment=ft.MainAxisAlignment.CENTER
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
        i.name = e.control.value.lower()
    elif e.control.data == "color":
        i.color = e.control.value.lower()
    i.update()


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
                    ft.Icon(ft.icons.MORE_VERT),
                    items=[
                        ft.PopupMenuItem(content=ft.Text("Menu 1")),
                        ft.PopupMenuItem(content=ft.Text("Menu 2")),
                        ft.PopupMenuItem(content=ft.Text("Menu 3"), )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
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
                    width=130,
                    content_padding=ft.Padding(10, 2, 1, 2)
                ),
                ft.Dropdown(
                    label="Icon",
                    prefix_icon=ft.icons.SEARCH,
                    options=[
                        # ft.dropdown.Option("Smile"),
                        ft.dropdown.Option("Cloud"),
                        ft.dropdown.Option("Brush"),
                        ft.dropdown.Option("Favorite"),
                    ],
                    value="Cloud",
                    on_change=dropdown_change,
                    data="icon",
                    width=165,
                    content_padding=2
                ),
                ft.Icon(ft.icons.CLOUD)
            ],
            height=50
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
        ft.Slider(min=0, max=100, divisions=5, label="{value}")
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
    alignment=ft.MainAxisAlignment.SPACE_AROUND
)

time_picker = ft.TextButton("Show time picker")

# Text Input Components


text_inputs = ft.Column(
    controls=[
        InputFields("filled"),
        InputFields("outlined")
    ]
)

# Classifying Sections and SubSections

actions_section = ComponentSection(
    "Actions",
    [
        ComponentSubSection(
            "Common buttons",
            "Use ElevatedButton, FilledButton, FilledTonalButton, OutlinedButton or TextButton",
            common_buttons
        ),
        ComponentSubSection(
            "Floating buttons",
            "Use FloatingActionButton",
            floating_action_buttons
        ),
        ComponentSubSection(
            "Icon buttons",
            "Use ElevatedButton, FilledButton, FilledTonalButton, OutlinedButton or TextButton and set icon property",
            icon_buttons
        ),
    ]
)

communication_section = ComponentSection(
    "Communication",
    [
        ComponentSubSection(
            "Progress Indicators",
            "Use ProgressBar or ProgressRing",
            progress_indicators
        ),
        ComponentSubSection(
            "Snackbar",
            "Use page.show_snackbar with Snackbar",
            snackbar
        ),
    ]
)

containment_section = ComponentSection(
    "Containment",
    [
        ComponentSubSection(
            "Bottom sheet",
            "Use page.show_bottom_sheet with BottomSheet",
            bottom_sheet
        ),
        ComponentSubSection(
            "Cards",
            "Use Card",
            cards
        ),
        ComponentSubSection(
            "Dialog",
            "Use page.show_dialog with AlertDialog",
            dialogs
        ),
        ComponentSubSection(
            "Divider",
            "Use Divider or VerticalDivider",
            dividers
        )
    ]
)

navigation_section = ComponentSection(
    "Navigation",
    [

    ]
)

selection_section = ComponentSection(
    "Selection",
    [
        ComponentSubSection(
            "Checkboxes",
            "Use Checkbox",
            checkboxes
        ),
        ComponentSubSection(
            "Date picker",
            "Use ...",
            date_picker
        ),
        ComponentSubSection(
            "Menus",
            "Use PopupMenuButton, PopupMenuItem, and Dropdown",
            menus
        ),
        ComponentSubSection(
            "Radio buttons",
            "Use Radio and RadioGroup",
            radio_buttons
        ),
        ComponentSubSection(
            "Sliders",
            "Use Slider",
            sliders
        ),
        ComponentSubSection(
            "Switches",
            "Use Switch",
            switches
        ),
        ComponentSubSection(
            "Time picker",
            "Use ...",
            time_picker
        )

    ]
)

text_inputs_section = ComponentSection(
    "Text Inputs",
    [
        ComponentSubSection(
            "Text fields",
            "Use TextField",
            text_inputs
        )
    ]
)

components = (
    actions_section,
    communication_section,
    containment_section,
    navigation_section,
    selection_section,
    text_inputs_section
)
