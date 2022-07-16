import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from Pages.DetailsPage import DetailsPage
from Pages.MainPage import MainPage
from Pages.Requests import Requests
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = "function")
def setup(request, initialize_driver):
    driver=initialize_driver
    request.cls.driver = driver
    page_object_init(request, driver)
    yield
    driver.close()
    driver.quit()

@pytest.fixture(scope='function')
def initialize_driver(headless):
    options = Options()
    print(headless)
    if headless == 'y':
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--lang=en-US")
    options.add_argument("--arc-disable-locale-sync")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-search-geolocation-disclosure")
    prefs = {
        "translate_whitelists": {"your native language": "en, en_US"},
        "translate": {"enabled": "True"}
    }
    options.add_experimental_option("prefs", prefs)
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/maps/')
    driver.maximize_window()
    return driver

def page_object_init(request, driver):
    request.cls.details_page = DetailsPage(driver)
    request.cls.main_page = MainPage(driver)

@pytest.fixture(scope = "function")
def api_setup(request):
    request.cls.request_api = Requests()


@pytest.fixture(scope='session')
def headless(request):
    headless=request.config.getoption('--headless')
    return headless

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action='store',
        default='y',
        help="headless: y(default) if wanted to be executed in headless mode"
    )


