import reflex as rx
from sonablues.components.ui.surface import (
    surface,
)
from sonablues.components.ui.stacks import (
    content_stack,
)


def media_card(
    media,
    *content,
    spacing=None,
    hoverable: bool = True,
    **props,
) -> rx.Component:
    return surface(
        content_stack(
            media,
            *content,
            spacing=spacing,
        ),
        hoverable=hoverable,
        **props,
    )