import reflex as rx
from sonablues.components.ui.page_title import (
    page_title,
)
from sonablues.components.ui.muted_text import (
    muted_text,
)
from sonablues.styles.spacing import (
    SMALL_GAP,
)


def empty_state(
    title: str,
    description: str | None = None,
) -> rx.Component:
    return rx.vstack(
        page_title(title),
        rx.cond(
            description is not None,
            muted_text(
                description,
                text_align="center",
                max_width="600px",
            ),
        ),
        spacing=SMALL_GAP,
        align="center",
        width="100%",
        padding_top="4rem",
    )