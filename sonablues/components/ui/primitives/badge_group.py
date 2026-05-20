import reflex as rx
from sonablues.components.ui.primitives.app_badge import (
    app_badge,
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
            lambda item: app_badge(
                item,
                variant="tag",
                size=size,
            ),
        ),
        wrap="wrap",
        gap=INLINE_GAP,
        width="100%",
    )