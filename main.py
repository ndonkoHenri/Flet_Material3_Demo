import flet as ft
from screens import TypographyScreen, ComponentScreen, ColorScreen, ElevationScreen


class Main:
    def __init__(self):
        self.page: ft.Page | None = None
        self.screens = [ComponentScreen(), ColorScreen(), TypographyScreen(), ElevationScreen()]
        self.width_breakpoint = 994
        self.nav_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.NONE,
            group_alignment=-1.0,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_INPUT_COMPONENT_OUTLINED,
                    selected_icon=ft.icons.SETTINGS_INPUT_COMPONENT,
                    label="Components"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FORMAT_PAINT_OUTLINED,
                    selected_icon=ft.icons.FORMAT_PAINT,
                    label="Colors"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.TYPE_SPECIMEN_OUTLINED,
                    selected_icon=ft.icons.TYPE_SPECIMEN,
                    label="Typography"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FORMAT_PAINT_OUTLINED,
                    selected_icon=ft.icons.FORMAT_PAINT,
                    label="Elevation"
                )
            ],
            on_change=self.handle_nav_rail_change,
            trailing=ft.Column(self._action_buttons(), alignment=ft.MainAxisAlignment.END),
            # visible=True if self.page.width >= self.width_breakpoint else False,
            expand=1,
            height=800
        )

    def _action_buttons(self):
        actions = [
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
                tooltip="Switch to Material 2",
            ),
            ft.PopupMenuButton(
                icon=ft.icons.COLOR_LENS_OUTLINED,
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

        return actions

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "Flet Material 3 Demo"
        self.page.window_height, self.page.window_width = 550, 1000
        self.page.on_resize = self.handle_page_resize
        self.page.on_route_change = self.handle_route_change
        self.page.on_view_pop = self.handle_view_pop
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.padding = ft.Padding(5, 0, 5, 0)
        # self.page.window_always_on_top = True
        self.page.theme_mode = "light"
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=True)
        self.nav_rail.visible = True if self.page.width >= self.width_breakpoint else False
        self.page.floating_action_button_location = ft.FloatingActionButtonLocation.END_CONTAINED

        self.page.time_picker = ft.TimePicker(
            confirm_text="OK",
            error_invalid_text="Time out of range",
            help_text="Select time",
            on_change=lambda e: e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Selected time: {e.control.value.strftime('%H:%M %p')}"))),
            #on_dismiss=dismissed,
        )

        self.page.overlay.append(self.page.time_picker)

        self.page.appbar = ft.AppBar(
            title=ft.Text("Material 3"),
            actions=[
                ft.Row(self._action_buttons(), visible=False if self.page.width >= self.width_breakpoint else True)
            ],
        )
        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS_INPUT_COMPONENT_OUTLINED,
                    selected_icon=ft.icons.SETTINGS_INPUT_COMPONENT,
                    label="Components"
                ),
                ft.NavigationDestination(
                    icon=ft.icons.FORMAT_PAINT_OUTLINED,
                    selected_icon=ft.icons.FORMAT_PAINT,
                    label="Colors"
                ),
                ft.NavigationDestination(
                    icon=ft.icons.TYPE_SPECIMEN_OUTLINED,
                    selected_icon=ft.icons.TYPE_SPECIMEN,
                    label="Typography"
                ),
                ft.NavigationDestination(
                    icon=ft.icons.FORMAT_PAINT_OUTLINED,
                    selected_icon=ft.icons.FORMAT_PAINT,
                    label="Elevation"
                ),
            ],
            on_change=self.handle_nav_bar_change,
            visible=False if self.page.width >= self.width_breakpoint else True
        )

        self.page.add(
            ft.Row(
                controls=[
                    self.nav_rail,
                    self.screens[0]
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        )

    def handle_brightness_change(self, e):
        e.control.selected = not e.control.selected
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def handle_material_version_change(self, e):
        e.control.selected = not e.control.selected
        self.page.theme = self.page.dark_theme = ft.Theme(use_material3=not self.page.theme.use_material3)
        e.control.tooltip = f"Switch to Material {2 if self.page.theme.use_material3 == True else 3}"
        self.page.appbar.title.value = f"Material {3 if self.page.theme.use_material3 == True else 2}"
        self.page.update()

    def handle_seed_color_change(self, e):
        self.page.theme.color_scheme_seed = self.page.dark_theme.color_scheme_seed = e.control.data
        # update icon of the selected color
        for i, j in zip(self.page.appbar.actions[0].controls[2].items, self.nav_rail.trailing.controls[2].items):
            # deactivate all
            if i.content.controls[0].name == ft.icons.COLOR_LENS:
                i.content.controls[0].name = ft.icons.COLOR_LENS_OUTLINED
                j.content.controls[0].name = ft.icons.COLOR_LENS_OUTLINED
            # set the clicked one
            if i.content.controls[0].color == e.control.data:
                i.content.controls[0].name = ft.icons.COLOR_LENS
                j.content.controls[0].name = ft.icons.COLOR_LENS
        self.page.update()

    def handle_page_resize(self, e):
        # print(self.page.width, self.page.window_width, self.page.height, self.page.window_height)
        if self.page.width >= self.width_breakpoint:
            self.page.navigation_bar.visible = False
            self.nav_rail.visible = True
            self.page.appbar.actions[0].visible = False
        else:
            self.page.navigation_bar.visible = True
            self.nav_rail.visible = False
            self.page.appbar.actions[0].visible = True

        self.page.update()

    def handle_nav_bar_change(self, e: ft.ControlEvent):
        self.page.controls[0].controls[-1] = self.screens[int(e.data)]
        self.page.update()

    def handle_nav_rail_change(self, e: ft.ControlEvent):
        self.page.controls[0].controls[-1] = self.screens[int(e.data)]
        self.page.update()

    def handle_route_change(self, e: ft.RouteChangeEvent):
        if e.route == "/a":
            self.page.views.append(
                ft.View(
                    e.route,
                    [
                        ft.AppBar(
                            title=ft.Text("Full-screen dialog"),
                            actions=[ft.TextButton("Close", on_click=self.handle_view_pop)]
                        ),
                    ],
                    fullscreen_dialog=True
                )
            )
            self.page.update()

    def handle_view_pop(self, v: ft.ViewPopEvent):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(
    target=Main().run,
    view=ft.WEB_BROWSER
)
