import reflex as rx

from ..primitives.surface import (
    surface,
)

from sonablues.styles.tokens import (
    CARD_MAX_WIDTH,
    CARD_PADDING_COMPACT,
)


def content_card(
    *children,
    **props,
) -> rx.Component:
    return surface(
        *children,
        width="100%",
        max_width=CARD_MAX_WIDTH,
        margin="0 auto",
        overflow="hidden",
        padding=CARD_PADDING_COMPACT,
        **props,
    )