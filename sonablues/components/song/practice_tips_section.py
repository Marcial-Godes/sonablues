import reflex as rx

from sonablues.components.ui import (
    content_section,
    content_card,
    stack_start,
    section_row,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
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

        content_card(
            stack_start(
                section_row(
                    badge="01",
                    title="Consejos de práctica",
                ),

                rx.unordered_list(
                    *[
                        rx.list_item(
                            tip,
                        )
                        for tip in tips
                    ],
                    spacing="3",
                    padding_left="1.25rem",
                ),

                spacing=CONTENT_GAP,
                width="100%",
            ),
        ),
    )