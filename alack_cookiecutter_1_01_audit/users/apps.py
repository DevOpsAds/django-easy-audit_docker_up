import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "alack_cookiecutter_1_01_audit.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import alack_cookiecutter_1_01_audit.users.signals  # noqa: F401
