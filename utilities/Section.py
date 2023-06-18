import flet as ft
import typing as tp
from . import SubSection


class Section(ft.UserControl):
    def __init__(self, sub_sections_list: tp.List[SubSection], title: str | None = None, title_font_size: int = 24, *args, **kwargs):
        self.sub_sections_list: tp.List[SubSection] = sub_sections_list
        self.title_font_size: int = title_font_size
        self.title: str | None = title
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(self.title, size=self.title_font_size) if self.title else ft.Container(),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=self.sub_sections_list,
                        expand=True
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START
            ),
            expand=True
        )
