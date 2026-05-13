import reflex as rx

from sonablues.components.navbar import navbar
from sonablues.components.footer import footer

from sonablues.styles.theme import base_style
from sonablues.styles.sizes import CONTENT_WIDTH


def base_layout(*children) -> rx.Component:

    return rx.box(

        navbar(),

        rx.box(

            rx.vstack(
                *children,

                width="100%",

                align="stretch",

                spacing="0",
            ),

            width="100%",

            max_width=CONTENT_WIDTH,

            margin="0 auto",

            class_name="main-content",
        ),

        footer(),

        min_height="100vh",

        width="100%",

        overflow_x="hidden",

        **base_style,
    )