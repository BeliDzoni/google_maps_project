from Pages.basePage import BasePage


class AppiumPage(BasePage):
    def __init__(self, appium_driver, request):
        super().__init__(appium_driver)
        self.request = request
        print('Appium page init')

    def start_maps(self):
        self.driver.activate_app("com.google.android.apps.maps")

    def close_maps(self):
        self.driver.terminate_app("com.google.android.apps.maps")