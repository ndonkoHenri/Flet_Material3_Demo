from typing import List, Tuple, Literal
import flet as ft


class ColorContainer(ft.Container):
    def __init__(self, colors: List[Tuple[str, str]], theme_mode: ft.ThemeMode):
        super().__init__(theme_mode=theme_mode)
        m = 14
        self.margin = ft.Margin(m, 0, 0, 0) if theme_mode == ft.ThemeMode.LIGHT else ft.Margin(0, 0, m, 0)

        self.border_radius = 10

        self.content = ft.Column(
            controls=[
                ft.Container(
                    bgcolor=bg[0].lower(),
                    content=ft.Text(bg[1], color=bg[1]),
                    height=53,
                    alignment=ft.alignment.center_left,
                    padding=ft.Padding(10, 0, 0, 0),
                    theme_mode=theme_mode
                ) for bg in colors
            ],
            spacing=0,
        )
