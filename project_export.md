# EXPORTACIÓN DE PROYECTO

Fecha: 2026-05-21 19:20:25

---

# ESTRUCTURA DEL PROYECTO

```text
📄 .gitignore
📁 .states
📁 assets
    📄 favicon.ico
    📁 icons
        📄 flame.svg
        📄 heart-filled.svg
        📄 heart-outline.svg
        📄 music.svg
        📄 search.svg
        📄 waveform.svg
    📁 images
        📁 hero
            📄 andrey-soldatov-0h7aKkEbcvk-unsplash.jpg
            📄 ChatGPT Image 12 may 2026, 07_55_16.png
            📄 ChatGPT Image 12 may 2026, 07_56_38.png
            📄 hero-guitar.png
            📄 joey-nicotra-C9qBZ13m6aI-unsplash.jpg
            📄 pexels-zan-carvalho-2104229-6794588.jpg
        📁 songs
            📁 jimi-hendrix
                📄 little-wing.webp
                📄 red-house.webp
            📁 joe-bonamassa
                📄 sloe-gin.webp
                📄 spanish-boots.webp
            📁 john-mayer
                📄 gravity.webp
                📄 slow-dancing-in-a-burning-room.webp
            📁 stevie-ray-vaughan
                📄 pride-and-joy.webp
            📁 tommy-emmanuel
                📄 angelina.png
                📄 angelina.webp
    📄 styles.css
📄 export_project.py
📄 project_export.md
📄 README.md
📄 requirements.txt
📄 rxconfig.py
📁 sonablues
    📄 __init__.py
    📄 app_pages.py
    📁 components
        📄 __init__.py
        📁 artist
            📄 __init__.py
            📄 artist_card.py
            📄 ui.py
        📄 base_layout.py
        📄 footer.py
        📁 home
            📄 featured_songs.py
            📄 home_hero.py
            📄 learning_section.py
            📄 ui.py
        📁 instrument
            📄 __init__.py
            📄 instrument_card.py
            📄 ui.py
        📁 layout
            📄 __init__.py
            📄 content_container.py
            📄 page_container.py
            📄 section_container.py
        📁 navbar
            📄 __init__.py
            📄 desktop_navigation.py
            📄 desktop_user.py
            📄 mobile_menu.py
            📄 nav_link.py
            📄 navbar.py
            📄 ui.py
        📁 search
            📄 __init__.py
            📄 song_search_input.py
        📁 song
            📄 __init__.py
            📁 content
                📄 __init__.py
                📄 song_content.py
            📄 difficulty_badge.py
            📄 favorite_button.py
            📁 sections
                📄 __init__.py
                📄 planned_content.py
                📄 practice_tips_section.py
                📄 song_hero.py
                📄 video_section.py
            📄 song_card.py
            📄 song_preview_card.py
        📁 ui
            📄 __init__.py
            📁 cards
                📄 __init__.py
                📄 content_card.py
                📄 media_card.py
            📁 feedback
                📄 __init__.py
                📄 empty_state.py
            📁 layout
                📄 __init__.py
                📄 responsive_grid.py
                📄 stacks.py
            📁 media
                📄 __init__.py
                📄 cover_image.py
                📄 video_embed.py
            📁 navigation
                📄 __init__.py
                📄 app_button.py
                📄 card_link.py
            📁 primitives
                📄 __init__.py
                📄 badge.py
                📄 badge_group.py
                📄 surface.py
            📁 sections
                📄 __init__.py
                📄 page_header.py
                📄 section_card.py
                📄 section_header.py
            📁 text
                📄 __init__.py
                📄 page_title.py
                📄 section_label.py
                📄 text_components.py
    📄 config.py
    📄 constants.py
    📁 data
        📄 __init__.py
        📄 lessons_data.py
        📁 mock
            📄 __init__.py
            📄 artist_indexes.py
            📄 artists_data.py
            📄 song_indexes.py
            📄 songs_data.py
        📁 models
            📄 __init__.py
            📄 artist_model.py
            📄 difficulty.py
            📄 song_model.py
            📄 user.py
    📁 database
        📄 __init__.py
        📄 db.py
    📄 estructura.txt
    📁 models
        📄 __init__.py
        📄 user.py
    📁 pages
        📄 __init__.py
        📄 artists.py
        📄 favorites.py
        📄 home.py
        📄 instruments.py
        📄 login.py
        📄 profile.py
        📄 register.py
        📄 song_detail.py
        📄 songs.py
    📁 routes
        📄 __init__.py
        📄 routes.py
    📁 services
        📄 __init__.py
        📄 artist_service.py
        📄 auth_service.py
        📄 song_service.py
        📄 user_service.py
    📄 sonablues.py
    📁 states
        📄 __init__.py
        📄 auth_state.py
        📄 profile_state.py
        📄 song_search_state.py
    📁 styles
        📄 __init__.py
        📄 layout.py
        📄 radius.py
        📄 theme.py
        📄 tokens.py
        📄 transitions.py
    📁 utils
        📄 __init__.py
        📄 protected.py
        📄 security.py
        📄 youtube.py
📄 sonablues.db
```

---

# ARCHIVO: assets\styles.css

```css
* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  overflow-x: hidden;
}

.main-content {
  width: 100%;
  padding: 0.75rem;
}

@media (min-width: 768px) {

  .main-content {
    padding: 1.5rem;
  }
}

@media (min-width: 1024px) {

  .main-content {
    padding: 3rem 2rem;
  }
}
```

---

# ARCHIVO: export_project.py

