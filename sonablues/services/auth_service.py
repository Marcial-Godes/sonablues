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