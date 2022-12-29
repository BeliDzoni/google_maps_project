

from Pages.basePage import BasePage
from Pages.appium.appium_locators import GoogleMapsLocators
from appium.webdriver.extensions.android.nativekey import AndroidKey


class AppiumPage(BasePage):
    def __init__(self, appium_driver, request):
        super().__init__(appium_driver)
        self.request = request
        self.maps_locators = GoogleMapsLocators()
        print('Appium page init')

    def _click(self, locator, timeout=30):
        super()._click(locator, timeout=timeout, scroll=False)

    def start_maps(self):
        self.close_maps()
        self.driver.activate_app("com.google.android.apps.maps")

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

