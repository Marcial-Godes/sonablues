import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.ui import (
    page_title,
    muted_text,
    surface,
)

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.utils.protected import (
    protected_page,
)

from sonablues.styles.spacing import (
    LARGE_GAP,
)


def profile_content() -> rx.Component:

    return rx.vstack(

        page_title(
            "Profile",
        ),

        muted_text(
            f"Welcome back, {AuthState.current_user}",
        ),

        surface(

            rx.vstack(

                rx.heading(
                    "Account Overview",
                    size="5",
                ),

                muted_text(
                    (
                        "Your personal dashboard will appear here "
                        "in future updates."
                    ),
                ),

                rx.divider(),

                rx.vstack(

                    rx.text(
                        "Planned features:",
                        weight="bold",
                    ),

                    rx.text("• Learning progress"),

                    rx.text("• Recently viewed lessons"),

                    rx.text("• Practice history"),

                    rx.text("• Custom playlists"),

                    rx.text("• Personal notes"),

                    spacing="2",
                    align="start",
                    width="100%",
                ),

                spacing=LARGE_GAP,
                align="start",
                width="100%",
            ),

            width="100%",
        ),

        spacing=LARGE_GAP,
        align="start",
        width="100%",
    )


def profile_page() -> rx.Component:

    return base_layout(

        protected_page(
            profile_content(),
        )
    )