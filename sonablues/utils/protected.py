import reflex as rx

from sonablues.states.auth_state import AuthState

from sonablues.styles.spacing import MEDIUM_GAP


def protected_page(
    component: rx.Component,
) -> rx.Component:

    return rx.cond(
        AuthState.is_authenticated,

        component,

        rx.center(

            rx.vstack(

                rx.heading(
                    "Acceso restringido",
                    size="7",
                ),

                rx.text(
                    "Debes iniciar sesión.",
                ),

                rx.button(
                    "Ir al login",
                    on_click=rx.redirect("/login"),
                ),

                spacing=MEDIUM_GAP,
            ),

            height="70vh",
        ),
    )