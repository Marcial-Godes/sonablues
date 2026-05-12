import reflex as rx
from sonablues.styles.sizes import (
    IMAGE_RADIUS,
)


def cover_image(
    src: str,
    height: str,
    **props,
) -> rx.Component:
    return rx.image(
        src=src,
        width="100%",
        height=height,
        object_fit="cover",
        border_radius=IMAGE_RADIUS,
        **props,
    )