import reflex as rx
from ..text import (
    display_title,
    secondary_text,
)

from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    SECTION_TEXT_WIDTH,
)


def page_header(
    title: str,
    description: str | None = None,
    **props,
) -> rx.Component:
    return stack_start(
        display_title(
            title,
            text_align="center",
        ),
        rx.cond(
            description,
            secondary_text(
                description,
                text_align="center",
                max_width=SECTION_TEXT_WIDTH,
            ),
        ),
        align="center",
        margin_x="auto",
        **props,
    )