import reflex as rx

from ..text import (
    title_text,
    secondary_text,
)

from ..layout import (
    stack_start,
)

from sonablues.styles.tokens import (
    SECTION_TEXT_WIDTH,
    SECTION_MAX_WIDTH,
    TITLE_SIZE_SECTION,
)


def section_header(
    title: str,
    description: str | None = None,
    title_size: str = TITLE_SIZE_SECTION,
    max_width: str = SECTION_MAX_WIDTH,
    align: str = "center",
    **props,
) -> rx.Component:
    return stack_start(
        title_text(
            title,
            size=title_size,
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

        align=align,
        max_width=max_width,
        margin_x="auto",
        padding_x="1rem",
        **props,
    )