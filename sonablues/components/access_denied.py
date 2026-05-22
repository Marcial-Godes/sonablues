import reflex as rx


def access_denied() -> rx.Component:

    return rx.center(
        rx.vstack(
            rx.heading(
                "Acceso privado",
                size="8",
            ),

            rx.text(
                (
                    "Sonablues es una plataforma "
                    "de acceso restringido."
                ),
                text_align="center",
                color="gray",
            ),

            rx.text(
                (
                    "Necesitas autorización "
                    "del propietario para acceder."
                ),
                text_align="center",
                color="gray",
                size="3",
            ),

            rx.button(
                "Ir al login",
                on_click=rx.redirect(
                    "/login",
                ),
                margin_top="12px",
            ),

            rx.vstack(
                rx.text(
                    "¿Ya tienes cuenta?",
                    size="2",
                    color="gray",
                ),

                rx.link(
                    "Recuperar contraseña",
                    href="#",
                    color="skyblue",
                    size="2",
                ),

                spacing="1",
                margin_top="16px",
            ),

            spacing="4",
            align="center",
            max_width="420px",
            padding="32px",
        ),

        width="100%",
        min_height="70vh",
    )