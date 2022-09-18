from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver, request):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()
        self.details_page = request.cls.details_page

    def open_route(self):
        self._click(self.main_page_locators.ROUTE_BUTTON)
        self._wait_for_element(self.main_page_locators.ROUTE_MENU)

    def set_destination_from(self, destination):
        self._type(self.main_page_locators.DESTINATION_FROM, Keys.CONTROL, 'A')
        self._type(self.main_page_locators.DESTINATION_FROM, destination)

    def set_destination_to(self, destination):
        self._type(self.main_page_locators.DESTINATION_TO, Keys.CONTROL, 'A')
        self._type(self.main_page_locators.DESTINATION_TO, destination)

    def set_transport_option(self, transport_option):
        options = {
            'auto': self.main_page_locators.AUTOMATO_ROUTE,
            'car': self.main_page_locators.CAR_ROUTE,
            'public_transportation': self.main_page_locators.PUBLIC_TRANSPORTATION_ROUTE,
            'walk': self.main_page_locators.WALK_ROUTE,
            'bike': self.main_page_locators.BIKE_ROUTE,
            'airplane': self.main_page_locators.AIRPLANE_ROUTE
        }
        self._click(options[transport_option])

    def search_route(self, destination_from, destination_to, transport_option='auto'):
        self.set_destination_from(destination_from)
        self.set_destination_to(destination_to)
        self._click(self.main_page_locators.SEARCH_ROUTE)
        self.set_transport_option(transport_option)
        # self._wait_for_element_to_be_visible(self.main_page_locators.SUGGESTED_ROUTES, 20)

    def open_route_options(self, status_open=True):
        if status_open:
            self._click(self.main_page_locators.OPTIONS_BTN, timeout=20, animation=True)
            assert self._is_aria_expanded(self.main_page_locators.OPTIONS_BTN)
        else:
            self._click(self.main_page_locators.OPTIONS_BTN, timeout=20, animation=True)
            assert self._is_aria_expanded(self.main_page_locators.OPTIONS_BTN) is False

    def set_route_options(self, high_way=False, pay_tool=False, ferry=False, units='auto'):
        self.open_route_options(True)

        if high_way:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS):
                pass
            else:
                self._click(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY)
        else:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS):
                self._click(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY)
            else:
                pass

        if pay_tool:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_TOOLS_CHECK_STATUS):
                pass
            else:
                self._click(self.main_page_locators.OPTIONS_AVOID_TOOLS)
        else:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_TOOLS_CHECK_STATUS):
                self._click(self.main_page_locators.OPTIONS_AVOID_TOOLS)
            else:
                pass

        if ferry:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_FERRIES_CHECK_STATUS):
                pass
            else:
                self._click(self.main_page_locators.OPTIONS_AVOID_FERRIES)
        else:
            if self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_FERRIES_CHECK_STATUS):
                self._click(self.main_page_locators.OPTIONS_AVOID_FERRIES)
            else:
                pass

        if units == 'auto':
            self._click(self.main_page_locators.OPTIONS_AUTOMATIC_UNITS)
            assert self._is_option_checked(self.main_page_locators.OPTIONS_AUTOMATIC_UNITS_CHECK_STATUS)
        elif units == 'miles':
            self._click(self.main_page_locators.OPTIONS_AUTOMATIC_MILES)
            assert self._is_option_checked(self.main_page_locators.OPTIONS_AUTOMATIC_MILES_CHECK_STATUS)
        elif units == 'km':
            self._click(self.main_page_locators.OPTIONS_AUTOMATIC_KM)
            assert self._is_option_checked(self.main_page_locators.OPTIONS_AUTOMATIC_KM_CHECK_STATUS)

        options_dict = {
            'high_way': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS),
            'tool': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_TOOLS_CHECK_STATUS),
            'ferries': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_FERRIES_CHECK_STATUS),
            'units': units
        }

        self.open_route_options(False)

        return options_dict

    def get_suggested_routes(self):
        route_objects = self._wait_for_elements(self.main_page_locators.SUGGESTED_ROUTES)
        routes_dict = {}
        for route in route_objects:
            route_text = route.text.split('\n')
            routes_dict[route_objects.index(route)] = {'time': route_text[0]}
            routes_dict[route_objects.index(route)]['distance'] = route_text[1]
            routes_dict[route_objects.index(route)]['description'] = route_text[2]
            routes_dict[route_objects.index(route)]['time_with_traffic'] = route_text[3]
        return routes_dict

    def select_route(self, id):
        if self._get_role_of_element(
                (By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id))) == 'button':
            self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))

    def open_details_of_routes(self, id):
        self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))
        if not self._is_displayed(self.main_page_locators.DETAIL_PAGE_OPEN, 3):
            self._click((By.XPATH, "//div[contains(@id,'section-directions-trip-{}')]".format(id)))
        assert self._is_displayed(self.main_page_locators.DETAIL_PAGE_OPEN)

    def get_longest_route(self, all_routes):
        longest_route_distance = 0
        longest_route = ''
        for key, value in all_routes.items():
            distance_value = float(value['distance'].replace('.', '').replace(',', '.').split()[0])
            if distance_value > longest_route_distance:
                longest_route_distance = distance_value
                longest_route = key
        return longest_route, longest_route_distance

    def change_direction(self):
        destination_from = self._get_element_value(self.main_page_locators.DESTINATION_FROM)
        destination_to = self._get_element_value(self.main_page_locators.DESTINATION_TO)
        self._click(self.main_page_locators.CHANGE_DIRECTION_BTN)
        assert self._get_element_value(self.main_page_locators.DESTINATION_FROM) == destination_to
        assert self._get_element_value(self.main_page_locators.DESTINATION_TO) == destination_from

    def click_back_btn(self):
        self.details_page.click_back_btn()
