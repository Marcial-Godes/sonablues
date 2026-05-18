import reflex as rx
from sonablues.styles.tokens import (
    CONTENT_GAP,
    SECTION_GAP,
)


def stack_start(
    *children,
    spacing=CONTENT_GAP,
    **props,
) -> rx.Component:
    default_props = {
        "spacing": spacing,
        "align": "start",
        "width": "100%",
    }
    return rx.vstack(
        *children,
        **{
            **default_props,
            **props,
        },
    )


def stack_section(
    *children,
    spacing=SECTION_GAP,
    **props,
) -> rx.Component:
    default_props = {
        "spacing": spacing,
        "align": "start",
        "width": "100%",
    }
    return rx.vstack(
        *children,
        **{
            **default_props,
            **props,
        },
    )