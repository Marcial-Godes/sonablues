import reflex as rx

from sonablues.components.navbar import (
    navbar,
)

from sonablues.components.footer import (
    footer,
)

from sonablues.styles.theme import (
    base_style,
)

from sonablues.styles.sizes import (
    CONTENT_WIDTH,
)


def base_layout(
    *children,
) -> rx.Component:

    return rx.flex(

        navbar(),

        rx.container(

            rx.vstack(

                *children,

                width="100%",
                align="start",
            ),

            max_width=CONTENT_WIDTH,

            padding="3rem 2rem",

            width="100%",

            flex="1",
        ),

        footer(),

        direction="column",

        min_height="100vh",

        **base_style,
    )