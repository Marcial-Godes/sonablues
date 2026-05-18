import reflex as rx
from .text import (
    title_text,
    secondary_text,
)
from .stacks import (
    stack_start,
)
from sonablues.styles.tokens import (
    SECTION_TEXT_WIDTH,
    SECTION_MAX_WIDTH,
    TITLE_SIZE_SECTION,
)


def section_header(
    title: str,
    description: str,
    max_width: str = SECTION_MAX_WIDTH,
) -> rx.Component:
    return stack_start(
        title_text(
            title,
            size=TITLE_SIZE_SECTION,
            text_align="center",
        ),
        secondary_text(
            description,
            text_align="center",
            max_width=SECTION_TEXT_WIDTH,
        ),
        align="center",
        width="100%",
        max_width=max_width,
        margin_x="auto",
        padding_x="1rem",
    )