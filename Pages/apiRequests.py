from Pages.baseAPI import API


class Requests(API):
    key = "" #https://console.cloud.google.com/apis/credentials get credentials from here
    distance_matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

    def __init__(self):
        super().__init__()

    def get_google_maps_status(self):
        return self._request('https://maps.google.com')[1]

    def get_distance_matrix(self, destination_from, destination_to, **kwargs):
        # https://developers.google.com/maps/documentation/distance-matrix/distance-matrix
        params = {
            "destinations": destination_to,
            "origins": destination_from,
            "key": self.key,
            "alternatives": "",
            "arrival_time": "",
            "departure_time": "now",
            "avoid": "",  # tolls|highways|ferries
            "language": "",
            "mode": "driving",  # driving , walking , bicycling , transit
            "region": "",
            "traffic_model": "",  # best_guess , pessimistic , optimistic
            "transit_mode": "",  # bus, subway, train, tram, rail
            "transit_routing_preference ": "",  # less_walking, fewer_transfers
            "units": "metric",  # metric, imperial
        }
        params.update(kwargs)
        response = self._get(url=self.distance_matrix_url, params=params)
        print(response)
        assert response['destination_addresses']
        assert response['origin_addresses']

        return response

    def get_longest_distance_matrix_route(self, route_dict):
        r = route_dict
        longest_route_distance = 0
        for route in route_dict['rows']:
            for route2 in route['elements']:
                if route2['distance']['value'] > longest_route_distance:
                    longest_route_distance_text = route2['distance']['text']
                    longest_route_time_text = route2['duration']['text']

        return longest_route_distance_text, longest_route_time_text


    def get_shortest_distance_matrix_route(self, route_dict):
        shortest_route_distance = 99999999999999999999999999999999999999
        for route in route_dict['rows']:
            for route2 in route['elements']:
                if route2['distance']['value'] < shortest_route_distance:
                    shortest_route_distance_text = route2['distance']['text']
                    shortest_route_time_text = route2['duration_in_traffic']['text']

        return shortest_route_distance_text, shortest_route_time_text
