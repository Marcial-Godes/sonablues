import reflex as rx
from sonablues.styles.theme import (
    CARD_COLOR,
    CARD_BORDER,
)
from sonablues.styles.sizes import (
    CARD_RADIUS,
    CARD_PADDING,
)


def surface(
    *children,
    padding: str = CARD_PADDING,
    **props,
) -> rx.Component:
    return rx.box(
        *children,
        background=CARD_COLOR,
        border=CARD_BORDER,
        border_radius=CARD_RADIUS,
        padding=padding,
        **props,
    )