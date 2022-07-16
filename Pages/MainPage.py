from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class MainPage(BasePage):
    __ROUTE_BUTTON = (By.XPATH, '//button[@id="hArJGc"]')
    __ROUTE_MENU = (By.XPATH, '//*[@id="omnibox-directions"]')
    __DESTINATION_FROM = (By.XPATH, '//div[@id="sb_ifc51"]/input')
    __DESTINATION_TO = (By.XPATH, '//div[@id="sb_ifc52"]/input')
    __SEARCH_ROUTE = (By.XPATH, '//*[@id="directions-searchbox-1"]/button[1]')
    __CHANGE_DIRECTION_BTN = (By.XPATH, '//div[@class="PLEQOe reverse"]//parent::button')
    __SUGGESTED_ROUTES = (By.XPATH, "//div[contains(@id,'section-directions-trip')]")


    #TRAVEL OPTIONS
    __AUTOMATO_ROUTE=(By.XPATH, "//img[contains(@src,'ic_directions_filled_blue900')]//parent::button")
    __CAR_ROUTE=(By.XPATH, "//img[contains(@src,'directions_car_grey800')]//parent::button")
    __PUBLIC_TRANSPORTATION_ROUTE=(By.XPATH, "//img[contains(@src,'directions_transit_grey800')]//parent::button")
    __WALK_ROUTE=(By.XPATH, "//img[contains(@src,'directions_walk_grey800')]//parent::button")
    __BIKE_ROUTE=(By.XPATH, "//img[contains(@src,'directions_bike_grey800')]//parent::button")
    __AIRPLANE_ROUTE=(By.XPATH, "//img[contains(@src,'flight_grey800')]//parent::button")

    #OPTIONS
    __OPTIONS_BTN = (By.XPATH, "//button[contains(@class,'OcYctc fontTitleSmall XbJon')]")
    __OPTIONS_AVOID_HIGH_WAY = (By.XPATH, '//input[@id="pane.directions-options-avoid-highways"]/parent::div')
    __OPTIONS_AVOID_TOOLS = (By.XPATH, '//input[@id="pane.directions-options-avoid-tolls"]/parent::div')
    __OPTIONS_AVOID_FERRIES = (By.XPATH, '//input[@id="pane.directions-options-avoid-ferries"]/parent::div')
    __OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-highways"]')
    __OPTIONS_AVOID_TOOLS_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-tolls"]')
    __OPTIONS_AVOID_FERRIES_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-avoid-ferries"]')

    __OPTIONS_AUTOMATIC_UNITS = (By.XPATH, '//input[@id="pane.directions-options-units-auto"]/following-sibling::label')
    __OPTIONS_AUTOMATIC_MILES = (By.XPATH, '//input[@id="pane.directions-options-units-miles"]/following-sibling::label')
    __OPTIONS_AUTOMATIC_KM = (By.XPATH, '//input[@id="pane.directions-options-units-km"]/following-sibling::label')
    __OPTIONS_AUTOMATIC_UNITS_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-auto"]')
    __OPTIONS_AUTOMATIC_MILES_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-miles"]')
    __OPTIONS_AUTOMATIC_KM_CHECK_STATUS = (By.XPATH, '//input[@id="pane.directions-options-units-km"]')

    #DETAIL PAGE
    __DETAIL_PAGE_OPEN = (By.XPATH, "//div[@class='m6QErb DxyBCb kA9KIf dS8AEf']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_route(self):
        self._click(self.__ROUTE_BUTTON)
        self._wait_for_element(self.__ROUTE_MENU)

    def set_destination_from(self, destination):
        self._type(self.__DESTINATION_FROM, destination)

    def set_destination_to(self, destination):
        self._type(self.__DESTINATION_TO, destination)

    def set_transport_option(self, transport_option):
        options = {
                    'auto': self.__AUTOMATO_ROUTE,
                    'car': self.__CAR_ROUTE,
                    'public_transportation': self.__PUBLIC_TRANSPORTATION_ROUTE,
                    'walk': self.__WALK_ROUTE,
                    'bike': self.__BIKE_ROUTE,
                    'airplane': self.__AIRPLANE_ROUTE
                  }
        self._click(options[transport_option])

    def search_route(self, destination_from, destination_to, transport_option='auto'):
        self.set_destination_from(destination_from)
        self.set_destination_to(destination_to)
        self._click(self.__SEARCH_ROUTE)
        self.set_transport_option(transport_option)
        # self._wait_for_element_to_be_visible(self.__SUGGESTED_ROUTES, 20)

    def open_route_options(self, status_open=True):
        if status_open:
            self._click(self.__OPTIONS_BTN,timeout=20, animation=True)
            assert self._is_aria_expanded(self.__OPTIONS_BTN)==True
        else:
            self._click(self.__OPTIONS_BTN, timeout=20, animation=True)
            assert self._is_aria_expanded(self.__OPTIONS_BTN)==False


    def set_route_options(self, high_way=False, pay_tool=False, ferry=False, units='auto'):
        self.open_route_options(True)

        if high_way:
            if self._is_option_checked(self.__OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS):
                pass
            else:
                self._click(self.__OPTIONS_AVOID_HIGH_WAY)
        else:
            if self._is_option_checked(self.__OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS):
                self._click(self.__OPTIONS_AVOID_HIGH_WAY)
            else:
                pass

        if pay_tool:
            if self._is_option_checked(self.__OPTIONS_AVOID_TOOLS_CHECK_STATUS):
                pass
            else:
                self._click(self.__OPTIONS_AVOID_TOOLS)
        else:
            if self._is_option_checked(self.__OPTIONS_AVOID_TOOLS_CHECK_STATUS):
                self._click(self.__OPTIONS_AVOID_TOOLS)
            else:
                pass

        if ferry:
            if self._is_option_checked(self.__OPTIONS_AVOID_FERRIES_CHECK_STATUS):
                pass
            else:
                self._click(self.__OPTIONS_AVOID_FERRIES)
        else:
            if self._is_option_checked(self.__OPTIONS_AVOID_FERRIES_CHECK_STATUS):
                self._click(self.__OPTIONS_AVOID_FERRIES)
            else:
                pass

        if units=='auto':
            self._click(self.__OPTIONS_AUTOMATIC_UNITS)
            assert self._is_option_checked(self.__OPTIONS_AUTOMATIC_UNITS_CHECK_STATUS)==True
        elif units=='miles':
            self._click(self.__OPTIONS_AUTOMATIC_MILES)
            assert self._is_option_checked(self.__OPTIONS_AUTOMATIC_MILES_CHECK_STATUS)==True
        elif units=='km':
            self._click(self.__OPTIONS_AUTOMATIC_KM)
            assert self._is_option_checked(self.__OPTIONS_AUTOMATIC_KM_CHECK_STATUS)==True

        self.open_route_options(False)

        return {
                    'high_way': self._is_option_checked(self.__OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS),
                    'tool': self._is_option_checked(self.__OPTIONS_AVOID_TOOLS_CHECK_STATUS),
                    'ferries': self._is_option_checked(self.__OPTIONS_AVOID_FERRIES_CHECK_STATUS),
                    'units': units
                }

    def get_suggested_routes(self):
        route_objects = self._wait_for_elements(self.__SUGGESTED_ROUTES)
        routes_dict={}
        for route in route_objects:
            route_text = route.text.split('\n')
            routes_dict[route_objects.index(route)]= {'time':route_text[0]}
            routes_dict[route_objects.index(route)]['distance'] = route_text[1]
            routes_dict[route_objects.index(route)]['description'] = route_text[2]
            routes_dict[route_objects.index(route)]['time_with_traffic'] = route_text[3]
        return routes_dict

    def select_route(self, id):
        self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))

    def open_one_of_routes(self, id):
        self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))
        if not self._is_displayed(self.__DETAIL_PAGE_OPEN):
            self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))
        assert self._is_displayed(self.__DETAIL_PAGE_OPEN)==True

    def get_longest_route(self, all_routes):
        longest_route_distance=0
        longest_route = ''
        for key,value in all_routes.items():
            if int(value['distance'].split()[0])>longest_route_distance:
                longest_route_distance=int(value['distance'].split()[0])
                longest_route = key
        return longest_route, longest_route_distance

    def change_direction(self):
        destination_from = self._get_element_value(self.__DESTINATION_FROM)
        destination_to = self._get_element_value(self.__DESTINATION_TO)
        self._click(self.__CHANGE_DIRECTION_BTN)
        assert self._get_element_value(self.__DESTINATION_FROM) == destination_to
        assert self._get_element_value(self.__DESTINATION_TO) == destination_from


