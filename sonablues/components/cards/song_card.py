import reflex as rx
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.routes import (
    song_detail_route,
)
from sonablues.components.ui import (
    surface,
    cover_image,
    badge_group,
    meta_badge,
    favorite_button,
)
from sonablues.styles.theme import (
    TEXT_COLOR,
)
from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
    SMALL_GAP,
    MEDIUM_GAP,
)


def song_card(
    song: Song,
) -> rx.Component:
    return surface(
        rx.vstack(
            rx.link(
                rx.vstack(
                    cover_image(
                        src=song.image,
                        height="220px",
                    ),
                    rx.vstack(
                        rx.heading(
                            song.title,
                            size="5",
                            color=TEXT_COLOR,
                        ),
                        rx.hstack(
                            meta_badge(
                                song.difficulty,
                                color_scheme=rx.cond(
                                    song.difficulty == "Beginner",
                                    "green",
                                    rx.cond(
                                        song.difficulty == "Intermediate",
                                        "orange",
                                        "red",
                                    ),
                                ),
                            ),
                            meta_badge(
                                song.tuning,
                            ),
                            spacing=EXTRA_SMALL_GAP,
                            wrap="wrap",
                        ),
                        badge_group(
                            song.techniques,
                            size="1",
                        ),
                        spacing=SMALL_GAP,
                        align="start",
                        width="100%",
                    ),
                    spacing=MEDIUM_GAP,
                    align="start",
                    width="100%",
                ),
                href=song_detail_route(
                    song.slug,
                ),
                width="100%",
                text_decoration="none",
            ),
            favorite_button(
                song.slug,
            ),
            spacing=MEDIUM_GAP,
            align="start",
            width="100%",
        ),
        width="100%",
        hoverable=True,
    )