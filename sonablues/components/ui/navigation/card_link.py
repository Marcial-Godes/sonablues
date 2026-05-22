import reflex as rx


def card_link(
    *children,
    href: str,
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.link(
        *children,
        href=href,
        width=width,
        text_decoration="none",
        display="block",
        **props,
    )