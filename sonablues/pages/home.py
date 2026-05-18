import reflex as rx
from sonablues.components.base_layout import (
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
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.ui import (
    stack_section,
)


def home_page() -> rx.Component:
    return base_layout(
        page_container(
            stack_section(
                home_hero(),
                learning_section(),
                featured_songs(),
                align="stretch",
            )
        )
    )