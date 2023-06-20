import flet as ft
from utilities import actions_section


class Main(object):
    def __init__(self):
        self.page: ft.Page | None = None

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "Flet Material 3 Demo"
        self.page.scroll = ft.ScrollMode.AUTO
        # self.page.window_always_on_top = True
        self.page.theme_mode = "light"
        self.page.horizontal_alignment = self.page.vertical_alignment = "center"
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=True)
        self.page.appbar = ft.AppBar(
            title=ft.Text("Material 3"),
            actions=[
                ft.IconButton(ft.icons.SHIELD_MOON),
                ft.IconButton(ft.icons.LOOKS_TWO_OUTLINED),
                ft.IconButton(ft.icons.FORMAT_PAINT_ROUNDED),
                ft.IconButton(ft.icons.IMAGE_OUTLINED)
            ]
        )

        self.page.add(
            actions_section
        )

# def main(page: ft.Page):
#     page.title = "Flet Material 3 Demo"
#     page.scroll = ft.ScrollMode.AUTO
#     page.theme_mode = ft.ThemeMode.LIGHT
#     # page.window_always_on_top = True
#     page.horizontal_alignment = page.vertical_alignment = "center"
#     page.theme = page.dark_theme = ft.Theme(use_material3=True)
#
#     page.appbar = ft.AppBar(
#         title=ft.Text("Material 3"),
#         actions=[
#             ft.IconButton(ft.icons.SHIELD_MOON),
#             ft.IconButton(ft.icons.LOOKS_TWO_OUTLINED),
#             ft.IconButton(ft.icons.FORMAT_PAINT_ROUNDED),
#             ft.IconButton(ft.icons.IMAGE_OUTLINED)
#         ]
#     )
#
#     page.add(
#         utils.common_buttons,
#         utils.floating_action_buttons,
#         utils.icon_buttons,
#         utils.progress_indicators,
#         utils.snackbar,
#         utils.bottom_sheet,
#         utils.cards,
#         utils.dialogs,
#         utils.dividers
#     )


if __name__ == '__main__':
    ft.app(target=Main().run)