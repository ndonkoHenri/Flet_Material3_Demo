import flet as ft
from utilities import ComponentSubSection, ComponentSection, BottomSheetButton, CardContainer, InputFields

# Actions Components

_cb_width = 125
_cb_width_icon = _cb_width - 25
_cb_height = 35
common_buttons = ft.Row(
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
    alignment=ft.MainAxisAlignment.CENTER
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


def _icon_clicked(e):
    if isinstance(e.control, ft.IconButton):
        e.control.selected = not e.control.selected

    else:
        e.control.content.name = "settings_outlined" if e.control.content.name == "settings" else "settings"

        if isinstance(e.control, ft.OutlinedButton):
            e.control.style.bgcolor = ft.colors.INVERSE_SURFACE if e.control.content.name == "settings" else None

    icon_buttons.update()


icon_buttons = ft.Column(
    controls=[
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected=False,
                    selected_icon=ft.icons.SETTINGS,
                    on_click=_icon_clicked
                ),
                ft.FilledButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6),
                    # bgcolor=ft.colors.TRANSPARENT,
                    on_click=_icon_clicked,

                ),
                ft.FilledTonalButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6),
                    on_click=_icon_clicked
                ),
                ft.OutlinedButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6, bgcolor=None),
                    on_click=_icon_clicked,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.SETTINGS_OUTLINED),
                ft.FilledButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6),
                    disabled=True
                ),
                ft.FilledTonalButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6),
                    disabled=True
                ),
                ft.OutlinedButton(
                    content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=6),
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            disabled=True
        )
    ]
)

segmented_buttons = ft.Column(
    controls=[
        ft.SegmentedButton(
            selected={"Day"},
            segments=[
                ft.Segment("Day", label=ft.Text("Day"), icon=ft.icons.CALENDAR_VIEW_DAY),
                ft.Segment("Week", label=ft.Text("Week"), icon=ft.icons.CALENDAR_VIEW_WEEK),
                ft.Segment("Month", label=ft.Text("Month"), icon=ft.icons.CALENDAR_VIEW_MONTH),
                ft.Segment("Year", label=ft.Text("Year"), icon=ft.icons.CALENDAR_TODAY),
            ]
        ),
        ft.SegmentedButton(
            selected={"L", "XL"},
            allow_multiple_selection=True,
            segments=[
                ft.Segment("XS", label=ft.Text("XS")),
                ft.Segment("S", label=ft.Text("S")),
                ft.Segment("M", label=ft.Text("M")),
                ft.Segment("L", label=ft.Text("L")),
                ft.Segment("XL", label=ft.Text("XL")),
            ]
        )
    ]
)

# Communication Components
badges = ft.NavigationBar(
    destinations=[
        ft.NavigationDestination(
            icon_content=ft.Badge(ft.Icon(ft.icons.EMAIL_OUTLINED), text="999+"),
            selected_icon_content=ft.Badge(ft.Icon(ft.icons.EMAIL), text="999+"),
            label="Mail"
        ),
        ft.NavigationDestination(
            icon_content=ft.Badge(ft.Icon(ft.icons.PEOPLE_OUTLINE_SHARP), text="10"),
            selected_icon_content=ft.Badge(ft.Icon(ft.icons.PEOPLE_SHARP), text="10"),
            label="Chat"
        ),
        ft.NavigationDestination(
            icon_content=ft.Badge(ft.Icon(ft.icons.ACCOUNT_BOX_OUTLINED)),
            selected_icon_content=ft.Badge(ft.Icon(ft.icons.ACCOUNT_BOX)),
            label="Rooms"
        ),
        ft.NavigationDestination(
            icon_content=ft.Badge(ft.Icon(ft.icons.VIDEOCAM_OUTLINED), text="3"),
            selected_icon_content=ft.Badge(ft.Icon(ft.icons.VIDEOCAM), text="3"),
            label="Meet"
        )
    ],
)


def _play_progress_indicators(e):
    if not progress_indicators.controls[1].value:
        progress_indicators.controls[1].value = progress_indicators.controls[2].value = 0.7
    else:
        progress_indicators.controls[1].value = progress_indicators.controls[2].value = None

    progress_indicators.update()


progress_indicators = ft.Row(
    controls=[
        ft.IconButton(ft.icons.PLAY_ARROW, on_click=_play_progress_indicators, expand=1),
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
            width=365,
            behavior=ft.SnackBarBehavior.FLOATING,
            duration=8000,
            # dismiss_direction=ft.DismissDirection.HORIZONTAL
        )
    )
)

