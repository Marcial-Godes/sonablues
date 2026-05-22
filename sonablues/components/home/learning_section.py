import reflex as rx
from sonablues.components.ui.text import (
    secondary_text,
)
from sonablues.components.ui.sections import (
    section_header,
)
from sonablues.components.ui.primitives import (
    surface,
)
from sonablues.components.ui.text import (
    title_text,
)
from sonablues.components.ui.layout import (
    stack_start,
    content_stack,
    responsive_grid,
)
from sonablues.styles.tokens import (
    LEARNING_ICON_SIZE,
    CARD_PADDING,
    CONTENT_GAP,
    TITLE_SIZE_CARD,
    TEXT_SIZE_SECONDARY,
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
                size=TITLE_SIZE_CARD,
            ),
            secondary_text(
                description,
                size=TEXT_SIZE_SECONDARY,
            ),
            spacing=CONTENT_GAP,
        ),
        padding=CARD_PADDING,
        hoverable=True,
    )


def learning_section() -> rx.Component:
    return content_stack(
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
        )
    )