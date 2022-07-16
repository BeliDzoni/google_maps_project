from test_cases.base_test import ApiTest

class TestApi(ApiTest):
    def test_get_google_maps_status(self):
        assert self.request_api.get_google_maps_status()<400