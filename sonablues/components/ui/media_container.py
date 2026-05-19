import reflex as rx

from sonablues.styles.tokens import (
    MEDIA_MAX_WIDTH,
    MEDIA_RADIUS,
)


def media_container(
    *children,
    **props,
) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        max_width=MEDIA_MAX_WIDTH,
        margin="0 auto",
        border_radius=MEDIA_RADIUS,
        overflow="hidden",
        **props,
    )