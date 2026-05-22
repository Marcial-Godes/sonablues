import reflex as rx

from sonablues.constants import (
    VIDEO_LESSONS_TITLE,
)

from sonablues.data.models.song_model import Song
from sonablues.components.ui.media.video_embed import video_embed
from sonablues.components.ui.layout import content_stack

from sonablues.components.ui.sections import (
    section_card,
    section_header,
)

from sonablues.utils.youtube import (
    youtube_embed_url,
)


def song_video_section(song: Song) -> rx.Component:
    return content_stack(
        section_header(
            VIDEO_LESSONS_TITLE,
            "Vídeos explicativos paso a paso de la canción.",
        ),

        *[
            section_card(
                f"{index + 1:02}",
                video.title,

                rx.box(
                    video_embed(
                        youtube_embed_url(
                            video.youtube_id
                        ),
                    ),

                    width="100%",
                    max_width="900px",
                    margin="0 auto",
                    border_radius="1rem",
                    overflow="hidden",
                ),
            )
            for index, video in enumerate(song.videos)
        ],
    )