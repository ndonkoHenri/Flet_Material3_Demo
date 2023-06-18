# could be further separated in the future if too long and messy

import flet as ft


class MyContainer(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alignment = ft.alignment.center
        self.width = 420

    def _build(self):
        return self


common_buttons = MyContainer(
    content=ft.Row(
        [
            ft.Column(
                [
                    ft.ElevatedButton("Elevated", width=130),
                    ft.FilledButton("Filled", width=130),
                    ft.FilledTonalButton("Filled tonal", width=130),
                    ft.OutlinedButton("Outlined", width=130),
                    ft.TextButton("Text", width=130)
                ]
            ),
            ft.Column(
                [
                    ft.ElevatedButton("Icon", icon=ft.icons.ADD, width=130),
                    ft.FilledButton("Icon", icon=ft.icons.ADD, width=130),
                    ft.FilledTonalButton("Icon", icon=ft.icons.ADD, width=130),
                    ft.OutlinedButton("Icon", icon=ft.icons.ADD, width=130),
                    ft.TextButton("Icon", icon=ft.icons.ADD, width=130)
                ]
            ),
            ft.Column(
                [
                    ft.ElevatedButton("Elevated", disabled=True, width=130),
                    ft.FilledButton("Filled", disabled=True, width=130),
                    ft.FilledTonalButton("Filled tonal", disabled=True, width=130),
                    ft.OutlinedButton("Outlined", disabled=True, width=130),
                    ft.TextButton("Text", disabled=True, width=130)
                ]
            )
        ]
    )
)

floating_action_buttons = MyContainer(
    content=ft.Row(
        controls=[
            ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Small"),
            ft.FloatingActionButton("Create", icon=ft.icons.ADD, tooltip="extended"),
            ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Standard"),
            ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Large"),
        ]
    )
)

icon_buttons = MyContainer(
    content=ft.Column(
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
)

progress_indicators = MyContainer(
    alignment=None,
    content=ft.Row(
        controls=[
            ft.IconButton(ft.icons.PLAY_ARROW),
            ft.ProgressRing(value=0.7),
            ft.ProgressBar(value=0.7, width=320)
        ]
    )
)

snackbar = MyContainer(
    content=ft.TextButton("Show snackbar")
)

bottom_sheet = MyContainer(
    content=ft.Row(
        [
            ft.TextButton("Show modal bottom sheet"),
            ft.TextButton("Show bottom sheet")
        ]
    )
)

cards = MyContainer(
    content=ft.Text("To be Done")
)

dialogs = MyContainer(
    content=ft.Row(
        [
            ft.TextButton("Show dialog"),
            ft.TextButton("Show full-screen dialog")
        ]
    )
)

dividers = MyContainer(
    content=ft.Divider(height=5, thickness=1)
)
