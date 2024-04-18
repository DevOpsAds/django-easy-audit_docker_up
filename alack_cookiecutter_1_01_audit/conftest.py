import pytest

from alack_cookiecutter_1_01_audit.users.models import User
from alack_cookiecutter_1_01_audit.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()
