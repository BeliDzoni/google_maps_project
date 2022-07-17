from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _get_element_text(self, locator):
        return self._wait_for_element(locator).text

    def _get_elements_text(self, locator):
        return self._wait_for_elements(locator).text

    def _get_element_attribute(self,locator, attribute, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).get_attribute(attribute)

    def _is_option_checked(self, locator):
        if self._get_element_attribute(locator, 'checked')=='true':
            return True
        else:
            return False

    def _is_aria_expanded(self, locator):
        if self._get_element_attribute(locator, 'ariaExpanded')=='true':
            return True
        else:
            return False

    def _get_role_of_element(self, locator):
        return self._get_element_attribute(locator, 'role')

    def _get_element_value(self,locator):
        return self._get_element_attribute(locator, 'value')


    def _wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def _wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


    def _wait_for_animation(self, locator):
        position_1 = self._wait_for_element_to_be_visible(locator).location
        while True:
            position_2=self._wait_for_element_to_be_visible(locator).location
            if position_1==position_2:
                break
            else:
                position_1=position_2

    def _click(self, locator, timeout=10, animation=False):
        element = self._wait_for_element_to_be_visible(locator, timeout)
        if animation:
            self._wait_for_animation(locator)
        for i in range(10):
            if element and element.is_enabled():
                try:
                    return element.click()
                except:
                    continue
            else:
                time.sleep(1)
                continue
        raise TimeoutException

    def _type(self, locator, input_text):
        self._wait_for_element(locator).send_keys(input_text)

    def _is_displayed(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).is_displayed()
        except:
            return False

    def _check_element_text(self, locator, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutError:
            return False

    def _wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def _scroll_to_element(self, locator_role, locator, timeout=120):
        end_time = time.time() + timeout
        element = self._wait_for_element_to_be_visible(*locator_role)
        while True:
            try:
                return WebDriverWait(self.driver, 0).until(EC.visibility_of_element_located(locator)).click()
            except TimeoutException:
                element.send_keys(Keys.END)
                if time.time() > end_time:
                    break
        raise Exception

class API:
    def __init__(self):
        pass

    def _request(self, url):
        try:
            response = requests.head(url)
            return (url, response.status_code)
        except Exception:  # SSL error, timeout, host is down, firewall block, etc.
            print(url, 'ERROR')
            return (url, None)