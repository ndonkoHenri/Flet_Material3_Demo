import flet as ft
from .section import Section, SubSection

cb_width = 130
common_buttons = ft.Row(
    [
        ft.Column(
            [
                ft.ElevatedButton("Elevated", width=cb_width),
                ft.FilledButton("Filled", width=cb_width),
                ft.FilledTonalButton("Filled tonal", width=cb_width),
                ft.OutlinedButton("Outlined", width=cb_width),
                ft.TextButton("Text", width=cb_width)
            ]
        ),
        ft.Column(
            [
                ft.ElevatedButton("Icon", icon=ft.icons.ADD, width=cb_width),
                ft.FilledButton("Icon", icon=ft.icons.ADD, width=cb_width),
                ft.FilledTonalButton("Icon", icon=ft.icons.ADD, width=cb_width),
                ft.OutlinedButton("Icon", icon=ft.icons.ADD, width=cb_width),
                ft.TextButton("Icon", icon=ft.icons.ADD, width=cb_width)
            ]
        ),
        ft.Column(
            [
                ft.ElevatedButton("Elevated", width=cb_width),
                ft.FilledButton("Filled", width=cb_width, disabled=True),
                ft.FilledTonalButton("Filled tonal", width=cb_width, disabled=True),
                ft.OutlinedButton("Outlined", width=cb_width),
                ft.TextButton("Text", width=cb_width)
            ],
            disabled=True
        )
    ]
)

floating_action_buttons = ft.Row(
    controls=[
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Small"),
        ft.FloatingActionButton("Create", icon=ft.icons.ADD, tooltip="Extended"),
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Standard"),
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Large"),
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

alert_dialog = ft.AlertDialog(
    title=ft.Text("What is a Dialog?"),
    content=ft.Text(
        "A dialog is a type of modal window that appears in front of app content to provide critical information, or prompt for a decision to be made."),
    actions=[
        ft.TextButton("Okay"),
        ft.ElevatedButton("Dismiss")
    ]
)


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
        ft.ProgressBar(value=0.7, width=320)
    ]
)

snackbar = ft.TextButton("Show snackbar")

bottom_sheet = ft.Row(
    [
        ft.TextButton("Show modal bottom sheet"),
        ft.TextButton("Show bottom sheet")
    ]
)

cards = ft.Text("To be Done")

dialogs = ft.Row(
    [
        ft.TextButton("Show dialog"),
        ft.TextButton("Show full-screen dialog")
    ]
)

dividers = ft.Divider(height=5, thickness=1)

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

    ]
)

text_inputs_section = Section(
    "Text Inputs",
    [

    ]
)
