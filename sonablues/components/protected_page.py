import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.components.access_denied import (
    access_denied,
)

from sonablues.config.public_routes import (
    PUBLIC_ROUTES,
)


def protected_page(
    component: rx.Component,
) -> rx.Component:

    current_path = (
        rx.State.router.page.path
    )

    is_public = (
        (current_path == "/")
        | (current_path == "/login")
        | (current_path == "/register")
    )

    return rx.cond(
        is_public
        | AuthState.is_authenticated,

        component,

        access_denied(),
    )