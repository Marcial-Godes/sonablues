import reflex as rx
from sonablues.components.ui import (
    section_header,
    surface,
    title_text,
    secondary_text,
    responsive_grid,
    stack_start,
    stack_section,
)
from sonablues.styles.tokens import (
    LEARNING_ICON_SIZE,
    SECTION_PADDING_Y,
    )


def learning_card(
    icon_src: str,
    title: str,
    description: str,
) -> rx.Component:
    return surface(
        stack_start(
            rx.image(
                src=icon_src,
                width=LEARNING_ICON_SIZE,
                height=LEARNING_ICON_SIZE,
                object_fit="contain",
            ),
            title_text(
                title,
                size="5",
            ),
            secondary_text(
                description,
                size="3",
            ),
            spacing="3",
        ),
        padding="1.5rem",
        width="100%",
        hoverable=True,
    )


def learning_section() -> rx.Component:
    return stack_section(
        section_header(
            "Aprende guitarra de forma práctica",
            "Canciones, riffs y técnicas explicadas paso a paso.",
        ),
        responsive_grid(
            learning_card(
                "/icons/music.svg",
                "Canciones completas",
                "Aprende temas clásicos nota por nota.",
            ),
            learning_card(
                "/icons/flame.svg",
                "Riffs icónicos",
                "Practica riffs esenciales de blues y rock.",
            ),
            learning_card(
                "/icons/waveform.svg",
                "Técnicas reales",
                "Mejora bends, vibrato, dinámica y phrasing.",
            ),
        ),
        padding_y=SECTION_PADDING_Y,
    )