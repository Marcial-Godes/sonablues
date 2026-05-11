import reflex as rx

from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)

from sonablues.components.ui import (
    surface,
    content_section,
)

from sonablues.styles.spacing import (
    SMALL_GAP,
)


def planned_content() -> rx.Component:

    return content_section(

        PLANNED_CONTENT_TITLE,

        surface(

            rx.vstack(

                rx.text("• Tabs sincronizadas"),
                rx.text("• Vídeo paso a paso"),
                rx.text("• Backing track"),
                rx.text("• Loop de práctica"),
                rx.text("• Sección técnica detallada"),

                spacing=SMALL_GAP,
                align="start",
            ),

            width="100%",
            max_width="700px",

            padding="2rem",
        ),
    )