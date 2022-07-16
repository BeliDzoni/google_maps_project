import pytest

@pytest.mark.usefixtures("setup")
class BaseTest:
    pass


@pytest.mark.usefixtures("api_setup")
class ApiTest:
    pass