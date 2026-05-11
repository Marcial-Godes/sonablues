import reflex as rx

from sonablues.components.layouts import base_layout
from sonablues.styles.spacing import(
    SMALL_GAP,
    LARGE_GAP,
    SECTION_GAP
    )


def instruments_page() -> rx.Component:

    return base_layout(

        rx.vstack(

            rx.heading(
                "Explorar",
                size="9",
            ),

            rx.text(
                "Selecciona instrumento.",
                color="#8A9AA8",
                size="4",
            ),

            rx.grid(

                rx.link(

                    rx.box(

                        rx.vstack(

                            rx.heading(
                                "Guitarra eléctrica",
                                size="6",
                            ),

                            rx.text(
                                "Blues, rock y fraseo eléctrico.",
                                color="#8A9AA8",
                            ),

                            spacing=SMALL_GAP,
                            align="start",
                        ),

                        background="#27313B",

                        border="1px solid #506070",

                        border_radius="18px",

                        padding="2rem",

                        min_height="220px",

                        _hover={
                            "border": "1px solid #D9D7D1",
                        },
                    ),

                    href="/artists/electric",

                    text_decoration="none",
                ),

                rx.link(

                    rx.box(

                        rx.vstack(

                            rx.heading(
                                "Guitarra acústica",
                                size="6",
                            ),

                            rx.text(
                                "Fingerstyle y dinámica acústica.",
                                color="#8A9AA8",
                            ),

                            spacing=SMALL_GAP,
                            align="start",
                        ),

                        background="#27313B",

                        border="1px solid #506070",

                        border_radius="18px",

                        padding="2rem",

                        min_height="220px",

                        _hover={
                            "border": "1px solid #D9D7D1",
                        },
                    ),

                    href="/artists/acoustic",

                    text_decoration="none",
                ),

                columns={
                    "base": "1",
                    "md": "2",
                },

                spacing=LARGE_GAP,

                width="100%",
            ),

            spacing=SECTION_GAP,

            align="start",

            width="100%",
        )
    )