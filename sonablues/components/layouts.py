import reflex as rx

from sonablues.components.navbar import navbar

from sonablues.styles.theme import (
    base_style,
)

from sonablues.styles.sizes import (
    CONTENT_WIDTH,
)


def base_layout(
    *children,
) -> rx.Component:

    return rx.box(

        navbar(),

        rx.container(

            rx.vstack(

                *children,

                width="100%",
                align="start",
            ),

            max_width=CONTENT_WIDTH,

            padding="3rem 2rem",
        ),

        **base_style,
    )