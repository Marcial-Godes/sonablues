import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.ui.layout import (
    content_stack,
)
from sonablues.components.home.ui import (
    featured_songs,
    home_hero,
    learning_section,
)


def home_page() -> rx.Component:
    return base_layout(
        page_container(
            content_stack(
                home_hero(),
                learning_section(),
                featured_songs(),
            )
        )
    )