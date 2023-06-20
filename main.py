import flet as ft
from utilities import *


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
                ft.IconButton(ft.icons.SHIELD_MOON, on_click=self.handle_brightness_change),
                ft.IconButton(ft.icons.LOOKS_TWO_OUTLINED, on_click=self.handle_material_version_change, tooltip="Use Material 2"),
                ft.IconButton(ft.icons.FORMAT_PAINT_ROUNDED),
                ft.IconButton(ft.icons.IMAGE_OUTLINED)
            ]
        )

        self.page.add(
            actions_section,
            communication_section,
            containment_section,
            navigation_section,
            selection_section,
            text_inputs_section
        )

    def handle_brightness_change(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def handle_material_version_change(self, e):
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=not self.page.theme.use_material3)
        e.control.tooltip = f"Use Material {2 if self.page.theme.use_material3==True else 3}"
        self.page.appbar.title.value = f"Material {3 if self.page.theme.use_material3==True else 2}"
        self.page.update()


if __name__ == '__main__':
    ft.app(target=Main().run)
