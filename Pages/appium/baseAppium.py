
from datetime import datetime, timedelta
from selenium.webdriver.support.wait import WebDriverWait
from Pages.basePage import BasePage
from Pages.appium.appium_locators import GoogleMapsLocators
from selenium.webdriver.support import expected_conditions as EC


class AppiumPage(BasePage):
    def __init__(self, appium_driver, request):
        super().__init__(appium_driver)
        self.request = request
        self.maps_locators = GoogleMapsLocators()
        print('Appium page init')

    def _click(self, locator, timeout=15, scroll=False):
        super()._click(locator, timeout=timeout, scroll=scroll)

    def _wait_for_element_to_be_clickable(self, locator, timeout=10):
        time_end = datetime.now() + timedelta(timeout)
        while True:
            try:
                return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            except Exception:
                if time_end > datetime.now():
                    raise Exception(
                        "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                            timeout))

    def start_maps(self):
        self.close_maps()
        self.driver.activate_app("com.google.android.apps.maps")
        self._wait_for_element(self.maps_locators.SEARCH_BOX)

    def close_maps(self):
        self.driver.terminate_app("com.google.android.apps.maps")

    def search_location(self, location):
        self._click(self.maps_locators.SEARCH_BOX)
        self.edit_text(location)
        self.click_direction_btn()

    def click_direction_btn(self):
        self._click(self.maps_locators.DIRECTION_BTN)

    def set_destination(self, from_dest='', to_dest=''):
        if from_dest:
            self._click(self.maps_locators.FROM_DEST)
            self.edit_text(from_dest)
        if to_dest:
            self._click(self.maps_locators.TO_DEST)
            self.edit_text(to_dest)

    def edit_text(self, text):
        self._type(self.maps_locators.EDIT_SEARCH_BOX, text)
        self._click(self.maps_locators.select_location(text))

    def get_route_distance(self):
        self._wait_for_elements(self.maps_locators.DISTANCE_VALUE)
        time, distance, *irrelevant = self._get_elements_text(self.maps_locators.DISTANCE_VALUE)
        distance = ''.join(filter(str.isdigit, distance))
        #returns tuple of time and km
        return time, distance
