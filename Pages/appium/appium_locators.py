from appium.webdriver.common.appiumby import AppiumBy


class GoogleMapsLocators:
    SEARCH_BOX = (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
    EDIT_SEARCH_BOX = (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    SELECT_LOCATION = (AppiumBy.XPATH, "//android.widget.TextView[contains()]")
    DIRECTION_BTN = (AppiumBy.XPATH, '//*[contains(@content-desc,"Directions")]')
    FROM_DEST = (AppiumBy.ID, "com.google.android.apps.maps:id/directions_startpoint_textbox")
    TO_DEST = (AppiumBy.ID, "com.google.android.apps.maps:id/directions_endpoint_textbox")
    DISTANCE_VALUE = (AppiumBy.XPATH, '//*[@resource-id="com.google.android.apps.maps:id/sheet_header"]'
                                      '//android.widget.TextView')

    def select_location(self, location):
        return (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{location}')]")

