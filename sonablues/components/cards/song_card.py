import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.components.ui import (
    surface,
    cover_image,
    badge_group,
    app_badge,
    favorite_button,
    card_link,
    stack_start,
    stack_section,
    title_text,
)
from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
    SMALL_GAP,
)
from sonablues.styles.tokens import (
    SONG_CARD_IMAGE_HEIGHT,
)


def song_card(
    song: Song,
) -> rx.Component:
    return surface(
        stack_section(
            card_link(
                stack_section(
                    cover_image(
                        src=song.image,
                        height=SONG_CARD_IMAGE_HEIGHT,
                    ),
                    stack_start(
                        title_text(
                            song.title,
                            size="5",
                        ),
                        
                        rx.hstack(
                            app_badge(
                                song.difficulty,
                                variant="difficulty",
                            ),
                            app_badge(
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
                    ),
                ),
                href=song_detail_route(
                    song.slug,
                ),
            ),
            favorite_button(
                song.slug,
            ),
        ),
        width="100%",
        hoverable=True,
    )