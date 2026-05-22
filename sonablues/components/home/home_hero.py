import reflex as rx

from sonablues.components.ui.navigation.app_button import app_button
from sonablues.components.ui.layout import stack_start
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.ui.text import (
    secondary_text,
    display_title,
)

from sonablues.routes import (
    ELECTRIC_ARTISTS_ROUTE,
    PROFILE_ROUTE,
)
from sonablues.styles.theme import BORDER_COLOR
from sonablues.styles.tokens import (
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
    HOME_HERO_MOBILE_IMAGE_HEIGHT,
    HOME_HERO_DESKTOP_IMAGE_HEIGHT,
    HOME_HERO_TEXT_MAX_WIDTH,
    HOME_HERO_TEXT_MIN_WIDTH,
    SECTION_GAP,
)


def hero_text() -> rx.Component:
    return stack_start(
        rx.badge(
            "Rock • Blues • Guitar",
            color_scheme="blue",
            size="2",
        ),
        display_title(
            "Sonablues",
            line_height="1",
        ),
        secondary_text(
            "Aprende canciones, riffs y guitarra paso a paso.",
            size={
                "base": "4",
                "sm": "5",
                "lg": "6",
            },
            max_width="320px",
        ),
        rx.flex(
            app_button(
                "Explorar canciones",
                href=ELECTRIC_ARTISTS_ROUTE,
            ),

            app_button(
                "Mi perfil",
                href=PROFILE_ROUTE,
                variant="outline",
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
        spacing=SECTION_GAP,
    )


def hero_image(height) -> rx.Component:
    return rx.box(
        cover_image(
            src="/images/hero/hero-guitar.png",
            height=height,
            border=f"1px solid {BORDER_COLOR}",
            box_shadow="0 20px 60px rgba(0,0,0,0.45)",
        ),
        width="100%",
        overflow="hidden",
    )


def home_hero() -> rx.Component:
    mobile_layout = rx.vstack(
        hero_text(),
        hero_image(
            HOME_HERO_MOBILE_IMAGE_HEIGHT,
        ),
        spacing=SECTION_GAP,
        width="100%",
        align="stretch",
        padding_top=SECTION_PADDING_TOP,
    )
    desktop_layout = rx.flex(
        rx.box(
            hero_text(),
            flex="1",
            min_width=HOME_HERO_TEXT_MIN_WIDTH,
            max_width=HOME_HERO_TEXT_MAX_WIDTH,
        ),
        rx.box(
            hero_image(
                HOME_HERO_DESKTOP_IMAGE_HEIGHT,
            ),
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
        padding_bottom=SECTION_PADDING_BOTTOM,
    )