import flet as ft
import typing as tp


class SubSection(ft.UserControl):
    def __init__(
            self,
            title: tp.Optional[str],
            help_text: tp.Optional[str],
            widget: ft.Control | ft.UserControl,
            *args, **kwargs
    ):
        self.title: str | None = title
        self.help_text: str | None = help_text
        self.widget: ft.Control | ft.UserControl = widget
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value=self.title, size=16),
                        ft.IconButton(
                            icon=ft.icons.HELP_OUTLINE,
                            tooltip=self.help_text,
                            icon_size=15
                        ) if self.help_text else ft.Container()
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,

                ) if self.title else ft.Container(),
                ft.Container(
                    content=self.widget,
                    width=445,
                    alignment=ft.alignment.center,
                    border_radius=10,
                    bgcolor=ft.colors.BACKGROUND,
                    padding=30
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )


class Section(ft.UserControl):
    def __init__(
            self,
            title: str,
            sub_sections_list: tp.List[SubSection],
            *args, **kwargs
    ):
        self.title: str | None = title
        self.sub_sections_list: tp.List[SubSection] = sub_sections_list
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(self.title, size=22) if self.title else ft.Container(),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=self.sub_sections_list,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=20
        )
