import reflex as rx

from sonablues.components.navbar.ui import (
    navbar,
)

from sonablues.components.footer import (
    footer,
)

from sonablues.styles.theme import (
    base_style,
)


def base_layout(
    *children,
) -> rx.Component:

    return rx.flex(
        navbar(),

        rx.box(
            *children,
            width="100%",
            flex="1",
        ),

        footer(),

        direction="column",
        min_height="100vh",
        width="100%",
        overflow_x="hidden",

        **base_style,
    )