import reflex as rx

from .stacks import (
    stack_start,
)

from .text import (
    title_text,
    secondary_text,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
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
        ),

        rx.cond(
            description,
            secondary_text(
                description,
            ),
        ),
        **props,
    )