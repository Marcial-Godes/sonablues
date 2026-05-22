import reflex as rx

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.components.ui.sections import (
    section_card,
    section_header,
)


def practice_tips_section() -> rx.Component:
    tips = [
        "Trabaja lentamente con metrónomo antes de subir velocidad.",
        "Mantén el vibrato controlado y consistente.",
        "Prioriza limpieza antes que velocidad.",
        "Escucha la dinámica de cada frase.",
    ]

    return content_stack(
        section_header(
            "Practice Tips",
            "Consejos importantes para estudiar la lección correctamente.",
        ),

        section_card(
            "01",
            "Consejos de práctica",

            rx.unordered_list(
                *[
                    rx.list_item(tip)
                    for tip in tips
                ],
                spacing="2",
                padding_left="1.25rem",
            ),
        ),
    )