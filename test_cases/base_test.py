import pytest
import subprocess

@pytest.mark.usefixtures("api_setup")
@pytest.mark.usefixtures("page_object_init")
class BaseTest:
    pass


@pytest.mark.usefixtures("api_setup")
class ApiTest:
    pass


@pytest.mark.usefixtures("initialize_appium_server")
@pytest.mark.usefixtures("appium_init")
class AppiumTest:
    pass

@pytest.mark.usefixtures("initialize_appium_server")
@pytest.mark.usefixtures("api_setup")
@pytest.mark.usefixtures("page_object_init")
@pytest.mark.usefixtures("appium_init")
class AllTest:
    pass