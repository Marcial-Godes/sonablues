import reflex as rx

from sonablues.components.ui import (
    section_header,
    content_stack,
)


def content_section(
    title: str,
    description: str,
    *children,
    **props,
) -> rx.Component:
    return content_stack(
        section_header(
            title,
            description,
        ),
        *children,
        **props,
    )