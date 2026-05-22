import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.layout import (
    page_container,
)
from sonablues.components.ui.text import (
    secondary_text,
    title_text,
    body_text,
    label_text,
    page_title,
)
from sonablues.components.ui.primitives import (
    surface,
)
from sonablues.components.ui.layout import (
    stack_start,
    content_stack,
)
from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_SECTION,
    CONTENT_GAP,
    SECTION_GAP,
)



def profile_content() -> rx.Component:

    return page_container(
        content_stack(
            page_title(
                "Profile",
            ),

            secondary_text(
                f"Welcome back, {AuthState.current_user}",
            ),

            surface(
                stack_start(
                    title_text(
                        "Account Overview",
                        size=TITLE_SIZE_SECTION,
                    ),

                    secondary_text(
                        (
                            "Your personal dashboard will appear here "
                            "in future updates."
                        ),
                    ),

                    rx.divider(),

                    stack_start(
                        label_text(
                            "Planned features:",
                        ),

                        body_text("• Learning progress"),
                        body_text("• Recently viewed lessons"),
                        body_text("• Practice history"),
                        body_text("• Custom playlists"),
                        body_text("• Personal notes"),

                        spacing=CONTENT_GAP,
                    ),
                ),
            ),
        )
    )

def profile_page() -> rx.Component:
    return protected_page(
        base_layout(
            profile_content(),
        )
    )