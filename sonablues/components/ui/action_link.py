import reflex as rx

from sonablues.components.ui import (
    action_button,
)


def action_link(
    text: str,
    href: str,
    **props,
) -> rx.Component:

    return rx.link(

        action_button(
            text,
        ),

        href=href,

        text_decoration="none",

        **props,
    )