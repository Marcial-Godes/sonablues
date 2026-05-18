import reflex as rx

from sonablues.components.ui.section_header import (
    section_header,
)

from sonablues.components.ui.stacks import (
    stack_section,
)


def content_section(
    title: str,
    description: str,
    *children,
    **props,
) -> rx.Component:
    return stack_section(
        section_header(
            title,
            description,
        ),
        *children,
        width="100%",
        **props,
    )