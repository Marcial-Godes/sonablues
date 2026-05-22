import reflex as rx

from .badge import (
    tag_badge,
)

from sonablues.styles.tokens import (
    INLINE_GAP,
)


def badge_group(
    items,
    size: str = "2",
) -> rx.Component:
    return rx.flex(
        rx.foreach(
            items,
            lambda item: tag_badge(
                item,
                size=size,
            ),
        ),
        wrap="wrap",
        gap=INLINE_GAP,
        width="100%",
    )