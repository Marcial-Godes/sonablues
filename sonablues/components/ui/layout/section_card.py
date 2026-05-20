import reflex as rx

from .section_row import (
    section_row,
)
from ..layout import (
    stack_start,
    content_card,
)
from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def section_card(
    badge: str,
    title: str,
    *children,
    **props,
) -> rx.Component:
    return content_card(
        stack_start(
            section_row(
                badge=badge,
                title=title,
            ),
            *children,
            spacing=CONTENT_GAP,
            **props,
        ),
    )