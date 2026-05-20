import reflex as rx
from sonablues.components.ui import (
    surface,
)
from sonablues.components.ui.layout import (
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