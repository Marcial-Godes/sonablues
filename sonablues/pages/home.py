import reflex as rx
from sonablues.components.layouts import (
    base_layout,
)
from sonablues.components.home.home_hero import (
    home_hero,
)
from sonablues.components.home.learning_section import (
    learning_section,
)
from sonablues.components.home.featured_songs import (
    featured_songs,
)
from sonablues.styles.tokens import (
    SECTION_PADDING_Y,
    )


def home_page() -> rx.Component:

    return base_layout(
        rx.vstack(
            home_hero(),
            learning_section(),
            featured_songs(),

            spacing="8",

            width="100%",

            align="stretch",

            padding_x=SECTION_PADDING_Y,
        )
    )