import reflex as rx

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.components.ui.primitives import (
    surface,
)


def media_card(
    media: rx.Component,
    *content,
    spacing: str | None = None,
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
        overflow="hidden",
        **props,
    )