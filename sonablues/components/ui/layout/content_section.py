import reflex as rx
from .section_header import (
    section_header,
)
from .stacks import (
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