import reflex as rx
from sonablues.constants import (
    VIDEO_LESSONS_TITLE,
)
from sonablues.data.models.song_model import Song
from sonablues.components.ui import (
    content_section,
    stack_start,
    video_embed,
    section_row,
    media_container,
    content_card,
)
from sonablues.utils.youtube import (
    youtube_embed_url,
)
from sonablues.styles.tokens import (
    COMPACT_STACK_SPACING,
)


def song_video_section(song: Song) -> rx.Component:
    return content_section(
        VIDEO_LESSONS_TITLE,
        "Vídeos explicativos paso a paso de la canción.",
        *[
            content_card(
                stack_start(
                    section_row(
                        badge=f"{index + 1:02}",
                        title=video.title,
                    ),
                    media_container(
                        video_embed(
                            youtube_embed_url(
                                video.youtube_id
                            ),
                        ),
                    ),
                    spacing=COMPACT_STACK_SPACING,
                    width="100%",
                ),
            )
            for index, video in enumerate(song.videos)
        ],
    )