from test_cases.base_test import BaseTest, ApiTest, AppiumTest
import pytest


class TestMainPage(BaseTest):
    @pytest.mark.api
    @pytest.mark.cicd
    @pytest.mark.selenium
    def test_budapest_route2(self):
        assert self.request_api.get_google_maps_status() < 400
        self.main_page.open_route()
        self.main_page.search_route(transport_option='car', dest_from='Budapest', dest_to='Belgrade')

        options = self.main_page.set_route_options(highways=True, unit='km')
        print(options)

        routes = self.main_page.get_suggested_routes()
        print(routes)

        longest_route = self.main_page.get_longest_route(routes)
        print(longest_route)

        self.main_page.select_route(longest_route[0])

        details_page = self.main_page.open_details_of_routes(longest_route[0])
        route_info = details_page.get_route_info()
        print(route_info)

        details_page.click_back_btn()

        self.main_page.change_direction()

        assert route_info['time'] == routes[longest_route[0]]['time']
        assert route_info['distance'] == routes[longest_route[0]]['distance']
        assert route_info['description'] == routes[longest_route[0]]['description']
