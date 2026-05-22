import reflex as rx

from sonablues.components.ui.primitives import (
    surface,
)

from sonablues.styles.tokens import (
    CARD_MAX_WIDTH,
    CARD_PADDING_COMPACT,
)


def content_card(
    *children,
    padding: str = CARD_PADDING_COMPACT,
    max_width: str = CARD_MAX_WIDTH,
    **props,
) -> rx.Component:
    return surface(
        *children,
        width="100%",
        max_width=max_width,
        margin="0 auto",
        padding=padding,
        **props,
    )