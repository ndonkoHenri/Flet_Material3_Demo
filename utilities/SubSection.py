import flet as ft
import typing as tp


class SubSection(ft.UserControl):
    def __init__(
            self,
            widgets: tp.List[ft.Control | ft.UserControl], title_font_size: int = 18,
            title: str | None = None, help_text: str | None = None, *args, **kwargs):
        self.widgets: tp.List[ft.Control | ft.UserControl] = widgets
        self.title_font_size: int = title_font_size
        self.title: str | None = title
        self.help_text: str | None = help_text
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            value=self.title,
                            size=self.title_font_size
                        ),
                        ft.IconButton(
                            icon=ft.icons.HELP_OUTLINE,
                            tooltip=self.help_text
                        ) if self.help_text else ft.Container()
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ) if self.title else ft.Container(),
                ft.Container(
                    content=ft.Row(
                        controls=self.widgets,
                        spacing=5,
                        expand=True
                    ),
                    expand=True
                )
            ],
            expand=True,
        )
