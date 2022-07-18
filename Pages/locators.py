from selenium.webdriver.common.by import By


class MainPageLocators:
    ROUTE_BUTTON = (By.XPATH, '//img[contains(@src,"directions-2x")]//parent::button[@id="hArJGc"]')
    ROUTE_MENU = (By.XPATH, '//*[@id="omnibox-directions"]')
    DESTINATION_FROM = (By.XPATH, '//div[@id="directions-searchbox-0"]/*/div[contains(@id,"sb_ifc51")]/input')
    DESTINATION_TO = (By.XPATH, '//div[@id="directions-searchbox-1"]/*/div[contains(@id,"sb_ifc52")]/input')
    SEARCH_ROUTE = (By.XPATH, '//*[@id="directions-searchbox-1"]/button[1]')
    CHANGE_DIRECTION_BTN = (By.XPATH, '//div[@class="PLEQOe reverse"]//parent::button')
    SUGGESTED_ROUTES = (By.XPATH, "//div[contains(@id,'section-directions-trip')]")

    # TRAVEL OPTIONS
    AUTOMATO_ROUTE = (By.XPATH, "//img[contains(@src,'ic_directions')]//parent::button")
    CAR_ROUTE = (By.XPATH, "//img[contains(@src,'directions_car')]//parent::button")
    PUBLIC_TRANSPORTATION_ROUTE = (By.XPATH, "//img[contains(@src,'directions_transit')]//parent::button")
    WALK_ROUTE = (By.XPATH, "//img[contains(@src,'directions_walk')]//parent::button")
    BIKE_ROUTE = (By.XPATH, "//img[contains(@src,'directions_bike')]//parent::button")
    AIRPLANE_ROUTE = (By.XPATH, "//img[contains(@src,'flight')]//parent::button")

    # OPTIONS
    OPTIONS_BTN = (By.XPATH, "//button[contains(@class,'OcYctc fontTitleSmall XbJon')]")
    OPTIONS_AVOID_HIGH_WAY = (By.XPATH, '//input[@id="pane.directions-options-avoid-highways"]/parent::div')
    OPTIONS_AVOID_TOOLS = (By.XPATH, '//input[@id="pane.directions-options-avoid-tolls"]/parent::div')
    OPTIONS_AVOID_FERRIES = (By.XPATH, '//input[@id="pane.directions-options-avoid-ferries"]/parent::div')
    OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-highways"]')
    OPTIONS_AVOID_TOOLS_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-tolls"]')
    OPTIONS_AVOID_FERRIES_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-ferries"]')

    OPTIONS_AUTOMATIC_UNITS = (By.XPATH, '//input[@id="pane.directions-options-units-auto"]/following-sibling::label')
    OPTIONS_AUTOMATIC_MILES = (By.XPATH, '//input[@id="pane.directions-options-units-miles"]/following-sibling::label')
    OPTIONS_AUTOMATIC_KM = (By.XPATH, '//input[@id="pane.directions-options-units-km"]/following-sibling::label')
    OPTIONS_AUTOMATIC_UNITS_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-auto"]')
    OPTIONS_AUTOMATIC_MILES_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-miles"]')
    OPTIONS_AUTOMATIC_KM_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-km"]')

    # DETAIL PAGE
    DETAIL_PAGE_OPEN = (By.XPATH, "//div[contains(@class,'m6QErb DxyBCb kA9KIf dS8AEf')]")


class DetailsPageLocators:
    BACK_BTN = (By.XPATH, '//button[@class="ysKsp"]')
    ROUTE_INFO = (By.XPATH, "//div[@class='PNEhTd Hk4XGb']")
