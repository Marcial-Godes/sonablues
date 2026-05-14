import reflex as rx
from sonablues.components.ui import (
    muted_text,
    surface,
)


def learning_card(
    icon_src: str,
    title: str,
    description: str,
) -> rx.Component:
    return surface(
        rx.vstack(
            rx.image(
                src=icon_src,
                width="22px",
                height="22px",
                object_fit="contain",
            ),
            rx.heading(
                title,
                size="5",
            ),
            muted_text(
                description,
                size="3",
            ),
            spacing="3",
            align="start",
        ),
        padding="1.5rem",
        width="100%",
        hoverable=True,
    )


def learning_section() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "Aprende guitarra de forma práctica",
                size={"base": "5", "md": "7"},
                text_align="center",
                width="100%",
                line_height="1.1",
                max_width={
                    "base": "18ch",
                    "md": "none",
                },
            ),
            muted_text(
                "Canciones, riffs y técnicas explicadas paso a paso.",
                size="4",
                text_align="center",
                width="100%",
                max_width={
                    "base": "18ch",
                    "md": "none",
                },
                margin_x="auto",
            ),
            spacing="4",
            align="center",
            width="100%",
            max_width="720px",
            margin_x="auto",
            padding_x="1rem",
        ),
        rx.grid(
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
            columns={
                "base": "1",
                "md": "2",
                "lg": "3",
            },
            spacing="6",
            width="100%",
        ),
        spacing={
            "base": "7",
            "lg": "8",
        },
        width="100%",
        padding_y={
            "base": "1rem",
            "lg": "2rem",
        },
    )