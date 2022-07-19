import pytest

@pytest.mark.usefixtures("initialize_driver")
@pytest.mark.usefixtures("api_setup")
@pytest.mark.usefixtures("page_object_init")
class BaseTest:
    pass


@pytest.mark.usefixtures("api_setup")
class ApiTest:
    pass