import reflex as rx

from sonablues.styles.tokens import (
    CARD_RADIUS,
)


def cover_image(
    src: str,
    height: str,
    object_position: str = "center",
    **props,
) -> rx.Component:

    return rx.image(
        src=src,
        loading="lazy",
        width="100%",
        height=height,
        object_fit="cover",
        object_position=object_position,
        border_radius=CARD_RADIUS,
        display="block",
        flex_shrink="0",
        **props,
    )