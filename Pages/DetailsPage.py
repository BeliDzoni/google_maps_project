from Pages.BasePage import BasePage
from Pages.locators import DetailsPageLocators


class DetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.details_page_locators = DetailsPageLocators()

    def click_back_btn(self):
        self._click(self.details_page_locators.BACK_BTN)

    def get_route_info(self):
        route_info = self._get_element_text(self.details_page_locators.ROUTE_INFO) \
            .replace(' (', '\n').replace(')', '').split('\n')
        return {'time': route_info[0],
                'distance': route_info[1],
                'description': route_info[2],
                'time_with_traffic': route_info[3]}