```python
from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================

ROOT_DIR = Path(".")

OUTPUT_FILE = "project_export.md"

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
    ".web",
    "node_modules",
    "dist",
    "build",
}

ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".css",
    ".scss",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".html",
    ".env",
}

LANGUAGE_MAP = {
    ".py": "python",
    ".md": "markdown",
    ".json": "json",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".css": "css",
    ".scss": "scss",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".jsx": "jsx",
    ".html": "html",
    ".txt": "text",
    ".env": "bash",
}


# =========================================================
# UTILIDADES
# =========================================================

def should_ignore(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def get_language(path: Path) -> str:
    return LANGUAGE_MAP.get(path.suffix.lower(), "text")


def build_tree(root: Path) -> str:
    lines = []

    for path in sorted(root.rglob("*")):

        if should_ignore(path):
            continue

        depth = len(path.relative_to(root).parts) - 1
        indent = "    " * depth

        if path.is_dir():
            lines.append(f"{indent}📁 {path.name}")
        else:
            lines.append(f"{indent}📄 {path.name}")

    return "\n".join(lines)


# =========================================================
# EXPORTACIÓN
# =========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    export_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -----------------------------------------------------
    # CABECERA
    # -----------------------------------------------------

    output.write("# EXPORTACIÓN DE PROYECTO\n\n")
    output.write(f"Fecha: {export_date}\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ÁRBOL DE ARCHIVOS
    # -----------------------------------------------------

    output.write("# ESTRUCTURA DEL PROYECTO\n\n")
    output.write("```text\n")
    output.write(build_tree(ROOT_DIR))
    output.write("\n```\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ARCHIVOS
    # -----------------------------------------------------

    for path in sorted(ROOT_DIR.rglob("*")):

        if should_ignore(path):
            continue

        if not path.is_file():
            continue

        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        relative_path = path.relative_to(ROOT_DIR)
        language = get_language(path)

        try:
            content = path.read_text(encoding="utf-8")

        except Exception as e:
            content = f"[ERROR LEYENDO ARCHIVO: {e}]"

        output.write(f"# ARCHIVO: {relative_path}\n\n")

        output.write(f"```{language}\n")
        output.write(content)
        output.write("\n```\n\n")

        output.write("---\n\n")

print(f"\n✅ Proyecto exportado correctamente:")
print(f"📄 {OUTPUT_FILE}\n")
```

---

# ARCHIVO: project_export.md

```markdown
# EXPORTACIÓN DE PROYECTO

Fecha: 2026-05-21 19:20:25

---

# ESTRUCTURA DEL PROYECTO

```text
📄 .gitignore
📁 .states
📁 assets
    📄 favicon.ico
    📁 icons
        📄 flame.svg
        📄 heart-filled.svg
        📄 heart-outline.svg
        📄 music.svg
        📄 search.svg
        📄 waveform.svg
    📁 images
        📁 hero
            📄 andrey-soldatov-0h7aKkEbcvk-unsplash.jpg
            📄 ChatGPT Image 12 may 2026, 07_55_16.png
            📄 ChatGPT Image 12 may 2026, 07_56_38.png
            📄 hero-guitar.png
            📄 joey-nicotra-C9qBZ13m6aI-unsplash.jpg
            📄 pexels-zan-carvalho-2104229-6794588.jpg
        📁 songs
            📁 jimi-hendrix
                📄 little-wing.webp
                📄 red-house.webp
            📁 joe-bonamassa
                📄 sloe-gin.webp
                📄 spanish-boots.webp
            📁 john-mayer
                📄 gravity.webp
                📄 slow-dancing-in-a-burning-room.webp
            📁 stevie-ray-vaughan
                📄 pride-and-joy.webp
            📁 tommy-emmanuel
                📄 angelina.png
                📄 angelina.webp
    📄 styles.css
📄 export_project.py
📄 project_export.md
📄 README.md
📄 requirements.txt
📄 rxconfig.py
📁 sonablues
    📄 __init__.py
    📄 app_pages.py
    📁 components
        📄 __init__.py
        📁 artist
            📄 __init__.py
            📄 artist_card.py
            📄 ui.py
        📄 base_layout.py
        📄 footer.py
        📁 home
            📄 featured_songs.py
            📄 home_hero.py
            📄 learning_section.py
            📄 ui.py
        📁 instrument
            📄 __init__.py
            📄 instrument_card.py
            📄 ui.py
        📁 layout
            📄 __init__.py
            📄 content_container.py
            📄 page_container.py
            📄 section_container.py
        📁 navbar
            📄 __init__.py
            📄 desktop_navigation.py
            📄 desktop_user.py
            📄 mobile_menu.py
            📄 nav_link.py
            📄 navbar.py
            📄 ui.py
        📁 search
            📄 __init__.py
            📄 song_search_input.py
        📁 song
            📄 __init__.py
            📁 content
                📄 __init__.py
                📄 song_content.py
            📄 difficulty_badge.py
            📄 favorite_button.py
            📁 sections
                📄 __init__.py
                📄 planned_content.py
                📄 practice_tips_section.py
                📄 song_hero.py
                📄 video_section.py
            📄 song_card.py
            📄 song_preview_card.py
        📁 ui
            📄 __init__.py
            📁 cards
                📄 __init__.py
                📄 content_card.py
                📄 media_card.py
            📁 feedback
                📄 __init__.py
                📄 empty_state.py
            📁 layout
                📄 __init__.py
                📄 responsive_grid.py
                📄 stacks.py
            📁 media
                📄 __init__.py
                📄 cover_image.py
                📄 video_embed.py
            📁 navigation
                📄 __init__.py
                📄 app_button.py
                📄 card_link.py
            📁 primitives
                📄 __init__.py
                📄 badge.py
                📄 badge_group.py
                📄 surface.py
            📁 sections
                📄 __init__.py
                📄 page_header.py
                📄 section_card.py
                📄 section_header.py
            📁 text
                📄 __init__.py
                📄 page_title.py
                📄 section_label.py
                📄 text_components.py
    📄 config.py
    📄 constants.py
    📁 data
        📄 __init__.py
        📄 lessons_data.py
        📁 mock
            📄 __init__.py
            📄 artist_indexes.py
            📄 artists_data.py
            📄 song_indexes.py
            📄 songs_data.py
        📁 models
            📄 __init__.py
            📄 artist_model.py
            📄 difficulty.py
            📄 song_model.py
            📄 user.py
    📁 database
        📄 __init__.py
        📄 db.py
    📄 estructura.txt
    📁 models
        📄 __init__.py
        📄 user.py
    📁 pages
        📄 __init__.py
        📄 artists.py
        📄 favorites.py
        📄 home.py
        📄 instruments.py
        📄 login.py
        📄 profile.py
        📄 register.py
        📄 song_detail.py
        📄 songs.py
    📁 routes
        📄 __init__.py
        📄 routes.py
    📁 services
        📄 __init__.py
        📄 artist_service.py
        📄 auth_service.py
        📄 song_service.py
        📄 user_service.py
    📄 sonablues.py
    📁 states
        📄 __init__.py
        📄 auth_state.py
        📄 profile_state.py
        📄 song_search_state.py
    📁 styles
        📄 __init__.py
        📄 layout.py
        📄 radius.py
        📄 theme.py
        📄 tokens.py
        📄 transitions.py
    📁 utils
        📄 __init__.py
        📄 protected.py
        📄 security.py
        📄 youtube.py
📄 sonablues.db
```

---

# ARCHIVO: assets\styles.css

```css
* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  overflow-x: hidden;
}

.main-content {
  width: 100%;
  padding: 0.75rem;
}

@media (min-width: 768px) {

  .main-content {
    padding: 1.5rem;
  }
}

@media (min-width: 1024px) {

  .main-content {
    padding: 3rem 2rem;
  }
}
```

---

# ARCHIVO: export_project.py

```python
from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================

ROOT_DIR = Path(".")

OUTPUT_FILE = "project_export.md"

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
    ".web",
    "node_modules",
    "dist",
    "build",
}

ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".css",
    ".scss",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".html",
    ".env",
}

LANGUAGE_MAP = {
    ".py": "python",
    ".md": "markdown",
    ".json": "json",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".css": "css",
    ".scss": "scss",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".jsx": "jsx",
    ".html": "html",
    ".txt": "text",
    ".env": "bash",
}


# =========================================================
# UTILIDADES
# =========================================================

def should_ignore(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def get_language(path: Path) -> str:
    return LANGUAGE_MAP.get(path.suffix.lower(), "text")


def build_tree(root: Path) -> str:
    lines = []

    for path in sorted(root.rglob("*")):

        if should_ignore(path):
            continue

        depth = len(path.relative_to(root).parts) - 1
        indent = "    " * depth

        if path.is_dir():
            lines.append(f"{indent}📁 {path.name}")
        else:
            lines.append(f"{indent}📄 {path.name}")

    return "\n".join(lines)


# =========================================================
# EXPORTACIÓN
# =========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    export_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -----------------------------------------------------
    # CABECERA
    # -----------------------------------------------------

    output.write("# EXPORTACIÓN DE PROYECTO\n\n")
    output.write(f"Fecha: {export_date}\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ÁRBOL DE ARCHIVOS
    # -----------------------------------------------------

    output.write("# ESTRUCTURA DEL PROYECTO\n\n")
    output.write("```text\n")
    output.write(build_tree(ROOT_DIR))
    output.write("\n```\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ARCHIVOS
    # -----------------------------------------------------

    for path in sorted(ROOT_DIR.rglob("*")):

        if should_ignore(path):
            continue

        if not path.is_file():
            continue

        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        relative_path = path.relative_to(ROOT_DIR)
        language = get_language(path)

        try:
            content = path.read_text(encoding="utf-8")

        except Exception as e:
            content = f"[ERROR LEYENDO ARCHIVO: {e}]"

        output.write(f"# ARCHIVO: {relative_path}\n\n")

        output.write(f"```{language}\n")
        output.write(content)
        output.write("\n```\n\n")

        output.write("---\n\n")

print(f"\n✅ Proyecto exportado correctamente:")
print(f"📄 {OUTPUT_FILE}\n")
```

---

# ARCHIVO: README.md

```markdown

```

---

# ARCHIVO: requirements.txt

```text

reflex==0.9.2
sqlmodel==0.0.38
passlib==1.7.4
bcrypt==4.0.1
```

---

# ARCHIVO: rxconfig.py

```python
import reflex as rx

from reflex_base.plugins.sitemap import SitemapPlugin


config = rx.Config(
    app_name="sonablues",

    plugins=[
        rx.plugins.RadixThemesPlugin(),
        SitemapPlugin(),
    ],
)
```

---

# ARCHIVO: sonablues\__init__.py

```python

```

---

# ARCHIVO: sonablues\app_pages.py

```python
import reflex as rx
from sonablues.constants import (
    ELECTRIC,
    ACOUSTIC,
)
from sonablues.data.mock.songs_data import SONGS
from sonablues.routes import (
    HOME_ROUTE,
    LOGIN_ROUTE,
    REGISTER_ROUTE,
    PROFILE_ROUTE,
    INSTRUMENTS_ROUTE,
    ELECTRIC_ARTISTS_ROUTE,
    ACOUSTIC_ARTISTS_ROUTE,
    FAVORITES_ROUTE,
    songs_route,
    song_detail_route,
)
from sonablues.pages.home import home_page
from sonablues.pages.login import login_page
from sonablues.pages.register import register_page
from sonablues.pages.profile import profile_page
from sonablues.pages.instruments import instruments_page
from sonablues.pages.artists import artists_page
from sonablues.pages.songs import songs_page
from sonablues.pages.song_detail import song_detail_page
from sonablues.states.profile_state import (
    ProfileState,
)
from sonablues.states.auth_state import (
    AuthState,
)
from sonablues.pages.favorites import (
    favorites_page,
)


def register_pages(app: rx.App):

    # Home
    app.add_page(
        home_page,
        route=HOME_ROUTE,
        on_load=AuthState.restore_session,
    )

    # Auth
    app.add_page(login_page, route=LOGIN_ROUTE)
    app.add_page(register_page, route=REGISTER_ROUTE)

    # Profile
    app.add_page(
        profile_page,
        route=PROFILE_ROUTE,
        on_load=ProfileState.load_favorites,
    )

    # Instruments
    app.add_page(
        instruments_page,
        route=INSTRUMENTS_ROUTE,
    )

    # Artists
    app.add_page(
        lambda: artists_page(ELECTRIC),
        route=ELECTRIC_ARTISTS_ROUTE,
    )

    app.add_page(
        lambda: artists_page(ACOUSTIC),
        route=ACOUSTIC_ARTISTS_ROUTE,
    )
    app.add_page(
        favorites_page,
        route=FAVORITES_ROUTE,
        on_load=ProfileState.load_favorites,
    )

    # Songs pages
    for artist_slug in SONGS.keys():
        app.add_page(
            lambda artist_slug=artist_slug: songs_page(
            artist_slug,
        ),
            route=songs_route(artist_slug),
        )


    # Song detail pages
    for artist_songs in SONGS.values():
        for song in artist_songs:
            def make_song_page(
                current_slug: str,
            ):
                return lambda: song_detail_page(
                    current_slug,
                )
            app.add_page(
                make_song_page(song.slug),
                route=song_detail_route(
                    song.slug,
                ),
            )
```

---

# ARCHIVO: sonablues\components\__init__.py

```python

```

---

# ARCHIVO: sonablues\components\artist\__init__.py

```python
# Artist domain package.
```

---

# ARCHIVO: sonablues\components\artist\artist_card.py

```python
import reflex as rx
from sonablues.data.models.artist_model import (
    Artist,
)
from sonablues.routes import (
    songs_route,
)
from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.components.ui.navigation.card_link import card_link
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.ui.cards import (
    media_card,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    CARD_IMAGE_HEIGHT_LG,
    ARTIST_CARD_MIN_HEIGHT,
    TITLE_SIZE_CARD,
    CONTENT_GAP,
    TEXT_SIZE_SECONDARY,
)


def artist_card(
    artist: Artist,
) -> rx.Component:
    return card_link(
        media_card(
            cover_image(
                src=artist.image,
                height=CARD_IMAGE_HEIGHT_LG,
            ),
            stack_start(
                title_text(
                    artist.name,
                    size=TITLE_SIZE_CARD,
                ),
                secondary_text(
                    artist.description,
                    size=TEXT_SIZE_SECONDARY,
                ),
                spacing=CONTENT_GAP,
            ),
            min_height=ARTIST_CARD_MIN_HEIGHT,
        ),
        href=songs_route(
            artist.slug,
        ),
    )
```

---

# ARCHIVO: sonablues\components\artist\ui.py

```python
from .artist_card import (
    artist_card,
)
```

---

# ARCHIVO: sonablues\components\base_layout.py

```python
import reflex as rx

from sonablues.components.navbar.ui import navbar
from sonablues.components.footer import footer
from sonablues.styles.theme import base_style


def base_layout(*children) -> rx.Component:
    return rx.flex(
        navbar(),
        rx.box(
            *children,
            width="100%",
            flex="1",
        ),
        footer(),
        direction="column",
        min_height="100vh",
        width="100%",
        overflow_x="hidden",
        **base_style,
    )
```

---

# ARCHIVO: sonablues\components\footer.py

```python
import reflex as rx
from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.components.ui.text import (
    label_text,
    caption_text,
)
from sonablues.styles.tokens import (
    INLINE_GAP,
    CONTENT_GAP,
    FOOTER_PADDING_Y,
    FOOTER_PADDING_X,
)


def footer() -> rx.Component:
    return rx.flex(
        stack_start(
            label_text(
            "Sonablues",
        ),
            caption_text(
                "Modern blues guitar platform",
            ),
            spacing=INLINE_GAP,
        ),
        rx.spacer(),
        caption_text(
            "Made by Marcial",
        ),
        direction={
            "base": "column",
            "sm": "row",
        },
        gap=CONTENT_GAP,
        align={
            "base": "start",
            "sm": "center",
        },
        padding_y=FOOTER_PADDING_Y,
        padding_x=FOOTER_PADDING_X,
        background_color=CARD_COLOR,
        border_top=f"1px solid {BORDER_COLOR}",
    )
```

---

# ARCHIVO: sonablues\components\home\featured_songs.py

```python
import reflex as rx

from sonablues.services.song_service import (
    get_featured_songs,
)

from sonablues.components.song import (
    song_preview_card,
)

from sonablues.components.ui.sections import (
    section_header,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)


def featured_songs() -> rx.Component:
    return content_stack(
        section_header(
            "Canciones destacadas",
            "Aprende algunos de los riffs y canciones más icónicos.",
        ),

        responsive_grid(
            rx.foreach(
                get_featured_songs(),
                lambda song: song_preview_card(song),
            )
        )
    )
```

---

# ARCHIVO: sonablues\components\home\home_hero.py

```python
import reflex as rx

from sonablues.components.ui.navigation.app_button import app_button
from sonablues.components.ui.layout import stack_start
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.routes import (
    ELECTRIC_ARTISTS_ROUTE,
    PROFILE_ROUTE,
)
from sonablues.styles.theme import BORDER_COLOR
from sonablues.styles.tokens import (
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
    HOME_HERO_MOBILE_IMAGE_HEIGHT,
    HOME_HERO_DESKTOP_IMAGE_HEIGHT,
    HOME_HERO_TEXT_MAX_WIDTH,
    HOME_HERO_TEXT_MIN_WIDTH,
    SECTION_GAP,
)


def hero_text() -> rx.Component:
    return stack_start(
        rx.badge(
            "Rock • Blues • Guitar",
            color_scheme="blue",
            size="2",
        ),
        title_text(
            "Sonablues",
            size={
                "base": "7",
                "sm": "8",
                "lg": "9",
            },
            line_height="1",
        ),
        secondary_text(
            "Aprende canciones, riffs y guitarra paso a paso.",
            size={
                "base": "4",
                "sm": "5",
                "lg": "6",
            },
            max_width="320px",
        ),
        rx.flex(
            app_button(
                "Explorar canciones",
                href=ELECTRIC_ARTISTS_ROUTE,
            ),

            app_button(
                "Mi perfil",
                href=PROFILE_ROUTE,
                variant="outline",
                width={
                    "base": "100%",
                    "md": "auto",
                },
            ),
            direction={
                "base": "column",
                "lg": "row",
            },
            gap="2",
        ),
        spacing=SECTION_GAP,
    )


def hero_image(height) -> rx.Component:
    return rx.box(
        cover_image(
            src="/images/hero/hero-guitar.png",
            height=height,
            border=f"1px solid {BORDER_COLOR}",
            box_shadow="0 20px 60px rgba(0,0,0,0.45)",
        ),
        width="100%",
        overflow="hidden",
    )


def home_hero() -> rx.Component:
    mobile_layout = rx.vstack(
        hero_text(),
        hero_image(
            HOME_HERO_MOBILE_IMAGE_HEIGHT,
        ),
        spacing=SECTION_GAP,
        width="100%",
        align="stretch",
        padding_top=SECTION_PADDING_TOP,
    )
    desktop_layout = rx.flex(
        rx.box(
            hero_text(),
            flex="1",
            min_width=HOME_HERO_TEXT_MIN_WIDTH,
            max_width=HOME_HERO_TEXT_MAX_WIDTH,
        ),
        rx.box(
            hero_image(
                HOME_HERO_DESKTOP_IMAGE_HEIGHT,
            ),
            flex="1.4",
        ),
        direction="row",
        gap="3.5rem",
        width="100%",
        align="center",
    )
    return rx.box(
        rx.mobile_and_tablet(
            mobile_layout,
        ),
        rx.desktop_only(
            desktop_layout,
        ),
        width="100%",
        padding_bottom=SECTION_PADDING_BOTTOM,
    )
```

---

# ARCHIVO: sonablues\components\home\learning_section.py

```python
import reflex as rx
from sonablues.components.ui.text import (
    secondary_text,
)
from sonablues.components.ui.sections import (
    section_header,
)
from sonablues.components.ui.primitives import (
    surface,
)
from sonablues.components.ui.text import (
    title_text,
)
from sonablues.components.ui.layout import (
    stack_start,
    content_stack,
    responsive_grid,
)
from sonablues.styles.tokens import (
    LEARNING_ICON_SIZE,
    CARD_PADDING,
    CONTENT_GAP,
    TITLE_SIZE_CARD,
    TEXT_SIZE_SECONDARY,
)


def learning_card(
    icon_src: str,
    title: str,
    description: str,
) -> rx.Component:
    return surface(
        stack_start(
            rx.image(
                src=icon_src,
                width=LEARNING_ICON_SIZE,
                height=LEARNING_ICON_SIZE,
                object_fit="contain",
            ),
            title_text(
                title,
                size=TITLE_SIZE_CARD,
            ),
            secondary_text(
                description,
                size=TEXT_SIZE_SECONDARY,
            ),
            spacing=CONTENT_GAP,
        ),
        padding=CARD_PADDING,
        hoverable=True,
    )


def learning_section() -> rx.Component:
    return content_stack(
        section_header(
            "Aprende guitarra de forma práctica",
            "Canciones, riffs y técnicas explicadas paso a paso.",
        ),
        responsive_grid(
            learning_card(
                "/icons/music.svg",
                "Canciones completas",
                "Aprende temas clásicos nota por nota.",
            ),
            learning_card(
                "/icons/flame.svg",
                "Riffs icónicos",
                "Practica riffs esenciales de blues y rock.",
            ),
            learning_card(
                "/icons/waveform.svg",
                "Técnicas reales",
                "Mejora bends, vibrato, dinámica y phrasing.",
            ),
        )
    )
```

---

# ARCHIVO: sonablues\components\home\ui.py

```python
from .featured_songs import (
    featured_songs,
)

from .home_hero import (
    home_hero,
)

from .learning_section import (
    learning_section,
)
```

---

# ARCHIVO: sonablues\components\instrument\__init__.py

```python
# Instrument domain package.
```

---

# ARCHIVO: sonablues\components\instrument\instrument_card.py

```python
import reflex as rx

from sonablues.components.ui.primitives import (
    surface,
)

from sonablues.components.ui.navigation import (
    card_link,
)

from sonablues.components.ui.text import (
    title_text,
    secondary_text,
)
from sonablues.components.ui.layout import (
    stack_start,
)

from sonablues.styles.tokens import (
    INSTRUMENT_CARD_MIN_HEIGHT,
    CARD_PADDING,
    TITLE_SIZE_SECTION,
    CONTENT_GAP,
)


def instrument_card(
    title: str,
    description: str,
    href: str,
) -> rx.Component:
    return card_link(
        surface(
            stack_start(
                title_text(
                    title,
                    size=TITLE_SIZE_SECTION,
                ),

                secondary_text(
                    description,
                ),

                spacing=CONTENT_GAP,
            ),

            padding=CARD_PADDING,
            min_height=INSTRUMENT_CARD_MIN_HEIGHT,
            hoverable=True,
        ),

        href=href,
    )
```

---

# ARCHIVO: sonablues\components\instrument\ui.py

```python
from .instrument_card import (
    instrument_card,
)
```

---

# ARCHIVO: sonablues\components\layout\__init__.py

```python
from .page_container import page_container
from .section_container import section_container
from .content_container import content_container

__all__ = [
    "page_container",
    "section_container",
    "content_container",
]
```

---

# ARCHIVO: sonablues\components\layout\content_container.py

```python
import reflex as rx

from sonablues.styles.tokens import (
    CONTENT_MAX_WIDTH,
    PAGE_PADDING_X,
)


def content_container(*children, **props) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        max_width=CONTENT_MAX_WIDTH,
        margin="0 auto",
        padding_left=PAGE_PADDING_X,
        padding_right=PAGE_PADDING_X,
        box_sizing="border-box",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\layout\page_container.py

```python
import reflex as rx

from sonablues.styles.layout import (
    CONTENT_WIDTH,
)
from sonablues.styles.tokens import (
    PAGE_PADDING_X,
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
)


def page_container(*children, **props):
    return rx.container(
        *children,
        width="100%",
        min_height="100%",
        max_width=CONTENT_WIDTH,
        margin="0 auto",
        padding_x=PAGE_PADDING_X,
        padding_top=SECTION_PADDING_TOP,
        padding_bottom=SECTION_PADDING_BOTTOM,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\layout\section_container.py

```python
import reflex as rx
from sonablues.styles.tokens import (
    SECTION_PADDING_TOP,
    SECTION_PADDING_BOTTOM,
    SECTION_MAX_WIDTH,
)


def section_container(
    *children,
    max_width: str | None = None,
    **props,
    ):
    return rx.box(
        *children,
        width="100%",
        padding_x={
            "base": "0",
            "md": "0",
        },
        max_width=max_width or SECTION_MAX_WIDTH,
        margin_x="auto",
        padding_top=SECTION_PADDING_TOP,
        padding_bottom=SECTION_PADDING_BOTTOM,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\navbar\__init__.py

```python
# Navbar domain package.
```

---

# ARCHIVO: sonablues\components\navbar\desktop_navigation.py

```python
import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.routes import (
    HOME_ROUTE,
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
)

from sonablues.styles.tokens import (
    NAVBAR_GAP,
)

from .nav_link import (
    nav_link,
)


def desktop_navigation(
    current_path,
    is_home,
) -> rx.Component:
    return rx.hstack(
        nav_link(
            "Home",
            HOME_ROUTE,
            is_home,
        ),

        rx.cond(
            AuthState.is_authenticated,
            rx.fragment(
                nav_link(
                    "Profile",
                    PROFILE_ROUTE,
                    current_path == PROFILE_ROUTE,
                ),

                nav_link(
                    "Favorites",
                    FAVORITES_ROUTE,
                    current_path == FAVORITES_ROUTE,
                ),
            ),
        ),

        spacing=NAVBAR_GAP,
    )
```

---

# ARCHIVO: sonablues\components\navbar\desktop_user.py

```python
import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
)

from sonablues.styles.tokens import (
    NAVBAR_GAP,
)

from sonablues.components.ui.text import (
    caption_text,
    label_text,
)


def desktop_user() -> rx.Component:
    return rx.hstack(
        caption_text(
            "Hola",
        ),

        label_text(
            AuthState.current_user,
        ),

        rx.button(
            "Logout",
            on_click=AuthState.logout,
            background_color=ACCENT_COLOR,
            size="2",
            cursor="pointer",
        ),

        spacing=NAVBAR_GAP,
    )
```

---

# ARCHIVO: sonablues\components\navbar\mobile_menu.py

```python
import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.routes import (
    HOME_ROUTE,
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
)

from sonablues.styles.theme import (
    CARD_COLOR,
    TEXT_COLOR,
    ACCENT_COLOR,
)

from sonablues.styles.tokens import (
    NAVBAR_SECTION_GAP,
    NAVBAR_DRAWER_PADDING,
)

from sonablues.components.ui.layout import (
    stack_start,
)

from .nav_link import (
    nav_link,
)


def mobile_menu(
    current_path,
    is_home,
) -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon_button(
                rx.icon("menu"),
                variant="ghost",
                color=TEXT_COLOR,
            ),
        ),

        rx.drawer.overlay(),

        rx.drawer.content(
            stack_start(
                nav_link(
                    "Home",
                    HOME_ROUTE,
                    is_home,
                ),

                rx.cond(
                    AuthState.is_authenticated,
                    rx.fragment(
                        nav_link(
                            "Profile",
                            PROFILE_ROUTE,
                            current_path == PROFILE_ROUTE,
                        ),

                        nav_link(
                            "Favorites",
                            FAVORITES_ROUTE,
                            current_path == FAVORITES_ROUTE,
                        ),

                        rx.button(
                            "Logout",
                            on_click=AuthState.logout,
                            background_color=ACCENT_COLOR,
                            width="100%",
                        ),
                    ),
                ),
                spacing=NAVBAR_SECTION_GAP,
                padding=NAVBAR_DRAWER_PADDING,
            ),
            background_color=CARD_COLOR,
        ),
        direction="right",
    )
```

---

# ARCHIVO: sonablues\components\navbar\nav_link.py

```python
import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    ACCENT_COLOR,
)

from sonablues.styles.transitions import (
    CARD_TRANSITION,
)

from sonablues.components.ui.text import (
    label_text,
)


def nav_link(
    text,
    href,
    active,
):
    return rx.link(
        label_text(
            text,
            color=rx.cond(
                active,
                ACCENT_COLOR,
                TEXT_COLOR,
            ),
            weight="medium",
            white_space="nowrap",
            transition=CARD_TRANSITION,
            _hover={
                "color": ACCENT_COLOR,
            },
        ),
        href=href,
        text_decoration="none",
    )
```

---

# ARCHIVO: sonablues\components\navbar\navbar.py

```python
import reflex as rx
from sonablues.routes import (
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
    HOME_ROUTE,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
)
from sonablues.styles.tokens import (
    NAVBAR_SECTION_GAP,
    NAVBAR_PADDING_X,
    NAVBAR_PADDING_Y,
)
from sonablues.components.ui.text import (
    title_text,
)
from .desktop_navigation import (
    desktop_navigation,
)
from .desktop_user import (
    desktop_user,
)
from .mobile_menu import (
    mobile_menu,
)


def navbar() -> rx.Component:
    current_path = rx.State.router.page.path
    is_home = rx.cond(
        current_path == PROFILE_ROUTE,
        False,
        rx.cond(
            current_path == FAVORITES_ROUTE,
            False,
            True,
        ),
    )
    return rx.hstack(
        rx.link(
            title_text(
                "Sonablues",
                size={
                    "base": "5",
                    "md": "6",
                },
                white_space="nowrap",
                width="auto",
            ),
            href=HOME_ROUTE,
            text_decoration="none",
        ),
        rx.spacer(),
        rx.desktop_only(
            rx.hstack(
                desktop_navigation(
                    current_path,
                    is_home,
                ),
                desktop_user(),
                spacing=NAVBAR_SECTION_GAP,
            ),
        ),

        rx.mobile_and_tablet(
            mobile_menu(
                current_path,
                is_home,
            ),
        ),
        width="100%",
        padding_x=NAVBAR_PADDING_X,
        padding_y=NAVBAR_PADDING_Y,
        align="center",
        background_color=CARD_COLOR,
        border_bottom=f"1px solid {BORDER_COLOR}",
    )
```

---

# ARCHIVO: sonablues\components\navbar\ui.py

```python
from .navbar import (
    navbar,
)

from .mobile_menu import (
    mobile_menu,
)

from .desktop_user import (
    desktop_user,
)

from .nav_link import (
    nav_link,
)
```

---

# ARCHIVO: sonablues\components\search\__init__.py

```python
from .song_search_input import (
    song_search_input,
)
```

---

# ARCHIVO: sonablues\components\search\song_search_input.py

```python
import reflex as rx
from sonablues.states.song_search_state import (
    SongSearchState,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    CARD_BORDER,
    TEXT_COLOR,
    MUTED_TEXT,
    ACCENT_COLOR,
    ACCENT_BACKGROUND,
)
from sonablues.styles.radius import (
    INPUT_RADIUS,
    
)
from sonablues.styles.layout import (
    SEARCH_WIDTH
)
from sonablues.styles.transitions import (
    FAST_TRANSITION
)
from sonablues.styles.tokens import (
    INPUT_ICON_SIZE,
    )


def song_search_input() -> rx.Component:
    return rx.box(

        rx.image(
        src="/icons/search.svg",
        width=INPUT_ICON_SIZE,
        height=INPUT_ICON_SIZE,
        position="absolute",
        left="14px",
        top="50%",
        transform="translateY(-50%)",
        pointer_events="none",
        z_index="1",
    ),

        rx.input(

            placeholder="Search songs, techniques or difficulty...",

            value=SongSearchState.search_text,

            on_change=SongSearchState.set_search,

            width="100%",

            size="3",

            background=CARD_COLOR,

            border=CARD_BORDER,

            border_radius=INPUT_RADIUS,

            color=TEXT_COLOR,

            padding_left="2.5rem",

            padding_right="1rem",

            transition=FAST_TRANSITION,

            _placeholder={
                "color": "#7F8C99",
            },

            _hover={
                "border": f"1px solid {ACCENT_COLOR}",
            },

            _focus={
                "border": f"1px solid {ACCENT_COLOR}",
                "background": ACCENT_BACKGROUND,
                "box_shadow": "none",
            },
        ),
        position="relative",
        width="100%",
        max_width=SEARCH_WIDTH,
        margin="12px auto 0 0",
    )
```

---

# ARCHIVO: sonablues\components\song\__init__.py

```python
from .favorite_button import (
    favorite_button,
)

from .song_preview_card import (
    song_preview_card,
)

from .song_card import (
    song_card,
)

from .content import (
    song_content,
)

from .sections import (
    planned_content,
    practice_tips_section,
    song_hero,
    song_video_section,
)

from .difficulty_badge import (
    difficulty_badge,
)
```

---

# ARCHIVO: sonablues\components\song\content\__init__.py

```python
from .song_content import (
    song_content,
)
```

---

# ARCHIVO: sonablues\components\song\content\song_content.py

```python
import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.song.sections import (
    planned_content,
    song_video_section,
)
from sonablues.components.song import (
    favorite_button,
)
from sonablues.components.ui.layout import (
    content_stack,
)


def song_content(song: Song) -> rx.Component:
    return content_stack(
        favorite_button(
            song.slug,
        ),
        song_video_section(song),
        planned_content(),
    )
```

---

# ARCHIVO: sonablues\components\song\difficulty_badge.py

```python
import reflex as rx


def difficulty_badge(
    difficulty: str,
    size: str = "2",
) -> rx.Component:

    color_scheme = rx.cond(
        difficulty == "Beginner",
        "green",

        rx.cond(
            difficulty == "Intermediate",
            "orange",
            "red",
        ),
    )

    return rx.badge(
        difficulty,
        size=size,
        color_scheme=color_scheme,
        variant="soft",
    )
```

---

# ARCHIVO: sonablues\components\song\favorite_button.py

```python
import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    ACCENT_BACKGROUND,
)

from sonablues.styles.tokens import (
    INPUT_ICON_SIZE,
)


def favorite_button(
    song_slug: str,
    compact: bool = False,
) -> rx.Component:

    is_favorite = (
        AuthState.favorite_songs_list.contains(
            song_slug,
        )
    )

    icon = rx.cond(
        is_favorite,

        rx.image(
            src="/icons/heart-filled.svg",
            width=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),

            height=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),
        ),

        rx.image(
            src="/icons/heart-outline.svg",
            width=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),

            height=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),
        ),
    )

    return rx.button(
        rx.cond(
            compact,

            icon,

            rx.hstack(
                icon,

                rx.cond(
                    is_favorite,
                    "Favorited",
                    "Save",
                ),

                spacing="2",
                align="center",
            ),
        ),

        on_click=lambda: AuthState.toggle_favorite(
            song_slug,
        ),

        background_color=rx.cond(
            is_favorite,
            ACCENT_BACKGROUND,
            "rgba(0,0,0,0.48)" if compact else "transparent",
        ),

        color=rx.cond(
            is_favorite,
            ACCENT_COLOR,
            TEXT_COLOR,
        ),

        border=rx.cond(
            compact,
            "1px solid rgba(255,255,255,0.08)",

            rx.cond(
                is_favorite,
                f"1px solid {ACCENT_COLOR}",
                f"1px solid {BORDER_COLOR}",
            ),
        ),

        backdrop_filter=rx.cond(
            compact,
            "blur(10px)",
            "none",
        ),

        _hover={
            "border": f"1px solid {ACCENT_COLOR}",
            "color": ACCENT_COLOR,
            "background_color": ACCENT_BACKGROUND,
        },

        transition="all 0.2s ease",
        cursor="pointer",

        border_radius=rx.cond(
            compact,
            "9999px",
            "0.5rem",
        ),

        min_width=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        width=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        height=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        padding=rx.cond(
            compact,
            "0",
            "0.35rem 0.75rem 0.35rem 0.75rem",
        ),

        display="flex",
        align_items="center",
        justify_content="center",

        size="2",
    )
```

---

# ARCHIVO: sonablues\components\song\sections\__init__.py

```python
from .song_hero  import (
    song_hero,
)

from .planned_content import (
    planned_content,
)

from .practice_tips_section import (
    practice_tips_section,
)

from .video_section import (
    song_video_section,
)
```

---

# ARCHIVO: sonablues\components\song\sections\planned_content.py

```python
import reflex as rx

from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)

from sonablues.components.ui.sections import (
    section_card,
    section_header,
)

from sonablues.components.ui.layout import (
    content_stack,
)


def planned_content() -> rx.Component:
    return content_stack(
        section_header(
            PLANNED_CONTENT_TITLE,
            "Contenido adicional planeado para cada lección.",
        ),

        section_card(
            "01",
            "Contenido incluido",

            rx.unordered_list(
                rx.list_item("Tabs sincronizadas"),
                rx.list_item("Vídeo paso a paso"),
                rx.list_item("Backing track"),
                rx.list_item("Loop de práctica"),
                rx.list_item("Sección técnica detallada"),
                spacing="2",
                padding_left="1.25rem",
            ),
        ),
    )
```

---

# ARCHIVO: sonablues\components\song\sections\practice_tips_section.py

```python
import reflex as rx

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.components.ui.sections import (
    section_card,
    section_header,
)


def practice_tips_section() -> rx.Component:
    tips = [
        "Trabaja lentamente con metrónomo antes de subir velocidad.",
        "Mantén el vibrato controlado y consistente.",
        "Prioriza limpieza antes que velocidad.",
        "Escucha la dinámica de cada frase.",
    ]

    return content_stack(
        section_header(
            "Practice Tips",
            "Consejos importantes para estudiar la lección correctamente.",
        ),

        section_card(
            "01",
            "Consejos de práctica",

            rx.unordered_list(
                *[
                    rx.list_item(tip)
                    for tip in tips
                ],
                spacing="2",
                padding_left="1.25rem",
            ),
        ),
    )
```

---

# ARCHIVO: sonablues\components\song\sections\song_hero.py

```python
import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.ui.text import (
    secondary_text,
    page_title,
)

from sonablues.components.ui.primitives.badge import badge
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.song.difficulty_badge import (
    difficulty_badge,
)
from sonablues.components.ui.primitives import (
    badge_group,
)
from sonablues.components.ui.layout import (
    content_stack,
    stack_start,
)
from sonablues.styles.tokens import (
    BADGE_SIZE_DEFAULT,
    TEXT_SIZE_BODY,
    INLINE_GAP,
    CONTENT_GAP,
    SECTION_TEXT_WIDTH,
)


def song_hero(
    song: Song,
) -> rx.Component:
    return content_stack(
        cover_image(
            src=song.image,
            height="240px",
        ),

        stack_start(
            page_title(
                song.title,
            ),

            rx.hstack(
                difficulty_badge(
                    song.difficulty,
                    size=BADGE_SIZE_DEFAULT,
                ),

                badge(
                    song.tuning,
                    size=BADGE_SIZE_DEFAULT,
                ),

                spacing=INLINE_GAP,
                wrap="wrap",
            ),

            badge_group(
                song.techniques,
                size=BADGE_SIZE_DEFAULT,
            ),

            secondary_text(
                (
                    "Lección enfocada en dinámica, "
                    "control expresivo, vibrato "
                    "y musicalidad moderna."
                ),
                size=TEXT_SIZE_BODY,
                max_width=SECTION_TEXT_WIDTH,
            ),
            spacing=CONTENT_GAP,
        ),
        spacing=CONTENT_GAP,
    )
```

---

# ARCHIVO: sonablues\components\song\sections\video_section.py

```python
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
```

---

# ARCHIVO: sonablues\components\song\song_card.py

```python
import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.components.ui.text import (
    title_text,
)

from sonablues.components.ui.primitives.badge import badge
from sonablues.components.ui.navigation.card_link import card_link
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.song.favorite_button import (
    favorite_button,
)

from sonablues.components.song.difficulty_badge import (
    difficulty_badge,
)

from sonablues.components.ui.primitives import (
    badge_group,
)
from sonablues.components.ui.cards import (
    media_card,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    CARD_IMAGE_HEIGHT_MD,
    SONG_CARD_MIN_HEIGHT,
    TITLE_SIZE_CARD,
    INLINE_GAP,
    CONTENT_GAP,
)


def song_card(
    song: Song,
) -> rx.Component:
    return rx.box(
        card_link(
            media_card(
                rx.box(
                    favorite_button(
                        song.slug,
                        compact=True,
                    ),
                    position="absolute",
                    top="16px",
                    right="16px",
                    z_index="10",
                ),

                cover_image(
                    src=song.image,
                    height=CARD_IMAGE_HEIGHT_MD,
                ),

                stack_start(
                    title_text(
                        song.title,
                        size=TITLE_SIZE_CARD,
                    ),

                    rx.hstack(
                        difficulty_badge(
                            song.difficulty,
                        ),

                        badge(
                            song.tuning,
                        ),

                        spacing=INLINE_GAP,
                        wrap="wrap",
                    ),

                    badge_group(
                        song.techniques,
                        size="1",
                    ),
                    spacing=CONTENT_GAP,
                ),
                min_height=SONG_CARD_MIN_HEIGHT,
                position="relative",
            ),
            href=song_detail_route(
                song.slug,
            ),
        ),
    )
```

---

# ARCHIVO: sonablues\components\song\song_preview_card.py

```python
import reflex as rx

from sonablues.components.ui.navigation.card_link import card_link
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
    TITLE_SIZE_CARD,
)

from sonablues.data.models.song_model import Song


def song_preview_card(
    song: Song,
) -> rx.Component:
    return card_link(
        content_stack(
            cover_image(
                song.image,
                alt=song.title,
                height="220px",
            ),

            title_text(
                song.title,
                size=TITLE_SIZE_CARD,
            ),

            secondary_text(
                song.artist,
            ),

            secondary_text(
                song.difficulty,
            ),

            spacing=CONTENT_GAP,
        ),
        href=f"/song/{song.slug}",
    )
```

---

# ARCHIVO: sonablues\components\ui\__init__.py

```python
# UI namespace intentionally minimal.
```

---

# ARCHIVO: sonablues\components\ui\cards\__init__.py

```python
from .content_card import (
    content_card,
)

from .media_card import (
    media_card,
)
```

---

# ARCHIVO: sonablues\components\ui\cards\content_card.py

```python
import reflex as rx

from sonablues.components.ui.primitives import (
    surface,
)

from sonablues.styles.tokens import (
    CARD_MAX_WIDTH,
    CARD_PADDING_COMPACT,
)


def content_card(
    *children,
    padding: str = CARD_PADDING_COMPACT,
    max_width: str = CARD_MAX_WIDTH,
    **props,
) -> rx.Component:
    return surface(
        *children,
        width="100%",
        max_width=max_width,
        margin="0 auto",
        padding=padding,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\cards\media_card.py

```python
import reflex as rx

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.components.ui.primitives import (
    surface,
)


def media_card(
    media: rx.Component,
    *content,
    spacing: str | None = None,
    hoverable: bool = True,
    **props,
) -> rx.Component:
    return surface(
        content_stack(
            media,
            *content,
            spacing=spacing,
        ),
        hoverable=hoverable,
        overflow="hidden",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\feedback\__init__.py

```python
from .empty_state import (
    empty_state,
)
```

---

# ARCHIVO: sonablues\components\ui\feedback\empty_state.py

```python
import reflex as rx

from ..text import (
    page_title,
)

from ..text import (
    secondary_text,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def empty_state(
    title: str,
    description: str | None = None,
) -> rx.Component:
    return rx.vstack(
        page_title(title),

        rx.cond(
            description is not None,
            secondary_text(
                description,
                text_align="center",
                max_width="600px",
            ),
        ),

        spacing=CONTENT_GAP,
        align="center",
        width="100%",
        padding_top="4rem",
    )
```

---

# ARCHIVO: sonablues\components\ui\layout\__init__.py

```python
from .stacks import (
    content_stack,
    stack_start,
)

from .responsive_grid import (
    responsive_grid,
)
```

---

# ARCHIVO: sonablues\components\ui\layout\responsive_grid.py

```python
import reflex as rx

from sonablues.styles.tokens import (
    GRID_GAP,
)


DEFAULT_GRID_COLUMNS = {
    "base": "1",
    "sm": "2",
    "lg": "3",
    "2xl": "4",
}


def responsive_grid(
    *children,
    columns: dict | None = None,
    spacing: str = GRID_GAP,
    **props,
) -> rx.Component:
    return rx.grid(
        *children,
        columns=columns or DEFAULT_GRID_COLUMNS,
        spacing=spacing,
        width="100%",
        align_items="stretch",
        auto_rows="1fr",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\layout\stacks.py

```python
import reflex as rx

from sonablues.styles.tokens import (
    CONTENT_GAP,
    SECTION_GAP,
)


def stack_start(
    *children,
    spacing=CONTENT_GAP,
    align: str = "start",
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=align,
        width=width,
        **props,
    )


def content_stack(
    *children,
    spacing=SECTION_GAP,
    align: str = "stretch",
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=align,
        width=width,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\media\__init__.py

```python
from .cover_image import (
    cover_image,
)

from .video_embed import (
    video_embed,
)
```

---

# ARCHIVO: sonablues\components\ui\media\cover_image.py

```python
import reflex as rx

from sonablues.styles.tokens import (
    CARD_RADIUS,
)


def cover_image(
    src: str,
    height: str,
    width: str = "100%",
    object_fit: str = "cover",
    object_position: str = "center",
    radius: str = CARD_RADIUS,
    **props,
) -> rx.Component:
    return rx.image(
        src=src,
        loading="lazy",
        width=width,
        height=height,
        object_fit=object_fit,
        object_position=object_position,
        border_radius=radius,
        display="block",
        flex_shrink="0",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\media\video_embed.py

```python
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
```

---

# ARCHIVO: sonablues\components\ui\navigation\__init__.py

```python
from .card_link import (
    card_link,
)

from .app_button import (
    app_button,
)
```

---

# ARCHIVO: sonablues\components\ui\navigation\app_button.py

```python
import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)


def app_button(
    text: str,
    href: str | None = None,
    variant: str = "solid",
    size: str = "3",
    **props,
) -> rx.Component:

    button = rx.button(
        text,
        background_color=(
            ACCENT_COLOR
            if variant == "solid"
            else "transparent"
        ),
        variant=variant,
        size=size,
        cursor="pointer",
        **props,
    )

    if not href:
        return button

    return rx.link(
        button,
        href=href,
        text_decoration="none",
    )
```

---

# ARCHIVO: sonablues\components\ui\navigation\card_link.py

```python
import reflex as rx


def card_link(
    *children,
    href: str,
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.link(
        *children,
        href=href,
        width=width,
        text_decoration="none",
        display="block",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\primitives\__init__.py

```python
from .badge import (
    badge,
)

from .badge_group import (
    badge_group,
)

from .surface import (
    surface,
)
```

---

# ARCHIVO: sonablues\components\ui\primitives\badge.py

```python
import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    BORDER_COLOR,
    ACCENT_BACKGROUND,
)


def tag_badge(
    text: str,
    size: str = "2",
) -> rx.Component:
    return rx.badge(
        text,
        size=size,
        color=TEXT_COLOR,
        background_color=ACCENT_BACKGROUND,
        border=f"1px solid {BORDER_COLOR}",
        padding_x="0.5rem",
        padding_y="0.15rem",
    )


def badge(
    text: str,
    size: str = "2",
) -> rx.Component:
    return rx.badge(
        text,
        size=size,
    )
```

---

# ARCHIVO: sonablues\components\ui\primitives\badge_group.py

```python
import reflex as rx

from .badge import (
    tag_badge,
)

from sonablues.styles.tokens import (
    INLINE_GAP,
)


def badge_group(
    items,
    size: str = "2",
) -> rx.Component:
    return rx.flex(
        rx.foreach(
            items,
            lambda item: tag_badge(
                item,
                size=size,
            ),
        ),
        wrap="wrap",
        gap=INLINE_GAP,
        width="100%",
    )
```

---

# ARCHIVO: sonablues\components\ui\primitives\surface.py

```python
import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)

from sonablues.styles.transitions import (
    CARD_TRANSITION,
)

from sonablues.styles.tokens import (
    CARD_HOVER_TRANSFORM,
    CARD_PADDING,
    CARD_RADIUS,
    CARD_BORDER,
    CARD_BACKGROUND,
)


def surface(
    *children,
    padding: str = CARD_PADDING,
    radius: str = CARD_RADIUS,
    background: str = CARD_BACKGROUND,
    border: str = CARD_BORDER,
    hoverable: bool = False,
    hover_transform: str = CARD_HOVER_TRANSFORM,
    transition: str = CARD_TRANSITION,
    **props,
) -> rx.Component:

    hover_styles = (
        {
            "transform": hover_transform,
            "border": f"1px solid {ACCENT_COLOR}",
        }
        if hoverable
        else {}
    )

    return rx.box(
        *children,
        background=background,
        border=border,
        border_radius=radius,
        padding=padding,
        transition=transition,
        _hover=hover_styles,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\sections\__init__.py

```python
from .page_header import (
    page_header,
)

from .section_card import (
    section_card,
)

from .section_header import (
    section_header,
)
```

---

# ARCHIVO: sonablues\components\ui\sections\page_header.py

```python
import reflex as rx
from ..text import (
    title_text,
    secondary_text,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
    SECTION_TEXT_WIDTH,
)


def page_header(
    title: str,
    description: str | None = None,
    **props,
) -> rx.Component:
    return stack_start(
        title_text(
            title,
            size=TITLE_SIZE_PAGE,
            text_align="center",
        ),
        rx.cond(
            description,
            secondary_text(
                description,
                text_align="center",
                max_width=SECTION_TEXT_WIDTH,
            ),
        ),
        align="center",
        margin_x="auto",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\sections\section_card.py

```python
import reflex as rx

from ..layout import (
    stack_start,
)

from ..text import (
    section_label,
)

from sonablues.components.ui.cards import (
    content_card,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
    ACCENT_BACKGROUND,
    BADGE_TEXT_COLOR,
)

from sonablues.styles.tokens import (
    BADGE_RADIUS,
    BADGE_SIZE_SMALL,
    COMPACT_STACK_SPACING,
    TEXT_BLOCK_SPACING,
    TEXT_INLINE_PADDING,
    CONTENT_GAP,
)


def section_card_header(
    badge: str,
    title: str,
) -> rx.Component:
    return rx.hstack(
        rx.badge(
            badge,
            radius=BADGE_RADIUS,
            size=BADGE_SIZE_SMALL,
            color=BADGE_TEXT_COLOR,
            background=ACCENT_BACKGROUND,
            border=f"1px solid {ACCENT_COLOR}08",
        ),

        section_label(
            title,
        ),

        spacing=COMPACT_STACK_SPACING,
        align="center",
        width="100%",
        padding_x=TEXT_INLINE_PADDING,
        padding_top=TEXT_BLOCK_SPACING,
    )


def section_card(
    badge: str,
    title: str,
    *children,
    spacing: str = CONTENT_GAP,
    **props,
) -> rx.Component:
    return content_card(
        stack_start(
            section_card_header(
                badge,
                title,
            ),

            *children,

            spacing=spacing,
        ),
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\sections\section_header.py

```python
import reflex as rx

from ..text import (
    title_text,
    secondary_text,
)

from ..layout import (
    stack_start,
)

from sonablues.styles.tokens import (
    SECTION_TEXT_WIDTH,
    SECTION_MAX_WIDTH,
    TITLE_SIZE_SECTION,
)


def section_header(
    title: str,
    description: str | None = None,
    title_size: str = TITLE_SIZE_SECTION,
    max_width: str = SECTION_MAX_WIDTH,
    align: str = "center",
    **props,
) -> rx.Component:
    return stack_start(
        title_text(
            title,
            size=title_size,
            text_align="center",
        ),

        rx.cond(
            description,
            secondary_text(
                description,
                text_align="center",
                max_width=SECTION_TEXT_WIDTH,
            ),
        ),

        align=align,
        max_width=max_width,
        margin_x="auto",
        padding_x="1rem",
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\text\__init__.py

```python
from .text_components import (
    body_text,
    caption_text,
    label_text,
    secondary_text,
    title_text,
)

from .section_label import (
    section_label,
)

from .page_title import (
    page_title,
)
```

---

# ARCHIVO: sonablues\components\ui\text\page_title.py

```python
from ..text import (
    title_text,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
)


def page_title(
    text: str,
):
    return title_text(
        text,
        size=TITLE_SIZE_PAGE,
    )
```

---

# ARCHIVO: sonablues\components\ui\text\section_label.py

```python
import reflex as rx

from sonablues.styles.theme import (
    SECTION_LABEL_COLOR,
)
from sonablues.styles.tokens import (
    FONT_WEIGHT_MEDIUM,
    LETTER_SPACING_TIGHT,
    LINE_HEIGHT_COMPACT,
)


def section_label(
    text: str,
    **props,
) -> rx.Component:
    return rx.text(
        text,
        font_weight=FONT_WEIGHT_MEDIUM,
        letter_spacing=LETTER_SPACING_TIGHT,
        line_height=LINE_HEIGHT_COMPACT,
        color=SECTION_LABEL_COLOR,
        **props,
    )
```

---

# ARCHIVO: sonablues\components\ui\text\text_components.py

```python
import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    MUTED_TEXT,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_CARD,
    TEXT_SIZE_SECONDARY,
    TEXT_SIZE_BODY,
    TEXT_SIZE_SMALL,
)


def base_text(
    component,
    text: str,
    width: str = "100%",
    **props,
) -> rx.Component:
    return component(
        text,
        width=width,
        **props,
    )


def title_text(
    text: str,
    size: str = TITLE_SIZE_CARD,
    color: str = TEXT_COLOR,
    **props,
) -> rx.Component:
    return base_text(
        rx.heading,
        text,
        size=size,
        color=color,
        **props,
    )


def body_text(
    text: str,
    size: str = TEXT_SIZE_BODY,
    color: str = TEXT_COLOR,
    **props,
) -> rx.Component:
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def secondary_text(
    text: str,
    size: str = TEXT_SIZE_SECONDARY,
    color: str = MUTED_TEXT,
    **props,
) -> rx.Component:
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def caption_text(
    text: str,
    size: str = TEXT_SIZE_SMALL,
    color: str = MUTED_TEXT,
    **props,
) -> rx.Component:
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def label_text(
    text: str,
    size: str = TEXT_SIZE_SMALL,
    color: str = TEXT_COLOR,
    weight: str = "bold",
    **props,
) -> rx.Component:
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        weight=weight,
        **props,
    )
```

---

# ARCHIVO: sonablues\config.py

```python

```

---

# ARCHIVO: sonablues\constants.py

```python
ELECTRIC = "electric"

ACOUSTIC = "acoustic"


VIDEO_LESSONS_TITLE = "Video lessons"

PLANNED_CONTENT_TITLE = "Contenido planeado"

SONG_NOT_FOUND = "Song not found"

ARTISTS_TITLE = "Artists"
```

---

# ARCHIVO: sonablues\data\__init__.py

```python

```

---

# ARCHIVO: sonablues\data\lessons_data.py

```python

```

---

# ARCHIVO: sonablues\data\mock\__init__.py

```python

```

---

# ARCHIVO: sonablues\data\mock\artist_indexes.py

```python
from sonablues.data.mock.artists_data import ARTISTS


ARTISTS_BY_SLUG = {
    artist.slug: artist
    for instrument_artists in ARTISTS.values()
    for artist in instrument_artists
}
```

---

# ARCHIVO: sonablues\data\mock\artists_data.py

```python
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
```

---

# ARCHIVO: sonablues\data\mock\song_indexes.py

```python
from sonablues.data.mock.songs_data import SONGS


SONGS_BY_SLUG = {
    song.slug: song
    for artist_songs in SONGS.values()
    for song in artist_songs
}
```

---

# ARCHIVO: sonablues\data\mock\songs_data.py

```python
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

            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.webp",
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
            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.webp",
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

            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.webp",
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

            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.webp",
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

            image="/images/songs/john-mayer/slow-dancing-in-a-burning-room.webp",
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

            image="/images/songs/stevie-ray-vaughan/pride-and-joy.webp",
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

            image="/images/songs/tommy-emmanuel/angelina.webp",
        ),
    ],
}
```

---

# ARCHIVO: sonablues\data\models\__init__.py

```python

```

---

# ARCHIVO: sonablues\data\models\artist_model.py

```python
from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    slug: str
    description: str
    image: str
```

---

# ARCHIVO: sonablues\data\models\difficulty.py

```python
from enum import StrEnum


class Difficulty(StrEnum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


DIFFICULTY_ORDER = {
    Difficulty.BEGINNER: 1,
    Difficulty.INTERMEDIATE: 2,
    Difficulty.ADVANCED: 3,
}
```

---

# ARCHIVO: sonablues\data\models\song_model.py

```python
from dataclasses import dataclass, field
from sonablues.data.models.difficulty import Difficulty


@dataclass
class Video:
    title: str
    youtube_id: str


@dataclass
class Song:
    title: str
    slug: str
    artist: str
    difficulty: Difficulty
    tuning: str
    techniques: list[str] = field(
        default_factory=list
    )
    videos: list[Video] = field(
        default_factory=list
    )
    image: str = ""
```

---

# ARCHIVO: sonablues\data\models\user.py

```python

```

---

# ARCHIVO: sonablues\database\__init__.py

```python

```

---

# ARCHIVO: sonablues\database\db.py

```python
from sqlmodel import SQLModel, Session, create_engine


DATABASE_URL = "sqlite:///sonablues.db"


engine = create_engine(
    DATABASE_URL,
    echo=True,
)


def create_db():

    SQLModel.metadata.create_all(engine)


def get_session():

    return Session(engine)
```

---

# ARCHIVO: sonablues\estructura.txt

```text
Estructura actual:
C:\Users\mazin\Desktop\Python\sonablues\.venv


C:\Users\mazin\Desktop\Python\sonablues\assets\styles.css


C:\Users\mazin\Desktop\Python\sonablues\assets\icons\flame.svg
C:\Users\mazin\Desktop\Python\sonablues\assets\icons\heart-filled.svg
C:\Users\mazin\Desktop\Python\sonablues\assets\icons\heart-outline.svg
C:\Users\mazin\Desktop\Python\sonablues\assets\icons\music.svg
C:\Users\mazin\Desktop\Python\sonablues\assets\icons\waveform.svg
C:\Users\mazin\Desktop\Python\sonablues\assets\icons\search.svg


C:\Users\mazin\Desktop\Python\sonablues\assets\images\hero\hero-guitar.jpg
C:\Users\mazin\Desktop\Python\sonablues\assets\images\songs\sloe-gin.jpg

C:\Users\mazin\Desktop\Python\sonablues\.gitignore
C:\Users\mazin\Desktop\Python\sonablues\README.md
C:\Users\mazin\Desktop\Python\sonablues\requirements.txt
C:\Users\mazin\Desktop\Python\sonablues\rxconfig.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\cards\artist_card.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\cards\featured_song_card.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\cards\featured_song_card.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\cards\song_card.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\home\featured_songs.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\home\home_hero.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\home\learning_section.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\layout\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\layout\content_container.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\layout\page_container.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\layout\section_container.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\navbar.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\nav_link.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\desktop_navigation.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\desktop_user.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\navbar\mobile_menu.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\search__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\search\song_search_input.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\song\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\song\hero.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\song\video_section.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\song\planned_content.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\song\content\song_content.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\app_badge.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\app_button.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\badge_group.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\card_link.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\content_section.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\cover_image.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\empty_state.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\favorite_button.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\media_card.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\muted_text.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\page_header.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\page_title.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\responsive_grid.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\section_header.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\section_title.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\stacks.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\surface.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\text.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\ui\video_embed.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\footer.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\components\layouts.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\models\artist_model.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\models\difficulty.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\models\song_model.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\models\user.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\mock\artist_indexes.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\mock\artists_data.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\mock\song_indexes.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\mock\songs_data.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\data\lessons_data.py




C:\Users\mazin\Desktop\Python\sonablues\sonablues\database\db.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\artists.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\favorites.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\home.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\instruments.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\login.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\profile.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\register.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\song_detail.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\pages\songs.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\routes\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\routes\routes.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\services\artist_service.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\services\auth_service.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\services\song_service.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\services\user_service.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\states\__init__.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\states\auth_state.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\states\profile_state.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\states\song_search_state.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\layout.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\radius.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\spacing.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\theme.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\transitions.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\styles\tokens.py


C:\Users\mazin\Desktop\Python\sonablues\sonablues\utils\protected.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\utils\security.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\utils\youtube.py

C:\Users\mazin\Desktop\Python\sonablues\sonablues\app_pages.pyP
C:\Users\mazin\Desktop\Python\sonablues\sonablues\config.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\constants.py
C:\Users\mazin\Desktop\Python\sonablues\sonablues\sonablues.py


magenes - Home
1. Hero image cinematográfica en Home

Una sola imagen grande.

Por ejemplo:

guitarra en estudio oscuro
amplificador vintage
escenario con luz cálida
manos tocando guitarra
micrófono blues/jazz
ambiente analógico

NO:

stock corporativo
guitarristas sonriendo
fotos demasiado coloridas
imágenes “curso online”

Tu paleta pide:

negros
azules oscuros
ámbar cálido
sombras
grano
ambiente nocturno


Dónde conseguir imágenes buenas
Gratis y bastante decentes
Unsplash
Pexels

Busca:

blues guitar
guitar amp
dark studio guitar
vintage guitar
moody guitar
guitar close up
blues stage



Repo:
https://github.com/Marcial-Godes/sonablues
https://github.com/Marcial-Godes/sonablues/tree/main/assets
https://github.com/Marcial-Godes/sonablues/tree/main/assets/icons
https://github.com/Marcial-Godes/sonablues/tree/main/assets/images
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/cards
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/home
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/layout
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/navbar
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/search
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/song
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/ui
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/components/ui/text
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/data
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/data/mock
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/data/models
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/database
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/models
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/pages
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/routes
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/services
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/states
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/styles
https://github.com/Marcial-Godes/sonablues/tree/main/sonablues/utils


```

---

# ARCHIVO: sonablues\models\__init__.py

```python

```

---

# ARCHIVO: sonablues\models\user.py

```python
from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    username: str

    password_hash: str

    favorite_songs: str = ""
```

---

# ARCHIVO: sonablues\pages\__init__.py

```python

```

---

# ARCHIVO: sonablues\pages\artists.py

```python
import reflex as rx
from sonablues.constants import (
    ARTISTS_TITLE,
)
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.artist.artist_card import (
    artist_card,
)
from sonablues.services.artist_service import (
    get_artists_by_instrument,
)

from sonablues.components.ui.text import (
    page_title,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)


def artists_page(
    instrument_slug: str,
) -> rx.Component:
    artists = get_artists_by_instrument(
        instrument_slug,
    )
    return base_layout(
        page_container(
            content_stack(
                page_title(
                    ARTISTS_TITLE,
                ),
                responsive_grid(
                    *[
                        artist_card(artist)
                        for artist in artists
                    ],
                ),
            )
        )
    )
```

---

# ARCHIVO: sonablues\pages\favorites.py

```python
import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.song import (
    song_card,
)
from sonablues.states.profile_state import (
    ProfileState,
)
from sonablues.utils.protected import (
    protected_page,
)

from sonablues.components.ui.text import (
    page_title,
)
from sonablues.components.ui.feedback import (
    empty_state,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)


def favorites_content() -> rx.Component:
    return page_container(
        content_stack(
            page_title(
                "Favorite Songs",
            ),
            rx.cond(
                ProfileState.favorite_songs.length() > 0,
                responsive_grid(
                    rx.foreach(
                        ProfileState.favorite_songs,
                        lambda song: song_card(song),
                    ),
                ),
                empty_state(
                    title="No favorite songs yet",
                    description=(
                        "Start adding songs to your favorites."
                    ),
                ),
            ),
        )
    )


def favorites_page() -> rx.Component:
    return base_layout(
        protected_page(
            favorites_content(),
        )
    )
```

---

# ARCHIVO: sonablues\pages\home.py

```python
import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.ui.layout import (
    content_stack,
)
from sonablues.components.home.ui import (
    featured_songs,
    home_hero,
    learning_section,
)


def home_page() -> rx.Component:
    return base_layout(
        page_container(
            content_stack(
                home_hero(),
                learning_section(),
                featured_songs(),
            )
        )
    )
```

---

# ARCHIVO: sonablues\pages\instruments.py

```python
import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.instrument.ui import (
    instrument_card,
)

from sonablues.components.layout import (
    page_container,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)

from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
)


def instruments_page() -> rx.Component:
    return base_layout(
        page_container(
            content_stack(
                title_text(
                    "Explorar",
                    size=TITLE_SIZE_PAGE,
                ),
                secondary_text(
                    "Selecciona instrumento.",
                    size="4",
                ),
                responsive_grid(
                    instrument_card(
                        "Guitarra eléctrica",
                        "Blues, rock y fraseo eléctrico.",
                        "/artists/electric",
                    ),
                    instrument_card(
                        "Guitarra acústica",
                        "Fingerstyle y dinámica acústica.",
                        "/artists/acoustic",
                    ),
                    columns={
                        "base": "1",
                        "md": "2",
                    },
                ),
            )
        )
    )
```

---

# ARCHIVO: sonablues\pages\login.py

```python
import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.states.auth_state import (
    AuthState,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    ACCENT_COLOR,
)
from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def login_page() -> rx.Component:
    return base_layout(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Login",
                        size="7",
                    ),
                    rx.input(
                        placeholder="Usuario",
                        on_change=AuthState.set_username,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        on_change=AuthState.set_password,
                        width="100%",
                    ),
                    rx.button(
                        "Entrar",
                        on_click=AuthState.login,
                        width="100%",
                        background_color=ACCENT_COLOR,
                    ),
                    rx.text(
                        AuthState.error_message,
                        color="red",
                    ),
                    spacing=CONTENT_GAP,
                    width="100%",
                ),
                background_color=CARD_COLOR,
                padding="2rem",
                border_radius="12px",
                width="400px",
            ),
            width="100%",
            min_height="70vh",
        )
    )
```

---

# ARCHIVO: sonablues\pages\profile.py

```python
import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.ui.text import (
    secondary_text,
    title_text,
    body_text,
    label_text,
    page_title,
)
from sonablues.components.ui.primitives import (
    surface,
)
from sonablues.components.ui.layout import (
    stack_start,
    content_stack,
)
from sonablues.states.auth_state import (
    AuthState,
)
from sonablues.utils.protected import (
    protected_page,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_SECTION,
    CONTENT_GAP,
    SECTION_GAP,
)



def profile_content() -> rx.Component:
    return page_container(
        content_stack(
            page_title(
                "Profile",
                ),
            secondary_text(
                f"Welcome back, {AuthState.current_user}",
                ),
            surface(
                stack_start(
                    title_text(
                        "Account Overview",
                        size=TITLE_SIZE_SECTION,
                        ),
                    secondary_text(
                        (
                            "Your personal dashboard will appear here "
                            "in future updates."
                        ),
                    ),
                    rx.divider(),
                    stack_start(
                        label_text(
                            "Planned features:",
                        ),
                        body_text("• Learning progress"),
                        body_text("• Recently viewed lessons"),
                        body_text("• Practice history"),
                        body_text("• Custom playlists"),
                        body_text("• Personal notes"),
                        spacing=CONTENT_GAP,
                    ),
                ),
            ),
        )
    )

def profile_page() -> rx.Component:
    return base_layout(
        protected_page(
            profile_content(),
        )
    )
```

---

# ARCHIVO: sonablues\pages\register.py

```python
import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.states.auth_state import AuthState
from sonablues.styles.tokens import (
    CONTENT_GAP,
)



def register_page() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading(
                "Registro",
                size="7",
            ),
            rx.input(
                placeholder="Usuario",
                on_change=AuthState.set_username,
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                on_change=AuthState.set_password,
            ),
            rx.button(
                "Crear cuenta",
                on_click=AuthState.register,
            ),
            rx.text(
                AuthState.error_message,
                color="red",
            ),
            spacing=CONTENT_GAP,
            align="start",
        ),
    )
```

---

# ARCHIVO: sonablues\pages\song_detail.py

```python
import reflex as rx
from sonablues.constants import (
    SONG_NOT_FOUND,
)
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    content_container,
)
from sonablues.components.song import (
    practice_tips_section,
    song_hero,
    song_content,
)
from sonablues.components.ui.feedback import (
    empty_state,
)
from sonablues.services import (
    get_song,
)
from sonablues.styles.tokens import (
    PAGE_GAP,
)


def song_detail_page(
    song_slug: str,
) -> rx.Component:
    song = get_song(song_slug)
    if not song:
        return base_layout(
            empty_state(
                title=SONG_NOT_FOUND,
                description=(
                    "The requested lesson does not exist "
                    "or is currently unavailable."
                ),
            )
        )

    return base_layout(
        content_container(
            rx.vstack(
                song_hero(song),
                song_content(song),
                practice_tips_section(),
                width="100%",
                spacing=PAGE_GAP,
                align="start",
            ),
        )
    )
```

---

# ARCHIVO: sonablues\pages\songs.py

```python
import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.layout import (
    page_container,
)

from sonablues.components.search import (
    song_search_input,
)

from sonablues.components.song import (
    song_card,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)
from sonablues.components.ui.sections import (
    page_header,
)

from sonablues.components.ui.feedback import (
    empty_state,
)

from sonablues.services.artist_service import (
    get_artist,
)

from sonablues.services.song_service import (
    get_songs_by_artist,
)


def songs_page(
    artist_slug: str,
) -> rx.Component:
    artist = get_artist(
        artist_slug,
    )

    if not artist:
        return base_layout(
            empty_state(
                "Artist not found",
            )
        )

    songs = get_songs_by_artist(
        artist_slug,
    )

    return base_layout(
        page_container(
            content_stack(
                page_header(
                    title=artist.name,
                    description=artist.description,
                ),

                song_search_input(),

                responsive_grid(
                    *[
                        song_card(song)
                        for song in songs
                    ],
                ),
            )
        )
    )
```

---

# ARCHIVO: sonablues\routes\__init__.py

```python
from .routes import (
    HOME_ROUTE,
    LOGIN_ROUTE,
    REGISTER_ROUTE,
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
    INSTRUMENTS_ROUTE,
    ELECTRIC_ARTISTS_ROUTE,
    ACOUSTIC_ARTISTS_ROUTE,
    songs_route,
    song_detail_route,
)
```

---

# ARCHIVO: sonablues\routes\routes.py

```python
HOME_ROUTE = "/"
LOGIN_ROUTE = "/login"
REGISTER_ROUTE = "/register"
PROFILE_ROUTE = "/profile"
FAVORITES_ROUTE = "/favorites"

INSTRUMENTS_ROUTE = "/instruments"

ELECTRIC_ARTISTS_ROUTE = "/artists/electric"
ACOUSTIC_ARTISTS_ROUTE = "/artists/acoustic"


def songs_route(artist_slug: str) -> str:
    return f"/songs/{artist_slug}"


def song_detail_route(song_slug: str) -> str:
    return f"/song/{song_slug}"
```

---

# ARCHIVO: sonablues\services\__init__.py

```python
from .song_service import (
    get_song,
    get_songs_by_artist,
)

from .artist_service import (
    get_artist,
    get_artists_by_instrument,
)
```

---

# ARCHIVO: sonablues\services\artist_service.py

```python
from sonablues.data.mock.artists_data import ARTISTS
from sonablues.data.mock.artist_indexes import ARTISTS_BY_SLUG

from sonablues.data.models.artist_model import Artist


def get_artist(artist_slug: str) -> Artist | None:
    return ARTISTS_BY_SLUG.get(artist_slug)


def get_artists_by_instrument(instrument_slug: str) -> list[Artist]:
    return ARTISTS.get(instrument_slug, [])
```

---

# ARCHIVO: sonablues\services\auth_service.py

```python
from sonablues.services.user_service import (
    get_user_by_username,
)

from sonablues.utils.security import (
    verify_password,
)


def authenticate_user(
    username: str,
    password: str,
):

    user = get_user_by_username(username)

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash,
    ):
        return None

    return user
```

---

# ARCHIVO: sonablues\services\song_service.py

```python
from sonablues.data.mock.songs_data import SONGS
from sonablues.data.mock.song_indexes import SONGS_BY_SLUG
from sonablues.data.models.song_model import Song
from sonablues.data.models.difficulty import (
    DIFFICULTY_ORDER,
)


def get_song(song_slug: str) -> Song | None:
    return SONGS_BY_SLUG.get(song_slug)


def get_songs_by_artist(artist_slug: str) -> list[Song]:
    return SONGS.get(artist_slug, [])

def get_featured_songs():
    featured_slugs = {
        "sloe-gin",
        "spanish-boots",
        "little-wing",
    }

    return [
        song
        for artist_songs in SONGS.values()
        for song in artist_songs
        if song.slug in featured_slugs
    ]


def sort_songs_by_difficulty(
    songs: list[Song],
) -> list[Song]:

    return sorted(
        songs,
        key=lambda song: DIFFICULTY_ORDER[
            song.difficulty
        ],
    )
```

---

# ARCHIVO: sonablues\services\user_service.py

```python
from sqlmodel import select

from sonablues.database.db import get_session
from sonablues.models.user import User
from sonablues.utils.security import hash_password


def create_user(
    username: str,
    password: str,
):
    with get_session() as session:
        existing_user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if existing_user:
            return False
        user = User(
            username=username,
            password_hash=hash_password(password),
        )
        session.add(user)
        session.commit()
        return True


def get_user_by_username(
    username: str,
):
    with get_session() as session:
        return session.exec(
            select(User).where(
                User.username == username
            )
        ).first()

def add_favorite_song(
    username: str,
    song_slug: str,
):
    with get_session() as session:
        user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if not user:
            return
        favorites = [
            slug
            for slug in user.favorite_songs.split(",")
            if slug
        ]
        if song_slug not in favorites:
            favorites.append(song_slug)
        user.favorite_songs = ",".join(
            favorites
        )
        session.add(user)
        session.commit()
        

def get_favorite_songs(
    username: str,
) -> list[str]:
    user = get_user_by_username(
        username,
    )
    if not user:
        return []
    return [
        slug
        for slug in user.favorite_songs.split(",")
        if slug
    ]
    

def remove_favorite_song(
    username: str,
    song_slug: str,
):

    with get_session() as session:
        user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if not user:
            return
        favorites = [
            slug
            for slug in user.favorite_songs.split(",")
            if slug
        ]
        favorites = [
            slug
            for slug in favorites
            if slug != song_slug
        ]
        user.favorite_songs = ",".join(
            favorites
        )
        session.add(user)
        session.commit()
        

def is_favorite_song(
    username: str,
    song_slug: str,
) -> bool:
    favorites = get_favorite_songs(
        username,
    )
    return song_slug in favorites
```

---

# ARCHIVO: sonablues\sonablues.py

```python
import reflex as rx
from sonablues.app_pages import register_pages


app = rx.App()

register_pages(app)
```

---

# ARCHIVO: sonablues\states\__init__.py

```python
from .auth_state import (
    AuthState,
)

from .song_search_state import (
    SongSearchState,
)
```

---

# ARCHIVO: sonablues\states\auth_state.py

```python
# sonablues/states/auth_state.py

import reflex as rx

from sonablues.database.db import create_db

from sonablues.services.auth_service import (
    authenticate_user,
)

from sonablues.services.user_service import (
    create_user,
    add_favorite_song,
    remove_favorite_song,
    is_favorite_song,
    get_favorite_songs,
)


create_db()


class AuthState(rx.State):

    username: str = ""

    password: str = ""

    is_authenticated: bool = False

    current_user: str = ""
    
    stored_user: str = rx.LocalStorage("")

    error_message: str = ""

    @rx.var
    def logged_user(self) -> str:

        return self.current_user

    @rx.var
    def favorite_songs_list(self) -> list[str]:

        if not self.current_user:
            return []

        return get_favorite_songs(
            self.current_user,
        )

    def is_song_favorite(
        self,
        song_slug: str,
    ) -> bool:
        return song_slug in self.favorite_songs_list
    
    def restore_session(self):
        if self.stored_user:
            self.current_user = self.stored_user
            self.is_authenticated = True

    def set_username(
        self,
        value: str,
    ):

        self.username = value

    def set_password(
        self,
        value: str,
    ):

        self.password = value

    def register(self):

        success = create_user(
            self.username,
            self.password,
        )

        if not success:

            self.error_message = (
                "El usuario ya existe"
            )

            return

        self.error_message = ""

        return rx.redirect("/login")

    def login(self):

        user = authenticate_user(
            self.username,
            self.password,
        )

        if not user:

            self.error_message = (
                "Usuario o contraseña incorrectos"
            )

            return

        self.is_authenticated = True

        self.current_user = user.username
        
        self.stored_user = user.username

        self.error_message = ""

        return rx.redirect("/profile")

    def add_favorite(
        self,
        song_slug: str,
    ):

        if not self.is_authenticated:
            return rx.redirect("/login")

        add_favorite_song(
            self.current_user,
            song_slug,
        )

    def remove_favorite(
        self,
        song_slug: str,
    ):

        if not self.is_authenticated:
            return

        remove_favorite_song(
            self.current_user,
            song_slug,
        )

    def toggle_favorite(
        self,
        song_slug: str,
    ):

        if not self.is_authenticated:
            return rx.redirect("/login")

        if is_favorite_song(
            self.current_user,
            song_slug,
        ):

            remove_favorite_song(
                self.current_user,
                song_slug,
            )

        else:

            add_favorite_song(
                self.current_user,
                song_slug,
            )

        self.current_user = self.current_user

    def logout(self):

        self.is_authenticated = False

        self.current_user = ""
        
        self.stored_user = ""

        self.username = ""

        self.password = ""

        return rx.redirect("/")
```

---

# ARCHIVO: sonablues\states\profile_state.py

```python
# sonablues/states/profile_state.py

import reflex as rx
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.services.user_service import (
    get_favorite_songs,
)
from sonablues.data.mock.song_indexes import (
    SONGS_BY_SLUG,
)
from sonablues.states.auth_state import (
    AuthState,
)


class ProfileState(rx.State):
    favorite_songs: list[Song] = []

    async def load_favorites(self):
        auth_state = await self.get_state(
            AuthState,
        )
        if not auth_state.logged_user:
            self.favorite_songs = []
            return
        favorite_slugs = get_favorite_songs(
            auth_state.logged_user,
        )
        self.favorite_songs = [
            SONGS_BY_SLUG[slug]
            for slug in favorite_slugs
            if slug in SONGS_BY_SLUG
        ]
```

---

# ARCHIVO: sonablues\states\song_search_state.py

```python
import reflex as rx
from sonablues.services.song_service import (
    get_songs_by_artist,
)


class SongSearchState(rx.State):
    search_text: str = ""
    def set_search(
        self,
        value: str,
    ):
        self.search_text = value
    def filtered_songs(
        self,
        artist_slug: str,
    ):
        songs = get_songs_by_artist(
            artist_slug,
        )
        query = self.search_text.strip().lower()
        if not query:
            return songs

        return [
            song
            for song in songs
            if (
                query in song.title.lower()
                or
                query in str(song.difficulty).lower()
                or
                any(
                    query in technique.lower()
                    for technique in song.techniques
                )
            )
        ]
```

---

# ARCHIVO: sonablues\styles\__init__.py

```python

```

---

# ARCHIVO: sonablues\styles\layout.py

```python
SEARCH_WIDTH = "820px"
CONTENT_WIDTH = "1440px"
```

---

# ARCHIVO: sonablues\styles\radius.py

```python
INPUT_RADIUS = "14px"
CARD_RADIUS = "20px"
IMAGE_RADIUS = "18px"
BADGE_RADIUS = "8px"
BUTTON_RADIUS = "10px"
```

---

# ARCHIVO: sonablues\styles\theme.py

```python
import reflex as rx


BACKGROUND_COLOR = "#182028"
CARD_COLOR = "#27313B"
BORDER_COLOR = "#506070"
TEXT_COLOR = "#D9D7D1"
MUTED_TEXT = "#8A9AA8"
ACCENT_COLOR = "#8FA3B8"
CARD_BORDER = f"1px solid {BORDER_COLOR}"
ACCENT_BACKGROUND = "#8FA3B814"
ICON_COLOR = "#A7B7C8"
BEGINNER_COLOR = "green"
INTERMEDIATE_COLOR = "orange"
ADVANCED_COLOR = "red"
SECTION_LABEL_COLOR = "#C3CED8"
BADGE_TEXT_COLOR = "#9FB0C0"

base_style = {
    "background_color": BACKGROUND_COLOR,
    "color": TEXT_COLOR,
}
```

---

# ARCHIVO: sonablues\styles\tokens.py

```python
# =========================
# Motion
# =========================
CARD_HOVER_TRANSFORM = "translateY(-4px)"


# =========================
# Layout
# =========================
SECTION_MAX_WIDTH = "960px"
SECTION_TEXT_WIDTH = "42ch"
CONTENT_MAX_WIDTH = "1200px"
MEDIA_MAX_WIDTH = "860px"
CARD_MAX_WIDTH = "980px"
PAGE_PADDING_X = {
    "base": "1rem",
    "md": "2rem",
    "xl": "3rem",
}
SECTION_PADDING_TOP = {
    "base": "1rem",
    "md": "1.5rem",
    "lg": "2rem",
}
SECTION_PADDING_BOTTOM = {
    "base": "1.5rem",
    "md": "2rem",
    "lg": "2.5rem",
}
SECTION_PADDING_Y = {
    "base": "1rem",
    "md": "1.5rem",
    "lg": "2rem",
}


# =========================
# Spacing
# =========================
SECTION_GAP = {
    "base": "4",
    "md": "5",
    "lg": "6",
}

CONTENT_GAP = {
    "base": "3",
    "md": "4",
}

PAGE_GAP = {
    "base": "6",
    "md": "7",
    "lg": "8",
}

INLINE_GAP = "2"

GRID_GAP = {
    "base": "4",
    "md": "5",
}


# =========================
# Typography
# =========================
TITLE_SIZE_PAGE = {
    "base": "6",
    "md": "7",
    "lg": "8",
}
TITLE_SIZE_SECTION = {
    "base": "5",
    "md": "6",
}
TITLE_SIZE_CARD = {
    "base": "4",
    "md": "5",
}

TITLE_SIZE_HERO = {
    "base": "7",
    "md": "8",
    "lg": "9",
}

TEXT_SIZE_BODY = "4"
TEXT_SIZE_SECONDARY = "3"
TEXT_SIZE_SMALL = "2"

BADGE_SIZE_SMALL = "1"
BADGE_SIZE_DEFAULT = "2"
BADGE_SIZE_LARGE = "3"


# =========================
# Card System
# =========================
CARD_PADDING = {
    "base": "1rem",
    "md": "1.25rem",
    "lg": "1.5rem",
}
CARD_PADDING_COMPACT = {
    "base": "0.5rem",
    "md": "0.75rem",
}
CARD_RADIUS = "24px"
MEDIA_RADIUS = "16px"
CARD_MIN_HEIGHT = "unset"
CARD_BORDER = "1px solid rgba(143,163,184,0.22)"
CARD_BACKGROUND = "rgba(37,48,62,0.92)"


# =========================
# Card Image Heights
# =========================
CARD_IMAGE_HEIGHT_SM = {
    "base": "170px",
    "md": "190px",
}
CARD_IMAGE_HEIGHT_MD = {
    "base": "200px",
    "md": "220px",
}
CARD_IMAGE_HEIGHT_LG = {
    "base": "220px",
    "md": "240px",
    "xl": "260px",
}
CARD_IMAGE_HEIGHT_HERO = {
    "base": "240px",
    "md": "340px",
    "lg": "420px",
}


# =========================
# Song / Artist Specific
# =========================
SONG_HERO_IMAGE_HEIGHT = {
    "base": "220px",
    "md": "320px",
    "lg": "420px",
}
SONG_CARD_MIN_HEIGHT = {
    "base": "520px",
}
ARTIST_CARD_MIN_HEIGHT = {
    "base": "100%",
}
FEATURED_CARD_MIN_HEIGHT = {
    "base": "100%",
}


# =========================
# Home Hero
# =========================
HOME_HERO_MOBILE_IMAGE_HEIGHT = {
    "base": "220px",
    "sm": "260px",
}
HOME_HERO_DESKTOP_IMAGE_HEIGHT = "420px"
HOME_HERO_TEXT_MAX_WIDTH = "560px"
HOME_HERO_TEXT_MIN_WIDTH = {
    "lg": "420px",
}


# =========================
# Inputs / Icons
# =========================
INPUT_ICON_SIZE = "18px"
LEARNING_ICON_SIZE = "22px"


# =========================
# Instrument Cards
# =========================
INSTRUMENT_CARD_MIN_HEIGHT = {
    "base": "120px",
    "md": "140px",
}


# =========================
# Footer
# =========================
FOOTER_PADDING_Y = {
    "base": "0.75rem",
    "md": "1rem",
}
FOOTER_PADDING_X = {
    "base": "1rem",
    "md": "2rem",
}
FOOTER_TEXT_SIZE = "2"


# =========================
# Navbar
# =========================

NAVBAR_GAP = {
    "base": "3",
    "md": "4",
}

NAVBAR_SECTION_GAP = {
    "base": "5",
    "md": "6",
}

NAVBAR_PADDING_X = {
    "base": "1rem",
    "md": "1.5rem",
    "lg": "2rem",
}

NAVBAR_PADDING_Y = {
    "base": "0.8rem",
    "md": "1rem",
}
NAVBAR_DRAWER_PADDING = {
    "base": "1.5rem",
    "md": "2rem",
}


FONT_WEIGHT_NORMAL = "400"
FONT_WEIGHT_MEDIUM = "500"
FONT_WEIGHT_SEMIBOLD = "600"
FONT_WEIGHT_BOLD = "700"

LETTER_SPACING_TIGHT = "-0.01em"
LETTER_SPACING_NORMAL = "0"

LINE_HEIGHT_COMPACT = "1.2"
LINE_HEIGHT_NORMAL = "1.5"
BADGE_RADIUS = "full"

# =========================
# Typography Layout
# =========================

TEXT_BLOCK_SPACING = "0.35rem"
TEXT_INLINE_PADDING = "0.35rem"
SECTION_BLOCK_SPACING = "1.5rem"
COMPACT_STACK_SPACING = "1"
LIST_SPACING = "3"
LIST_PADDING_LEFT = "1.25rem"
```

---

# ARCHIVO: sonablues\styles\transitions.py

```python
FAST_TRANSITION = "all 0.2s ease"
CARD_TRANSITION = "0.2s ease"
```

---

# ARCHIVO: sonablues\utils\__init__.py

```python

```

---

# ARCHIVO: sonablues\utils\protected.py

```python
import reflex as rx
from sonablues.states.auth_state import AuthState
from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def protected_page(
    component: rx.Component,
) -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        component,
        rx.center(
            rx.vstack(
                rx.heading(
                    "Acceso restringido",
                    size="7",
                ),
                rx.text(
                    "Debes iniciar sesión.",
                ),
                rx.button(
                    "Ir al login",
                    on_click=rx.redirect("/login"),
                ),
                spacing=CONTENT_GAP,
            ),
            height="70vh",
        ),
    )
```

---

# ARCHIVO: sonablues\utils\security.py

```python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )
```

---

# ARCHIVO: sonablues\utils\youtube.py

```python
def youtube_embed_url(
    youtube_id: str,
) -> str:

    return (
        f"https://www.youtube.com/embed/{youtube_id}"
    )
```

---

