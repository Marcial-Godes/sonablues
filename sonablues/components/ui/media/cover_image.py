import reflex as rx

from sonablues.styles.radius import (
    IMAGE_RADIUS,
)


def cover_image(
    src: str,
    height: str,
    width: str = "100%",
    object_fit: str = "cover",
    object_position: str = "center",
    radius: str = IMAGE_RADIUS,
    **props,
) -> rx.Component:
    return rx.image(
        src=src,
        loading="lazy",
        width=width,
        height=height,
        object_fit=object_fit,
        object_position=object_position,
        border_radius=radius,
        display="block",
        flex_shrink="0",
        **props,
    )