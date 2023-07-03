import flet as ft
from typing import List, Optional


class ComponentSubSection(ft.UserControl):
    def __init__(
            self,
            title: Optional[str],
            help_text: Optional[str],
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
                        ft.Icon(
                            name=ft.icons.HELP_OUTLINE,
                            tooltip=self.help_text,
                            size=17
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,

                ) if self.title else ft.Container(),
                ft.Container(
                    content=self.widget,
                    width=450,
                    alignment=ft.alignment.center,
                    border_radius=10,
                    bgcolor=ft.colors.SURFACE,
                    padding=30
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )


class ComponentSection(ft.UserControl):
    def __init__(
            self,
            title: str,
            sub_sections_list: List[ComponentSubSection],
            *args, **kwargs
    ):
        self.title: str | None = title
        self.sub_sections_list: List[ComponentSubSection] = sub_sections_list
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(self.title, size=22),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=self.sub_sections_list,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
            ),
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20
        )


class BottomSheetButton(ft.Column):
    def __init__(self, icon, text):
        super().__init__()
        self.controls = [
            ft.IconButton(icon),
            ft.Text(text)
        ]
        self.spacing = 0


class CardContainer(ft.Container):
    def __init__(self, text):
        super().__init__(padding=10)
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.IconButton(ft.icons.MORE_VERT),
                    alignment=ft.alignment.top_right
                ),
                ft.Container(
                    content=ft.Text(text),
                    alignment=ft.alignment.bottom_left
                )
            ],
            spacing=15
        )


class InputFields(ft.Column):
    def __init__(self, field_type: str):
        super().__init__()
        self.field_type = field_type

        is_filled = self.field_type.lower() == "filled"
        self.temp = []

        for i in range(1, 4):
            p = 4
            self.temp.append(
                ft.TextField(
                    label=field_type.title() if i != 3 else "Disabled",
                    # data=field_type.lower(),
                    border=ft.InputBorder.UNDERLINE if is_filled else ft.InputBorder.OUTLINE,
                    filled=True if is_filled else False,
                    helper_text="supporting text" if i in [1, 3] else None,

                    error_text="error text" if i == 2 else None,
                    expand=1 if i in [2, 3] else None,
                    counter_text="0/10" if i == 2 else None,
                    disabled=True if i == 3 else None,

                    hint_text="hint text",
                    prefix_icon=ft.icons.LOOP,
                    suffix=ft.IconButton(ft.icons.CANCEL, on_click=self.clear),
                    on_change=self.on_change,
                    height=80,
                    content_padding=ft.Padding(p, p+1, p, p+5)
                )
            )

        self.controls = [
            self.temp[0],
            ft.Row(
                controls=self.temp[1:]
            ),
        ]

    def equalize_fields_to(self, value):
        for idx, control in enumerate(self.controls, start=1):
            if idx == 1:
                control.value = value  # control here is a textfield
            else:
                # control here is a row - so access it's controls
                for c in control.controls:
                    c.value = value
        self.update()

    def clear(self, e):
        self.equalize_fields_to("")

    def on_change(self, e):
        # make the text in all the fields thesame
        self.equalize_fields_to(e.control.value)

        # update the counter_text in the second textfield
        self.controls[1].controls[0].counter_text = f"{len(e.control.value)}/10"
        self.update()
