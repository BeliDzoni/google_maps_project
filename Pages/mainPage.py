from selenium.webdriver import Keys
from Pages.basePage import BasePage
from Pages.locators import MainPageLocators
from Pages.detailsPage import DetailsPage


class MainPage(BasePage):
    def __init__(self, driver, request):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()
        self.request = request

    def open_route(self):
        self._click(self.main_page_locators.ROUTE_BUTTON)
        self._wait_for_element(self.main_page_locators.ROUTE_MENU)

    def set_destination(self, **kwargs):
        """
        Setting destination from and to.
        :param kwargs: gets from and to param and uses it to type (from='From location', to='To location')
        :return:
        """
        dest_dict = {
            'dest_from': '',
            'dest_to': ''
        }
        dest_locator = self.main_page_locators.destination_from_to()
        dest_dict.update(kwargs)
        for key, value in dest_dict.items():
            if key in dest_locator:
                self._type(dest_locator[key], Keys.CONTROL, 'A')
                self._type(dest_locator[key], dest_dict[key])

    def set_transport_option(self, transport_option):
        self._click(self.main_page_locators.travel_option(transport_option))

    def search_route(self, transport_option='auto', **kwargs):
        self.set_destination(**kwargs)
        self._click(self.main_page_locators.SEARCH_ROUTE)
        self.set_transport_option(transport_option)

    def open_route_options(self, status_open=True):
        if status_open:
            self._click(self.main_page_locators.OPTIONS_BTN, timeout=20)
            assert self._is_aria_expanded(self.main_page_locators.OPTIONS_BTN)
        else:
            self._click(self.main_page_locators.OPTIONS_BTN, timeout=20)
            assert self._is_aria_expanded(self.main_page_locators.OPTIONS_BTN) is False

    def set_option_unit(self, unit):
        self._click(self.main_page_locators.options_unit(unit))
        assert self._is_option_checked(self.main_page_locators.options_unit_check(unit))

    def set_route_options(self, unit='auto', **kwargs):
        self.open_route_options(True)
        options = {
            'highways': False,
            'tolls': False,
            'ferries': False
        }
        options.update(kwargs)
        for key, value in options.items():
            if value:
                if not self._is_option_checked(self.main_page_locators.avoid_options_check(key)):
                    self._click(self.main_page_locators.avoid_options(key))
            else:
                if self._is_option_checked(self.main_page_locators.avoid_options_check(key)):
                    self._click(self.main_page_locators.avoid_options(key))
        self.set_option_unit(unit)
        options_dict = {
            'highwas': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_HIGH_WAY_CHECK_STATUS),
            'tolls': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_TOOLS_CHECK_STATUS),
            'ferries': self._is_option_checked(self.main_page_locators.OPTIONS_AVOID_FERRIES_CHECK_STATUS),
            'units': unit
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
        self._click(self.main_page_locators.route_id(id))

    def open_details_of_routes(self, id):
        # self._click(self.main_page_locators.route_id(id))
        if not self._is_displayed(self.main_page_locators.DETAIL_PAGE_OPEN, 3):
            self._click(self.main_page_locators.route_id(id))
        assert self._is_displayed(self.main_page_locators.DETAIL_PAGE_OPEN)
        return DetailsPage(self.driver, self.request)

    def get_longest_route(self, all_routes):
        longest_route_distance = 0
        longest_route = ''
        for key, value in all_routes.items():
            distance_value = float(value['distance'].replace('.', '').replace(',', '.').split()[0])
            if distance_value > longest_route_distance:
                longest_route_distance = distance_value
                longest_route = key
        return longest_route, longest_route_distance

    def get_shortest_route(self, all_routes):
        shortest_route_distance = 999999999999999
        shortest_route = ''
        for key, value in all_routes.items():
            distance_value = float(value['distance'].replace('.', '').replace(',', '.').split()[0])
            if distance_value < shortest_route_distance:
                shortest_route_distance = distance_value
                shortest_route = key
        return shortest_route, shortest_route_distance

    def change_direction(self):
        destination_from = self._get_element_value(self.main_page_locators.DESTINATION_FROM)
        destination_to = self._get_element_value(self.main_page_locators.DESTINATION_TO)
        self._click(self.main_page_locators.CHANGE_DIRECTION_BTN)
        assert self._get_element_value(self.main_page_locators.DESTINATION_FROM) == destination_to
        assert self._get_element_value(self.main_page_locators.DESTINATION_TO) == destination_from
