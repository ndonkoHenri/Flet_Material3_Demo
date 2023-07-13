import flet as ft
from Flet_Material3_Demo.utilities import ColorContainer

containers_spacing = 18
d = [
    [
        ("primary", "onPrimary"), ("onPrimary", "primary"),
        ("primaryContainer", "onPrimaryContainer"),
        ("onPrimaryContainer", "primaryContainer")
    ],
    [
        ("secondary", "onSecondary"), ("onSecondary", "secondary"),
        ("secondaryContainer", "onSecondaryContainer"), ("onSecondaryContainer", "secondaryContainer")
    ],
    [
        ("tertiary", "onTertiary"), ("onTertiary", "tertiary"),
        ("tertiaryContainer", "onTertiaryContainer"), ("onTertiaryContainer", "tertiaryContainer")
    ],
    [
        ("error", "onError"), ("onError", "error"),
        ("errorContainer", "onErrorContainer"), ("onErrorContainer", "errorContainer")
    ],
    [("background", "onBackground"), ("onBackground", "background")],
    [
        ("surface", "onSurface"), ("onSurface", "surface"),
        ("surfaceVariant", "onSurfaceVariant"), ("onSurfaceVariant", "surfaceVariant")
    ],
    [
        ("outline", "shadow"), ("shadow", "outline"), ("inverseSurface", "onInverseSurface"),
        ("onInverseSurface", "inverseSurface"), ("inversePrimary", "primary")
    ]
]


class ColorScreen(ft.Row):
    def __init__(self):
        super().__init__(spacing=35, expand=19)
        self.controls = [
            ft.Column(
                controls=[
                    ft.Text(f"{theme_mode.value.title()} ColorScheme", weight=ft.FontWeight.BOLD, size=20),
                    ft.Column(
                        controls=[ColorContainer(color_list, theme_mode) for color_list in d],
                        spacing=containers_spacing,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                expand=1,
            ) for theme_mode in [ft.ThemeMode.LIGHT, ft.ThemeMode.DARK]
        ]
