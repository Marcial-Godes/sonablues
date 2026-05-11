from sonablues.data.models.artist_model import Artist


ARTISTS: dict[str, list[Artist]] = {

    "electric": [

        Artist(
            name="Joe Bonamassa",
            slug="joe-bonamassa",

            description=(
                "Blues rock moderno, tono potente "
                "y fraseo elegante con alma clásica."
            ),

            image=(
                "https://images.unsplash.com/photo-1516280440614-37939bbacd81"
            ),
        ),

        Artist(
            name="John Mayer",
            slug="john-mayer",

            description=(
                "Blues moderno, dinámica contenida "
                "y sensibilidad melódica contemporánea."
            ),

            image=(
                "https://images.unsplash.com/photo-1511379938547-c1f69419868d"
            ),
        ),

        Artist(
            name="Jimi Hendrix",
            slug="jimi-hendrix",

            description=(
                "Expresividad, acordes con color "
                "y lenguaje blues psicodélico."
            ),

            image=(
                "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f"
            ),
        ),

        Artist(
            name="Stevie Ray Vaughan",
            slug="srv",

            description=(
                "Texas blues agresivo, shuffle "
                "y fraseo lleno de carácter."
            ),

            image=(
                "https://images.unsplash.com/photo-1516280440614-37939bbacd81"
            ),
        ),
    ],

    "acoustic": [

        Artist(
            name="Tommy Emmanuel",
            slug="tommy-emmanuel",

            description=(
                "Fingerstyle dinámico y control "
                "rítmico extremadamente musical."
            ),

            image=(
                "https://images.unsplash.com/photo-1510915361894-db8b60106cb1"
            ),
        ),
    ],
}