from test_cases.base_test import BaseTest


class TestMainPage(BaseTest):
    def test_budapest_route(self):
        self.main_page.open_route()
        self.main_page.search_route("Belgrade", "Budapest", 'car')

        options = self.main_page.set_route_options(high_way=True, units='km')
        print(options)

        routes = self.main_page.get_suggested_routes()
        print(routes)

        longest_route = self.main_page.get_longest_route(routes)
        print(longest_route)

        self.main_page.select_route(longest_route[0])

        self.main_page.open_one_of_routes(longest_route[0])
        route_info = self.details_page.get_route_info()
        print(route_info)

        self.details_page.click_back_btn()

        self.main_page.change_direction()

        assert route_info['time'] == routes[longest_route[0]]['time']
        assert route_info['distance'] == routes[longest_route[0]]['distance']
        assert route_info['description'] == routes[longest_route[0]]['description']




