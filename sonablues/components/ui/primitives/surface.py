import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)

from sonablues.styles.transitions import (
    CARD_TRANSITION,
)

from sonablues.styles.tokens import (
    CARD_HOVER_TRANSFORM,
    CARD_PADDING,
    CARD_BORDER,
    CARD_BACKGROUND,
)

from sonablues.styles.radius import (
    CARD_RADIUS,
)


def surface(
    *children,
    padding: str = CARD_PADDING,
    radius: str = CARD_RADIUS,
    background: str = CARD_BACKGROUND,
    border: str = CARD_BORDER,
    hoverable: bool = False,
    hover_transform: str = CARD_HOVER_TRANSFORM,
    transition: str = CARD_TRANSITION,
    **props,
) -> rx.Component:

    hover_styles = (
        {
            "transform": hover_transform,
            "border": f"1px solid {ACCENT_COLOR}",
        }
        if hoverable
        else {}
    )

    return rx.box(
        *children,
        background=background,
        border=border,
        border_radius=radius,
        padding=padding,
        transition=transition,
        _hover=hover_styles,
        **props,
    )