import pytest
from test_cases.base_test import ApiTest


class TestApi(ApiTest):
    @pytest.mark.api
    @pytest.mark.cicd
    def test_get_google_maps_status(self):
        assert self.request_api.get_google_maps_status() < 400

    @pytest.mark.api
    @pytest.mark.cicd
    def test_get_distance_matrix(self):
        route_dict = self.request_api.get_distance_matrix("Budapest", "Novi Sad")
        longest_distance, longest_time = self.request_api.get_longest_distance_matrix_route(route_dict)
        print(longest_distance)
        print(longest_time)
