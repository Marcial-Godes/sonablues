import reflex as rx

from ..primitives.page_title import (
    page_title,
)

from ..text import (
    secondary_text,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def empty_state(
    title: str,
    description: str | None = None,
) -> rx.Component:
    return rx.vstack(
        page_title(title),

        rx.cond(
            description is not None,
            secondary_text(
                description,
                text_align="center",
                max_width="600px",
            ),
        ),

        spacing=CONTENT_GAP,
        align="center",
        width="100%",
        padding_top="4rem",
    )