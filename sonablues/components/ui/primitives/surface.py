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
    CARD_RADIUS,
    CARD_BORDER,
    CARD_BACKGROUND,
    CARD_MIN_HEIGHT,
)

def surface(
    *children,
    padding=CARD_PADDING,
    hoverable: bool = False,
    **props,
) -> rx.Component:
    hover_styles = {}
    if hoverable:
        hover_styles = {
            "transform": CARD_HOVER_TRANSFORM,
            "border": f"1px solid {ACCENT_COLOR}",
        }
    default_props = {
        "background": CARD_BACKGROUND,
        "border": CARD_BORDER,
        "border_radius": CARD_RADIUS,
        "padding": padding,
        "transition": CARD_TRANSITION,
        "_hover": hover_styles,
    }
    return rx.box(
        *children,
        **{
            **default_props,
            **props,
        },
    )