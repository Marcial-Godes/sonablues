import reflex as rx

from sonablues.components.ui.app_badge import (
    app_badge,
)

from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
)


def badge_group(
    items,
    size: str = "2",
) -> rx.Component:

    return rx.flex(

        rx.foreach(

            items,

            lambda item: app_badge(
                item,
                variant="tag",
                size=size,
            ),
        ),

        wrap="wrap",

        gap=EXTRA_SMALL_GAP,

        width="100%",
    )