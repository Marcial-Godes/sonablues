import reflex as rx

from sonablues.components.ui import (
    page_title,
    muted_text,
    action_link,
)

from sonablues.routes import (
    ELECTRIC_ARTISTS_ROUTE,
    PROFILE_ROUTE,
)

from sonablues.styles.spacing import (
    LARGE_GAP,
)

from sonablues.styles.theme import (
    BORDER_COLOR,
)


def home_hero() -> rx.Component:

    return rx.grid(

        # Left column
        rx.vstack(

            rx.badge(
                "Rock • Blues • Guitar",
                color_scheme="blue",
                size="3",
            ),

            rx.heading(
                "Sonablues",
                size={
                    "base": "8",
                    "md": "9",
                },
            ),

            muted_text(
                "Aprende canciones, riffs y guitarra paso a paso.",
                size="5",
            ),

            rx.flex(

                action_link(
                    "Explorar canciones",
                    href=ELECTRIC_ARTISTS_ROUTE,
                ),

                rx.link(

                    rx.button(
                        "Mi perfil",
                        variant="outline",
                        size="3",
                    ),

                    href=PROFILE_ROUTE,
                    text_decoration="none",
                ),
                wrap="wrap",
                spacing="4",
            ),

            spacing=LARGE_GAP,
            align="start",
            justify="center",
            height="100%",
        ),

        # Right column
        rx.image(
            src="/images/hero/hero-guitar.png",
            width="100%",
            height={
                "base": "340px",
                "md": "420px",
                "lg": "520px",
            },
            object_fit="cover",
            object_position="center",

            border_radius="24px",

            border=f"1px solid {BORDER_COLOR}",
        ),

        columns={
            "base": "1",
            "lg": "2",
        },

        spacing={
            "base": "6",
            "lg": "8",
        },
        align_items="center",
        width="100%",
        margin_top="4rem",
        padding_bottom="2rem",
    )