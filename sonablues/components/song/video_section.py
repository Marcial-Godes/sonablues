import reflex as rx

from sonablues.constants import (
    VIDEO_LESSONS_TITLE,
)

from sonablues.data.models.song_model import Song

from sonablues.components.ui import (
    surface,
    content_section,
)

from sonablues.utils.youtube import (
    youtube_embed_url,
)

from sonablues.styles.spacing import (
    MEDIUM_GAP,
)


def song_video_section(song: Song) -> rx.Component:

    return content_section(

        VIDEO_LESSONS_TITLE,

        *[
            surface(

                rx.vstack(

                    rx.text(
                        video.title,
                        weight="bold",
                        size="4",
                    ),

                    rx.html(
                        f"""
                        <iframe
                            width="100%"
                            height="500"
                            src="{youtube_embed_url(video.youtube_id)}"
                            title="YouTube video player"
                            frameborder="0"
                            allowfullscreen
                        ></iframe>
                        """
                    ),

                    spacing=MEDIUM_GAP,
                    width="100%",
                ),

                width="100%",
            )

            for video in song.videos
        ],
    )