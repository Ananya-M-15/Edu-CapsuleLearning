from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    """
    Custom authentication backend that permits case-insensitive username lookups.
    Ensures users registering with auto-capitalization (e.g. on mobile keyboards)
    can authenticate regardless of input casing, while preserving secure password checks.
    Gracefully handles databases where legacy case-variant usernames coexist.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if not username or not password:
            return None

        clean_username = str(username).strip()
        candidates = list(
            UserModel._default_manager.filter(
                **{f"{UserModel.USERNAME_FIELD}__iexact": clean_username}
            )
        )
        if not candidates:
            # Run default password hasher to mitigate timing attacks (Django ticket #20760)
            UserModel().set_password(password)
            return None

        # 1. Prioritize exact case match if one exists and credentials are valid
        for user in candidates:
            if getattr(user, UserModel.USERNAME_FIELD) == clean_username:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user

        # 2. Check remaining case-insensitive candidate users
        for user in candidates:
            if getattr(user, UserModel.USERNAME_FIELD) != clean_username:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user

        UserModel().set_password(password)
        return None