# Containment Components

bs_func = lambda e, modal: e.page.show_bottom_sheet(
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
        dismissible=True,
        show_drag_handle=modal,
        enable_drag=True,
    )
)

bottom_sheet = ft.Row(
    [
        ft.TextButton("Show modal bottom sheet", on_click=lambda e: bs_func(e, modal=True)),
        ft.TextButton("Show bottom sheet", on_click=lambda e: bs_func(e, modal=False))
    ],
    alignment=ft.MainAxisAlignment.CENTER
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


def _close_dlg(e: ft.ControlEvent):
    e.control.page.dialog.open = False
    e.control.page.update()


alert_dialog = ft.AlertDialog(
    title=ft.Text("What is a Dialog?"),
    content=ft.Text(
        "A dialog is a type of modal window that appears in front of app content to provide critical information, or prompt for a decision to be made."),
    actions=[
        ft.TextButton("Okay", on_click=_close_dlg),
        ft.ElevatedButton("Dismiss", on_click=_close_dlg)
    ],
    actions_alignment=ft.MainAxisAlignment.END
)


def _show_dlg(e: ft.ControlEvent):
    match e.control.data:
        case 1:
            e.control.page.dialog = alert_dialog
            e.control.page.dialog.open = True
        case 2:
            e.page.go("/a")

    e.control.page.update()


dialogs = ft.Row(
    [
        ft.TextButton("Show dialog", on_click=_show_dlg, data=1),
        ft.TextButton("Show full-screen dialog", on_click=_show_dlg, data=2)
    ],
    alignment=ft.MainAxisAlignment.CENTER
)

dividers = ft.Divider(height=5, thickness=1)


# Navigation Components
def _fab_hover(e):
    e.control.content.elevation = 5 if e.control.content.elevation == 0 else 0
    e.page.update()


bottom_appbar = ft.BottomAppBar(
    bgcolor=ft.colors.SURFACE_VARIANT,
    content=ft.Row(
        [
            ft.IconButton(ft.icons.MENU, tooltip="Menu"),
            ft.IconButton(ft.icons.SEARCH, tooltip="Search"),
            ft.IconButton(ft.icons.FAVORITE, tooltip="Favorite"),
            ft.Container(expand=True),
            ft.FloatingActionButton(icon=ft.icons.ADD)
        ]
    )
)

navbar = ft.NavigationBar(
    destinations=[
        ft.NavigationDestination(
            icon=ft.icons.EXPLORE_OUTLINED,
            selected_icon=ft.icons.EXPLORE,
            label="Explore"
        ),
        ft.NavigationDestination(
            icon=ft.icons.PETS_OUTLINED,
            selected_icon=ft.icons.PETS,
            label="Pets"
        ),
        ft.NavigationDestination(
            icon=ft.icons.ACCOUNT_BOX_OUTLINED,
            selected_icon=ft.icons.ACCOUNT_BOX,
            label="Account"
        )
    ],
)

nd = ft.NavigationDrawer(
    controls=[
        ft.Container(
            ft.Text("Mail", style=ft.TextThemeStyle.TITLE_SMALL),
            padding=ft.Padding(28, 16, 16, 10),
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.INBOX_OUTLINED,
            selected_icon=ft.icons.INBOX,
            label="Inbox"
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.SEND_OUTLINED,
            selected_icon=ft.icons.SEND,
            label="Outbox"
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.FAVORITE_BORDER,
            selected_icon=ft.icons.FAVORITE,
            label="Favorites"
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.DELETE_OUTLINED,
            selected_icon=ft.icons.DELETE,
            label="Trash"
        ),
        ft.Divider(height=5, thickness=1),
        ft.Container(
            ft.Text("Labels", style=ft.TextThemeStyle.TITLE_SMALL),
            padding=ft.Padding(28, 16, 16, 10),
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.BOOKMARK_BORDER,
            selected_icon=ft.icons.BOOKMARK,
            label="Family"
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.BOOKMARK_BORDER,
            selected_icon=ft.icons.BOOKMARK,
            label="School"
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.BOOKMARK_BORDER,
            selected_icon=ft.icons.BOOKMARK,
            label="Work"
        )
    ]
)

navdrawer = ft.Column(
    [
        ft.TextButton("Show Navigation Drawer", on_click=lambda e: e.page.show_end_drawer(nd)),
    ]
)

navrail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.SELECTED,
    group_alignment=0.0,
    expand=1,
    height=350,
    leading=ft.FloatingActionButton(icon=ft.icons.CREATE),
    destinations=[
        ft.NavigationRailDestination(
            icon=ft.icons.INBOX_OUTLINED,
            selected_icon=ft.icons.INBOX,
            label="Inbox"
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.SEND_OUTLINED,
            selected_icon=ft.icons.SEND,
            label="Outbox"
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.FAVORITE_BORDER,
            selected_icon=ft.icons.FAVORITE,
            label="Favorites"
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.DELETE_OUTLINED,
            selected_icon=ft.icons.DELETE,
            label="Trash"
        )
    ],
)

