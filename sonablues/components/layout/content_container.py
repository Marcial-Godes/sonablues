import reflex as rx

from sonablues.styles.tokens import (
    CONTENT_MAX_WIDTH,
    PAGE_PADDING_X,
)


def content_container(*children, **props) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        max_width=CONTENT_MAX_WIDTH,
        margin="0 auto",
        padding_left=PAGE_PADDING_X,
        padding_right=PAGE_PADDING_X,
        box_sizing="border-box",
        **props,
    )