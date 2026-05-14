import reflex as rx
from sonablues.styles.theme import (
    CARD_COLOR,
    CARD_BORDER,
    ACCENT_COLOR,
)
from sonablues.styles.radius import (
    CARD_RADIUS,
)
from sonablues.styles.sizes import (
    CARD_PADDING,
)
from sonablues.styles.transitions import (
    CARD_TRANSITION,
)
from sonablues.styles.tokens import (
    CARD_HOVER_TRANSFORM,
    )

def surface(
    *children,
    padding: str = CARD_PADDING,
    hoverable: bool = False,
    **props,
) -> rx.Component:
    hover_styles = {}
    if hoverable:
        hover_styles = {
            "transform": CARD_HOVER_TRANSFORM,
            "border": f"1px solid {ACCENT_COLOR}",
        }
    return rx.box(
        *children,
        background=CARD_COLOR,
        border=CARD_BORDER,
        border_radius=CARD_RADIUS,
        padding=padding,
        transition=CARD_TRANSITION,
        _hover=hover_styles,
        **props,
    )