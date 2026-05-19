import reflex as rx
from sonablues.constants import (
    VIDEO_LESSONS_TITLE,
)
from sonablues.data.models.song_model import Song
from sonablues.components.ui import (
    content_section,
    video_embed,
    media_container,
    section_card,
)
from sonablues.utils.youtube import (
    youtube_embed_url,
)


def song_video_section(song: Song) -> rx.Component:
    return content_section(
        VIDEO_LESSONS_TITLE,
        "Vídeos explicativos paso a paso de la canción.",
        *[
            section_card(
                f"{index + 1:02}",
                video.title,

                media_container(
                    video_embed(
                        youtube_embed_url(
                            video.youtube_id
                        ),
                    ),
                ),
            )
            for index, video in enumerate(song.videos)
        ],
    )