tabs = ft.Tabs(
    tabs=[
        ft.Tab(
            "Video",
            icon=ft.icons.VIDEO_CALL
        ),
        ft.Tab(
            "Photo",
            icon=ft.icons.PHOTO
        ),
        ft.Tab(
            "Audio",
            icon=ft.icons.AUDIOTRACK
        )
    ],
)

# Selection Components
checkboxes = ft.ListView(
    controls=[
        ft.ListTile(title=ft.Text("Option 1"), trailing=ft.Checkbox(value=True, tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 2"), trailing=ft.Checkbox(value=True, tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 3"), trailing=ft.Checkbox(tristate=True), toggle_inputs=True),
        ft.ListTile(title=ft.Text("Option 4"), trailing=ft.Checkbox(value=False), disabled=True)
    ]
)

chips = ft.Column(
    controls=[
        ft.Row(
            controls=[

                ft.Chip(ft.Text("Assist"), leading=ft.Icon(ft.icons.EVENT, color="blue"),
                        on_click=lambda e: e.page.update(), disabled=state),
                ft.Chip(ft.Text("Filter"), show_checkmark=True, selected=True, on_select=lambda e: e.page.update(),
                        disabled=state),
                ft.Chip(ft.Text("Input"), on_delete=lambda e: e.page.update(), disabled=state),
                ft.Chip(ft.Text("Suggestion"), on_click=lambda e: e.page.update(), disabled=state),
            ]
        )
        for state in [False, True]
    ]
)

date_picker = ft.TextButton("Show date picker")


def _dropdown_change(e):
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
                    icon=ft.icons.MORE_VERT,
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
                    on_change=_dropdown_change,
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
                    on_change=_dropdown_change,
                    data="icon",
                    width=165,
                    content_padding=2
                ),
                ft.Icon(ft.icons.CLOUD)
            ],
            height=50,
            alignment=ft.MainAxisAlignment.CENTER
        )
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
                ft.Switch(value=True, thumb_icon=ft.icons.CHECK),
                ft.Switch(value=True, thumb_icon=ft.icons.CHECK, disabled=True)
            ]
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_AROUND
)

time_picker = ft.TextButton("Show time picker", on_click=lambda e: e.page.time_picker.pick_time())

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
        ComponentSubSection(
            "Segmented buttons",
            "Use SegmentedButton and Segment",
            icon_buttons
        ),
    ]
)

communication_section = ComponentSection(
    "Communication",
    [
        ComponentSubSection(
            "Badges",
            "Use ..",
            badges
        ),
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
        ComponentSubSection(
            "Bottom app bar",
            "Use BottomAppBar",
            bottom_appbar
        ),
        ComponentSubSection(
            "Navigation Bar",
            "Use NavigationBar and NavigationDestination",
            navbar
        ),
        ComponentSubSection(
            "Navigation Drawer",
            "Use NavigationDrawer and NavigationDrawerDestination",
            navdrawer
        ),
        ComponentSubSection(
            "Navigation Rail",
            "Use NavigationRail and NavigationRailDestination",
            navrail
        ),
        ComponentSubSection(
            "Tabs",
            "Use Tabs and Tab",
            tabs
        ),
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
            "Use DatePicker",
            date_picker
        ),
        ComponentSubSection(
            "Chips",
            "Use Chip",
            chips
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
            "Use TimePicker",
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


class ComponentScreen(ft.ResponsiveRow):
    def __init__(self):
        super().__init__(expand=19)
        self.controls = [
            ft.Column(
                controls=[
                    actions_section,
                    communication_section,
                    containment_section
                ],
                col={"lg": 6, "sm": 12},
                scroll=ft.ScrollMode.HIDDEN
            ),
            ft.Column(
                controls=[
                    navigation_section,
                    selection_section,
                    text_inputs_section
                ],
                col={"lg": 6, "sm": 12},
                scroll=ft.ScrollMode.AUTO
            )
        ]
