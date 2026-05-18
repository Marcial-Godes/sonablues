import reflex as rx

from sonablues.styles.tokens import CONTENT_MAX_WIDTH


def content_container(*children, **props) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        max_width=CONTENT_MAX_WIDTH,
        margin_x="auto",
        **props,
    )