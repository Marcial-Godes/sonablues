import reflex as rx
from sonablues.styles.tokens import (
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
    SECTION_MAX_WIDTH,
)


def section_container(
    *children,
    max_width: str | None = None,
    **props,
    ):
    return rx.box(
        *children,
        width="100%",
        padding_x={
            "base": "0",
            "md": "0",
        },
        max_width=max_width or SECTION_MAX_WIDTH,
        margin_x="auto",
        padding_top=SECTION_PADDING_TOP,
        padding_bottom=SECTION_PADDING_BOTTOM,
        **props,
    )