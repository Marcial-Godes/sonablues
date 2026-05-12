import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.home.home_hero import (
    home_hero,
)


def home_page() -> rx.Component:

    return base_layout(

        rx.vstack(

            home_hero(),

            width="100%",
            align="start",
        )
    )