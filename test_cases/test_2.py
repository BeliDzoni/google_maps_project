import pytest
from test_cases.base_test import ApiTest


class TestApi(ApiTest):
    @pytest.mark.api
    @pytest.mark.cicd
    def test_get_google_maps_status(self):
        assert self.request_api.get_google_maps_status() < 400
