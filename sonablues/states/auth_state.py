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