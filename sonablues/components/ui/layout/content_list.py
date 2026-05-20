import reflex as rx
from sonablues.styles.tokens import (
    LIST_SPACING,
    LIST_PADDING_LEFT,
)


def content_list(
    *items,
    **props,
) -> rx.Component:
    return rx.unordered_list(
        *items,
        spacing=LIST_SPACING,
        padding_left=LIST_PADDING_LEFT,
        **props,
    )