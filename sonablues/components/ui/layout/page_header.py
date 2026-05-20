import reflex as rx
from ..text import (
    title_text,
    secondary_text,
)
from .stacks import (
    stack_start,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
    SECTION_TEXT_WIDTH,
)


def page_header(
    title: str,
    description: str | None = None,
    **props,
) -> rx.Component:
    return stack_start(
        title_text(
            title,
            size=TITLE_SIZE_PAGE,
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