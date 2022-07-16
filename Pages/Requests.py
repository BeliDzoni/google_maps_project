from Pages.BasePage import API


class Requests(API):

    def __init__(self):
        super().__init__()

    def get_google_maps_status(self):
        return self._request('https://maps.google.com')[1]

