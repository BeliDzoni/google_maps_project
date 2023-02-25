import pytest
from test_cases.base_test import AllTest

class TestApi(AllTest):

    @pytest.mark.appium
    @pytest.mark.cicd
    @pytest.mark.selenium
    @pytest.mark.all
    # @pytest.mark.parametrize("destination_from,destination_to", [('Novi Sad', "Budapest"), ("Belgrade", "Budapest")], indirect=True)
    def test_budapest_route_appium(self):
        destination_from = "Belgrade"
        destination_to = "Budapest"

        self.appium.start_maps()
        self.appium.search_location(destination_to)
        self.appium.set_destination(from_dest=destination_from)
        time_needed_mobile, distance_mobile = self.appium.get_route_distance()
        print(f"Time needed is {time_needed_mobile}, and distance is {distance_mobile}")
        self.appium.close_maps()

        self.main_page.open_route()
        self.main_page.search_route(transport_option='car', dest_from=destination_from, dest_to=destination_to)

        options = self.main_page.set_route_options(unit='km')
        # print(options)

        routes = self.main_page.get_suggested_routes()
        print(routes)

        shortest_route = self.main_page.get_shortest_route(routes)
        print(shortest_route)

        self.main_page.select_route(shortest_route[0])

        details_page = self.main_page.open_details_of_routes(shortest_route[0])
        route_info = details_page.get_route_info()
        print(route_info)

        details_page.click_back_btn()

        self.main_page.change_direction()

        assert route_info['time'] == routes[shortest_route[0]]['time']
        assert route_info['distance'] == routes[shortest_route[0]]['distance']
        assert route_info['description'] == routes[shortest_route[0]]['description']
        assert route_info['distance'].split()[0] == str(distance_mobile)
        assert route_info['time'].split()[::2] == time_needed_mobile.split()[::2]
