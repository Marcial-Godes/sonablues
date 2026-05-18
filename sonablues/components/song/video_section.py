import reflex as rx
from sonablues.constants import (
    VIDEO_LESSONS_TITLE,
)
from sonablues.data.models.song_model import Song
from sonablues.components.ui import (
    surface,
    content_section,
    stack_start,
    label_text,
    video_embed,
)
from sonablues.utils.youtube import (
    youtube_embed_url,
)


def song_video_section(song: Song) -> rx.Component:
    return content_section(
        VIDEO_LESSONS_TITLE,
        "Vídeos explicativos paso a paso de la canción.",

        *[
            surface(
                stack_start(
                    label_text(
                        video.title,
                    ),
                    video_embed(
                        youtube_embed_url(video.youtube_id),
                    ),
                    width="100%",
                ),
                width="100%",
            )
            for video in song.videos
        ],
    )