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
                        ft.Text(value=self.title, size=18),
                        ft.IconButton(
                            icon=ft.icons.HELP_OUTLINE,
                            tooltip=self.help_text
                        ) if self.help_text else ft.Container()
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ) if self.title else ft.Container(),
                ft.Container(
                    content=self.widget,
                    width=420,
                    alignment=ft.alignment.center
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
                            ft.Text(self.title, size=24) if self.title else ft.Container(),
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
        )
