import reflex as rx

from sonablues.components.ui import (
    content_card,
    stack_start,
    section_row,
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