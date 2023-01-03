import pytest
from test_cases.base_test import AppiumTest
import time

class TestApi(AppiumTest):
    @pytest.mark.appium
    @pytest.mark.cicd
    def test_budapest_route_appium(self):
        self.appium.start_maps()
        self.appium.search_location('Budapest')
        self.appium.set_destination(from_dest='Novi Sad')
        time.sleep(5)
        self.appium.close_maps()

    @pytest.mark.appium
    @pytest.mark.cicd
    def test_budapest_route_appium2(self):
        self.appium.start_maps()
        self.appium.search_location('Budapest')
        self.appium.set_destination(from_dest='Novi Sad')
        time.sleep(5)
        self.appium.close_maps()

