import reflex as rx

from sonablues.components.ui import (
    content_section,
    section_card,
    content_list,
)


def practice_tips_section() -> rx.Component:
    tips = [
        "Trabaja lentamente con metrónomo antes de subir velocidad.",
        "Mantén el vibrato controlado y consistente.",
        "Prioriza limpieza antes que velocidad.",
        "Escucha la dinámica de cada frase.",
    ]

    return content_section(
        "Practice Tips",
        "Consejos importantes para estudiar la lección correctamente.",

        section_card(
            "01",
            "Consejos de práctica",

            content_list(
                *[
                    rx.list_item(tip)
                    for tip in tips
                ],
            ),
        ),
    )