import reflex as rx

from sonablues.styles.layout import (
    CONTENT_WIDTH,
)
from sonablues.styles.tokens import (
    PAGE_PADDING_X,
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
)


def page_container(*children, **props):
    return rx.container(
        *children,
        width="100%",
        min_height="100%",
        max_width=CONTENT_WIDTH,
        margin="0 auto",
        padding_x=PAGE_PADDING_X,
        padding_top=SECTION_PADDING_TOP,
        padding_bottom=SECTION_PADDING_BOTTOM,
        **props,
    )