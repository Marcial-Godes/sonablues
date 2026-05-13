from sonablues.data.models.song_model import Song, Video


SONGS: dict[str, list[Song]] = {

    "joe-bonamassa": [

        Song(
            title="Sloe Gin",
            slug="sloe-gin",
            artist="Joe Bonamassa",
            difficulty="Advanced",
            tuning="Standard",

            techniques=[
                "Expressive Bends",
                "Wide Vibrato",
                "Sustain Control",
                "Slow Blues Phrasing",
                "Dynamic Picking",
            ],

            videos=[
                Video(
                    title="Introduction",
                    youtube_id="k47-9KNlFY4",
                ),

                Video(
                    title="Main Theme",
                    youtube_id="k47-9KNlFY4",
                ),

                Video(
                    title="Solo Breakdown",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1516280440614-37939bbacd81",
        ),

        Song(
            title="Spanish Boots",
            slug="spanish-boots",
            artist="Joe Bonamassa",
            difficulty="Intermediate",
            tuning="Standard",

            techniques=[
                "Blues Licks",
                "String Bending",
                "Vibrato",
                "Pentatonic Runs",
                "Rhythmic Accents",
            ],

            videos=[
                Video(
                    title="Introduction",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f",
        ),
    ],

    "john-mayer": [

        Song(
            title="Slow Dancing in a Burning Room",
            slug="slow-dancing",
            artist="John Mayer",
            difficulty="Intermediate",
            tuning="Standard",

            techniques=[
                "Bends",
                "Vibrato",
                "Double Stops",
            ],

            videos=[
                Video(
                    title="Full Lesson",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1516280440614-37939bbacd81",
        ),

        Song(
            title="Gravity",
            slug="gravity",
            artist="John Mayer",
            difficulty="Beginner / Intermediate",
            tuning="Standard",

            techniques=[
                "Dynamics",
                "Chord Melody",
            ],

            videos=[
                Video(
                    title="Full Lesson",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f",
        ),
    ],

    "jimi-hendrix": [

        Song(
            title="Little Wing",
            slug="little-wing",
            artist="Jimi Hendrix",
            difficulty="Advanced",
            tuning="Standard",

            techniques=[
                "Thumb Chords",
                "Double Stops",
                "Slides",
            ],

            videos=[
                Video(
                    title="Full Lesson",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1511379938547-c1f69419868d",
        ),
    ],

    "srv": [

        Song(
            title="Pride and Joy",
            slug="pride-and-joy",
            difficulty="Intermediate",
            artist="Stivie Ray Vaughan",
            tuning="Half Step Down",

            techniques=[
                "Shuffle",
                "Texas Blues",
            ],

            videos=[
                Video(
                    title="Full Lesson",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1516280440614-37939bbacd81",
        ),
    ],

    "tommy-emmanuel": [

        Song(
            title="Angelina",
            slug="angelina",
            artist="Tommy Emmanuel",
            difficulty="Advanced",
            tuning="Standard",

            techniques=[
                "Fingerstyle",
                "Percussive",
            ],

            videos=[
                Video(
                    title="Full Lesson",
                    youtube_id="k47-9KNlFY4",
                ),
            ],

            image="https://images.unsplash.com/photo-1510915361894-db8b60106cb1",
        ),
    ],
}