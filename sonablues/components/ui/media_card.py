import reflex as rx
from sonablues.components.ui.surface import (
    surface,
)
from sonablues.components.ui.stacks import (
    stack_section,
)


def media_card(
    media,
    *content,
    spacing=None,
    hoverable: bool = True,
    **props,
) -> rx.Component:
    return surface(
        stack_section(
            media,
            *content,
            spacing=spacing,
        ),
        width="100%",
        hoverable=hoverable,
        **props,
    )