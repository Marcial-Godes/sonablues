import reflex as rx
from sonablues.components.ui.section_title import (
    section_title,
)
from sonablues.styles.spacing import (
    LARGE_GAP,
)


def content_section(
    title: str,
    *children,
) -> rx.Component:
    return rx.vstack(
        section_title(title),
        *children,
        spacing=LARGE_GAP,
        align="start",
        width="100%",
    )