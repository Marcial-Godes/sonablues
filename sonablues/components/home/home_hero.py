# home_hero.py

import reflex as rx

from sonablues.components.ui import (
    muted_text,
    action_link,
)

from sonablues.routes import (
    ELECTRIC_ARTISTS_ROUTE,
    PROFILE_ROUTE,
)

from sonablues.styles.spacing import LARGE_GAP
from sonablues.styles.theme import BORDER_COLOR


def hero_text() -> rx.Component:

    return rx.vstack(

        rx.badge(
            "Rock • Blues • Guitar",
            color_scheme="blue",
            size="2",
        ),

        rx.heading(
            "Sonablues",
            size={
                "base": "7",
                "sm": "8",
                "lg": "9",
            },
            line_height="1",
            width="100%",
        ),

        muted_text(
            "Aprende canciones, riffs y guitarra paso a paso.",
            size={
                "base": "4",
                "sm": "5",
                "lg": "6",
            },
            max_width="320px",
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
                    size="2",
                ),
                href=PROFILE_ROUTE,
                text_decoration="none",
                width={
                    "base": "100%",
                    "md": "auto",
                },
            ),
            direction={
                "base": "column",
                "lg": "row",
            },
            gap="2",
        ),
        spacing={
            "base": "5",
            "sm": LARGE_GAP,
        },
        align="start",
        width="100%",
    )


def hero_image(height) -> rx.Component:

    return rx.box(
        rx.image(
            src="/images/hero/hero-guitar.png",
            width="100%",
            height=height,
            object_fit="cover",
            object_position="center",
            border_radius="24px",
            border=f"1px solid {BORDER_COLOR}",
            box_shadow="0 20px 60px rgba(0,0,0,0.45)",
        ),
        width="100%",
        overflow="hidden",
    )


def home_hero() -> rx.Component:

    mobile_layout = rx.vstack(
        hero_text(),
        hero_image({
            "base": "240px",
            "sm": "280px",
        }),
        spacing="7",
        width="100%",
        align="stretch",
        padding_top="1rem",
    )

    desktop_layout = rx.flex(
        rx.box(
            hero_text(),
            flex="1",
            min_width="420px",
            max_width="560px",
        ),
        rx.box(
            hero_image("620px"),
            flex="1.4",
        ),
        direction="row",
        gap="3.5rem",
        width="100%",
        align="center",
    )

    return rx.box(

        rx.mobile_and_tablet(
            mobile_layout,
        ),

        rx.desktop_only(
            desktop_layout,
        ),
        width="100%",
        margin_top={
            "base": "1rem",
            "lg": "2rem",
        },
        padding_bottom="2rem",
    )