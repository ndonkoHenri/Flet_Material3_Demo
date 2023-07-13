import flet as ft
from screens import TypographyScreen, ComponentScreen, ColorScreen, ElevationScreen


class Main(object):
    def __init__(self):
        self.page: ft.Page | None = None

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "Flet Material 3 Demo"
        self.page.window_height, self.page.window_width = 550, 500
        # self.page.on_resize = lambda e: print(self.page.window_width)
        self.page.scroll = ft.ScrollMode.AUTO
        # self.page.window_always_on_top = True
        self.page.theme_mode = "light"
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=True)
        self.page.appbar = ft.AppBar(
            title=ft.Text("Material 3"),
            actions=[
                ft.IconButton(
                    ft.icons.DARK_MODE_OUTLINED,
                    selected_icon=ft.icons.WB_SUNNY_OUTLINED,
                    on_click=self.handle_brightness_change,
                    tooltip="Toggle brightness"
                ),
                ft.IconButton(
                    ft.icons.FILTER_2,
                    selected_icon=ft.icons.FILTER_3,
                    on_click=self.handle_material_version_change,
                    tooltip="Switch to Material 2"
                ),
                ft.PopupMenuButton(
                    content=ft.Icon(
                        ft.icons.COLOR_LENS_OUTLINED,
                    ),
                    items=[
                        ft.PopupMenuItem(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.COLOR_LENS_OUTLINED, color=clr),
                                    ft.Text(clr.title())
                                ]
                            ),
                            data=clr,
                            on_click=self.handle_seed_color_change
                        ) for clr in [
                            # "M3 Baseline", 
                            "indigo",
                            "blue",
                            "teal",
                            "green",
                            "yellow",
                            "orange",
                            "deeporange",
                            "pink"
                        ]
                    ],
                    tooltip="Select a seed color"
                ),
                ft.IconButton(
                    ft.icons.IMAGE_OUTLINED
                )
            ]
        )

        self.page.add(
            components,
            # typography
            # colors
        )

    def handle_brightness_change(self, e):
        e.control.selected = not e.control.selected
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def handle_material_version_change(self, e: ft.ControlEvent):
        # e.control.selected = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         nnnnn
        e.control.tooltip = f"Switch to Material {2 if self.page.theme.use_material3 == True else 3}"
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=not self.page.theme.use_material3)
        self.page.appbar.title.value = f"Material {3 if self.page.theme.use_material3 == True else 2}"
        self.page.update()

    def handle_seed_color_change(self, e):
        e.control.disabled = True
        self.page.theme.color_scheme_seed = self.page.dark_theme.color_scheme_seed = e.control.data
        self.page.update()


if __name__ == '__main__':
    ft.app(
        target=Main().run,
        view=ft.WEB_BROWSER
    )
