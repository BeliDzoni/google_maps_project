from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class DetailsPage(BasePage):
    __BACK_BTN = (By.XPATH, '//button[@class="ysKsp"]')
    __ROUTE_INFO = (By.XPATH, "//div[@class='PNEhTd Hk4XGb']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_back_btn(self):
        self._click(self.__BACK_BTN)

    def get_route_info(self):
        route_info=self._get_element_text(self.__ROUTE_INFO).replace(' (','\n').replace(')','').split('\n')
        route_info_dict={}
        route_info_dict['time']=route_info[0]
        route_info_dict['distance'] = route_info[1]
        route_info_dict['description'] = route_info[2]
        route_info_dict['time_with_traffic'] = route_info[3]
        return route_info_dict




