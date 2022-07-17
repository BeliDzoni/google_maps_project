import pytest

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("api_setup")
class BaseTest:
    pass


@pytest.mark.usefixtures("api_setup")
class ApiTest:
    pass