import flet as ft
from utilities.elevation_utils import ElevationSection


class ElevationScreen(ft.Column):
    def __init__(self):
        super().__init__(spacing=10, expand=19)
        self.controls = [
            ElevationSection("Surface Tint Only", surface_tint=ft.colors.PRIMARY, is_top=True),
            ElevationSection("Surface Tint and Shadow", surface_tint=ft.colors.PRIMARY, shadow_color=ft.colors.SHADOW),
            ElevationSection("Shadow Only", shadow_color=ft.colors.SHADOW),
        ]
