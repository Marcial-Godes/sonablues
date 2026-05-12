import reflex as rx
from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
)


def badge_group(
    items,
    size: str = "2",
) -> rx.Component:
    return rx.flex(
        rx.foreach(
            items,
            lambda item: rx.badge(
                item,
                color_scheme="gray",
                variant="soft",
                size=size,
            ),
        ),
        wrap="wrap",
        gap=EXTRA_SMALL_GAP,
        width="100%",
    )