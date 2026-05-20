import reflex as rx


def card_link(
    *children,
    href: str,
    **props,
) -> rx.Component:

    return rx.link(

        *children,

        href=href,

        width="100%",

        text_decoration="none",

        display="block",

        **props,
    )