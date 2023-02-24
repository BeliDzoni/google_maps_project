from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _get_element_text(self, locator):
        return self._wait_for_element(locator).text

    def _get_elements_text(self, locator):
        texts = []
        elements = self._wait_for_elements(locator)
        for element in elements:
            texts.append(element.text)
        return texts

    def _get_element_attribute(self, locator, attribute, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).get_attribute(
                attribute)
        except Exception:
            raise Exception(
                "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                    timeout))

    def _is_option_checked(self, locator):
        return self._get_element_attribute(locator, 'checked') == 'true'

    def _is_aria_expanded(self, locator):
        return self._get_element_attribute(locator, 'ariaExpanded') == 'true' or \
            self._get_element_attribute(locator, 'aria-expanded') == 'true'

    def _get_role_of_element(self, locator):
        return self._get_element_attribute(locator, 'role')

    def _get_element_value(self, locator):
        return self._get_element_attribute(locator, 'value')

    def _wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(
                "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                    timeout))

    def _wait_for_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception(
                "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                    timeout))

    def _wait_for_animation(self, locator):
        position_1 = self._wait_for_element_to_be_visible(locator).location
        while True:
            position_2 = self._wait_for_element_to_be_visible(locator).location
            if position_1 == position_2:
                break
            else:
                position_1 = position_2

    def _click(self, locator, timeout=10, scroll=True):
        element = self._wait_for_element_to_be_clickable(locator, timeout)
        if scroll:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def _type(self, locator, *input_text):
        self._wait_for_element(locator).send_keys(*input_text)

    def _is_displayed(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).is_displayed()
        except:
            return False

    def _check_element_text(self, locator, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except:
            return False

    def _wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(
                "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                    timeout))

    def _wait_for_element_to_be_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception:
            raise Exception(
                "Couldn't find element with locator: {} , for time period of: {} secounds\n".format(locator[1],
                                                                                                    timeout))

    def highlight_web_element(self, locator):
        self.driver.execute_script("arguments[0].style.border='2px ridge #33ffff'",
                                   self._wait_for_element_to_be_visible(locator))
