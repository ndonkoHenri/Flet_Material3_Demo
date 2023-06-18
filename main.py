import flet as ft
import utils


def main(page: ft.Page):
    page.title = "Flet Material 3 Demo"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.window_always_on_top = True
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.theme = page.dark_theme = ft.Theme(use_material3=True)

    page.appbar = ft.AppBar(
        title=ft.Text("Material 3"),
        actions=[
            ft.IconButton(ft.icons.SHIELD_MOON),
            ft.IconButton(ft.icons.LOOKS_TWO_OUTLINED),
            ft.IconButton(ft.icons.FORMAT_PAINT_ROUNDED),
            ft.IconButton(ft.icons.IMAGE_OUTLINED)
        ]
    )

    page.add(
        utils.common_buttons,
        utils.floating_action_buttons,
        utils.icon_buttons,
        utils.progress_indicators,
        utils.snackbar,
        utils.bottom_sheet,
        utils.cards,
        utils.dialogs,
        utils.dividers
    )


ft.app(
    main
)
