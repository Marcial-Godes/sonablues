import reflex as rx


def video_embed(src: str) -> rx.Component:
    return rx.html(
        f"""
        <div style="
            position:relative;
            width:100%;
            padding-top:56.25%;
            overflow:hidden;
            border-radius:16px;
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