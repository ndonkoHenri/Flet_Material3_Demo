import flet as ft
import utilities


class WidgetsPage(ft.View):
    def __init__(self):
        self.common_buttons_style = ft.ButtonStyle(
            shape={
                ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder()
            },
        )
        super().__init__(
            '/WidgetsPage',
            padding=ft.padding.all(0),
            controls=[
                ft.Container(
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Column(
                                controls=[
                                    utilities.Section(
                                        title='Actions',
                                        sub_sections_list=[
                                            utilities.SubSection(
                                                title='Common buttons',
                                                help_text='Use ElevatedButton, FilledButton, FilledButton.tonal, OutlinedButton or TextButton',
                                                widgets=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                "Elevated", width=100, height=80,
                                                                style=self.common_buttons_style
                                                            ),
                                                            ft.FilledButton(
                                                                "Filled", width=100, height=80,
                                                                style=self.common_buttons_style
                                                            ),
                                                            ft.FilledTonalButton(
                                                                "Filled tonal", width=100, height=80,
                                                                style=self.common_buttons_style
                                                            ),
                                                            ft.OutlinedButton(
                                                                "Outlined", width=100, height=80,
                                                                style=self.common_buttons_style
                                                            ),
                                                            ft.TextButton(
                                                                "Text", width=100, height=80,
                                                                style=self.common_buttons_style
                                                            )
                                                        ],
                                                        expand=True,
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        alignment=ft.MainAxisAlignment.START
                                                    ) for _ in range(3)
                                                ],
                                                expand=True
                                            )
                                        ],
                                        expand=True
                                    ),
                                ],
                                col={'sm': 12, 'md': 6},
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            ft.Column(
                                controls=[],
                                col={'sm': 12, 'md': 6}
                            )
                        ]
                    ),
                    expand=True,
                    alignment=ft.alignment.center
                )
            ]
        )
