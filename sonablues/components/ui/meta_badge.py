import reflex as rx


def meta_badge(
    text: str,
    color_scheme: str = "gray",
    size: str = "2",
) -> rx.Component:

    return rx.badge(
        text,
        color_scheme=color_scheme,
        size=size,
    )