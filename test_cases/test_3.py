import pytest
from test_cases.base_test import AppiumTest


class TestApi(AppiumTest):
    @pytest.mark.appium
    @pytest.mark.cicd
    def test_budapest_route_appium(self):
        self.appium.start_maps()
        self.appium.close_maps()

