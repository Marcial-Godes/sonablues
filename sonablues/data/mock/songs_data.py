from sonablues.data.models.song_model import Song, Video
from sonablues.data.models.difficulty import Difficulty


SONGS: dict[str, list[Song]] = {

    "joe-bonamassa": [

        Song(
            title="Sloe Gin",
            slug="sloe-gin",
            artist="Joe Bonamassa",
            difficulty=Difficulty.ADVANCED,
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

            image="/images/songs/joe-bonamassa/sloe-gin.png",
        ),

        Song(
            title="Spanish Boots",
            slug="spanish-boots",
            artist="Joe Bonamassa",
            difficulty=Difficulty.INTERMEDIATE,
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
            image="/images/songs/joe-bonamassa/spanish-boots.png",
        ),
    ],

    "john-mayer": [
        Song(
            title="Slow Dancing in a Burning Room",
            slug="slow-dancing",
            artist="John Mayer",
            difficulty=Difficulty.INTERMEDIATE,
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

            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.png",
        ),

        Song(
            title="Gravity",
            slug="gravity",
            artist="John Mayer",
            difficulty=Difficulty.INTERMEDIATE,
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

            image="/images/songs/john-mayer/gravity.png",
        ),
    ],

    "jimi-hendrix": [

        Song(
            title="Little Wing",
            slug="little-wing",
            artist="Jimi Hendrix",
            difficulty=Difficulty.ADVANCED,
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

            image="/images/songs/jimi-hendrix/little-wing.png",
        ),
    ],

    "srv": [

        Song(
            title="Pride and Joy",
            slug="pride-and-joy",
            difficulty=Difficulty.INTERMEDIATE,
            artist="Stevie Ray Vaughan",
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

            image="/images/songs/stevie-ray-vaughan/pride-and-joy.png",
        ),
    ],

    "tommy-emmanuel": [

        Song(
            title="Angelina",
            slug="angelina",
            artist="Tommy Emmanuel",
            difficulty=Difficulty.ADVANCED,
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

            image="/images/songs/tommy-emmanuel/angelina.png",
        ),
    ],
}