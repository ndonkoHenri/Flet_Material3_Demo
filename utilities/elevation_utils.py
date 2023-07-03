import flet as ft
from typing import List, Optional


class ElevationCard(ft.Card):
    def __init__(self, info, shadow_color=None, surface_tint=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.surface_tint_color = surface_tint
        self.shadow_color = shadow_color
        self.color = ft.colors.SURFACE
        self.elevation = info[1]
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        ft.Column(
                            controls=[
                                ft.Text(f"Level {info[0]}\n{info[1]} dp", style=ft.TextThemeStyle.BODY_SMALL)
                            ]
                        ),
                        alignment=ft.alignment.top_left,
                        padding=10
                    ),
                    ft.Container(
                        ft.Text(
                            f"{info[2]}%", style=ft.TextThemeStyle.BODY_SMALL,
                            opacity=0 if surface_tint is None and shadow_color is not None else 1
                                ),
                        alignment=ft.alignment.bottom_right,
                        padding=10
                    )
                ],
            ),
            border_radius=4,
            padding=10
        )


class ElevationSection(ft.Container):
    def __init__(
            self,
            title: str,
            shadow_color=None,
            surface_tint=None,
            is_top=False,
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.title: str = title
        cards_grid = ft.GridView(runs_count=6, padding=8)

        # level, elevation, overlayPercent
        p = [(0, 0, 0), (1, 1, 5), (2, 3, 8), (3, 6, 11), (4, 8, 12), (5, 12, 14)]

        for tup in p:
            cards_grid.controls.append(
                ElevationCard(tup, shadow_color, surface_tint)
            )

        self.content = ft.Column(
            controls=[
                ft.Text(self.title, style=ft.TextThemeStyle.TITLE_LARGE),
                cards_grid
            ]
        )

        self.padding = ft.Padding(16, 20 if is_top else 8, 16, 0)
