import reflex as rx


VIDEO_ASPECT_RATIO = "56.25%"


def video_embed(
    src: str,
    aspect_ratio: str = VIDEO_ASPECT_RATIO,
    radius: str = "16px",
) -> rx.Component:
    return rx.html(
        f"""
        <div style="
            position:relative;
            width:100%;
            padding-top:{aspect_ratio};
            overflow:hidden;
            border-radius:{radius};
        ">
            <iframe
                src="{src}"
                title="YouTube video player"
                frameborder="0"
                allowfullscreen
                style="
                    position:absolute;
                    top:0;
                    left:0;
                    width:100%;
                    height:100%;
                    border:none;
                "
            ></iframe>
        </div>
        """
    )