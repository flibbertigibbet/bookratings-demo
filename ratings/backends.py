from django.contrib.auth import backends, get_user_model


UserModel = get_user_model()


class CookieUserBackend(backends.ModelBackend):
    """
    This backend is to be used in conjunction with the ``CookieUserMiddleware``
    found in the middleware module of this package, and is used when the server
    is handling authentication outside of Django, via a cookie.
    By default, the ``authenticate`` method creates ``User`` objects for
    usernames that don't already exist in the database.
    """

    def user_can_authenticate(self, user):
        return True

    def authenticate(self, request, remote_user):
        """
        The username passed as ``remote_user`` is considered trusted. Return
        the ``User`` object with the given username. Create a new ``User``
        object if user with given name does not exist yet.
        """
        if not remote_user:
            return
        username = remote_user
        user, created = UserModel._default_manager.get_or_create(**{
            UserModel.USERNAME_FIELD: username
        })
        return user
