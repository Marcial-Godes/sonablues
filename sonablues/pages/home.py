import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.ui import (
    page_title,
    muted_text,
    action_link,
)

from sonablues.routes import (
    ELECTRIC_ARTISTS_ROUTE,
)

from sonablues.styles.spacing import (
    LARGE_GAP,
)


def home_page() -> rx.Component:

    return base_layout(

        rx.vstack(

            rx.badge(
                "Rock • Blues • Guitar",
                color_scheme="blue",
                size="3",
            ),

            page_title(
                "Sonablues",
            ),

            muted_text(
                "Aprende canciones, riffs y guitarra paso a paso.",
                size="5",
            ),

            rx.hstack(

                action_link(
                    "Explorar canciones",
                    href=ELECTRIC_ARTISTS_ROUTE,
                ),

                rx.button(
                    "Mi perfil",
                    variant="outline",
                    size="3",
                ),
            ),

            spacing=LARGE_GAP,
            align="start",
            margin_top="4rem",
        )
    )