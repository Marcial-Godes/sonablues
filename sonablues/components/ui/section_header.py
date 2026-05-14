import reflex as rx
from sonablues.components.ui import (
    muted_text,
)
from sonablues.styles.spacing import (
    SMALL_GAP,
)
from sonablues.styles.tokens import (
    SECTION_TEXT_WIDTH,
    SECTION_MAX_WIDTH
)


def section_header(
    title: str,
    description: str,
    max_width: str = SECTION_MAX_WIDTH,
) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            size={
                "base": "5",
                "md": "7",
            },
            text_align="center",
            width="100%",
        ),
        muted_text(
            description,
            size="4",
            text_align="center",
            max_width=SECTION_TEXT_WIDTH,
        ),
        spacing=SMALL_GAP,
        align="center",
        width="100%",
        max_width=max_width,
        margin_x="auto",
        padding_x="1rem",
    )