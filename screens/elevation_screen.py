import flet as ft
from Flet_Material3_Demo.utilities import ElevationSection

elevation = ft.Column(
    controls=[
        ElevationSection("Surface Tint Only", surface_tint=ft.colors.PRIMARY, is_top=True),
        ElevationSection("Surface Tint and Shadow", surface_tint=ft.colors.PRIMARY, shadow_color=ft.colors.SHADOW),
        ElevationSection("Shadow Only", shadow_color=ft.colors.SHADOW),
    ],
    spacing=10
)
