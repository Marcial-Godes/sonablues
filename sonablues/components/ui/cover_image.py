import reflex as rx
from sonablues.styles.radius import (
    IMAGE_RADIUS,
)


def cover_image(
    src: str,
    height,
    object_position: str = "center",
    **props,
) -> rx.Component:
    return rx.image(
        src=src,
        width="100%",
        height=height,
        object_fit="cover",
        object_position=object_position,
        border_radius=IMAGE_RADIUS,
        **props,
    )