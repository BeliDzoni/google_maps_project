import datetime
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
# import edgedriver_autoinstaller
# import geckodriver_autoinstaller
from Pages.DetailsPage import DetailsPage
from Pages.MainPage import MainPage
from Pages.Requests import Requests
from selenium.webdriver.chrome.options import Options
from py.xml import html

@pytest.fixture(scope='function')
def initialize_driver(headless, browser, remote):
    if browser == 'chrome':
        options = driver_options(headless, Options(), browser)
        # chromedriver_autoinstaller.install()
        if remote=='y':
            driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
        else:
            driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = driver_options(headless, webdriver.FirefoxOptions(), browser)
        # geckodriver_autoinstaller.install()
        # executable_path='E:\\chromedirver\\geckodriver.exe'
        if remote=='y':
            driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
        else:
            driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = driver_options(headless, webdriver.edge.options.Options(), browser)
        # edgedriver_autoinstaller.install()
        # executable_path="E:\\chromedirver\\msedgedriver.exe"
        if remote=='y':
            driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
        else:
            driver = webdriver.Edge(options=options)
    else:
        raise Exception('Not good --browser!')

    driver.get('https://www.google.com/maps/')
    driver.maximize_window()
    yield driver
    if not browser == 'firefox':
        driver.close()
    driver.quit()


def driver_options(headless, options, browser):
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
    if 'firefox' not in browser:
        prefs = {
            "translate_whitelists": {"your native language": "en, en_US"},
            "translate": {"enabled": "True"},
            "profile.default_content_setting_values.geolocation": 2
        }
        options.add_experimental_option("prefs", prefs)
    return options

@pytest.fixture(scope="function")
def page_object_init(request, initialize_driver):
    request.cls.details_page = DetailsPage(initialize_driver)
    request.cls.main_page = MainPage(initialize_driver)


@pytest.fixture(scope="function")
def api_setup(request):
    request.cls.request_api = Requests()

@pytest.fixture(scope='session')
def remote(request):
    remote = request.config.getoption('--remote')
    return remote

@pytest.fixture(scope='session')
def headless(request):
    headless = request.config.getoption('--headless')
    return headless


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('--browser')
    return browser


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action='store',
        default='y',
        help="headless: y(default) if wanted to be executed in headless mode"
    )
    parser.addoption(
        "--remote",
        action='store',
        default='y',
        help="remote: y(default) if wanted to be executed remote"
    )
    parser.addoption(
        "--browser",
        action='store',
        default='chrome',
        help="headless: chrome(default), firefox, safari, ie, edge"
    )


def pytest_html_report_title(report):
    now = datetime.datetime.now()
    report.title = "Test Resutlts ("'{}'.format(now.strftime("%Y-%m-%d %H:%M:%S")) + ")"


def pytest_html_results_table_header(cells):
    cells.insert(3, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


#
def pytest_html_results_table_row(cells, report):
    cells.insert(3, html.td(report.time, class_="col-time"))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    report.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if ((report.skipped and xfail) or (report.failed and not xfail)) and ('initialize_driver' in item.funcargs):
            driver = item.funcargs['initialize_driver']
            screenshot = driver.get_screenshot_as_base64()
            html = '<div><img src= "data:image/png;base64, {}" alt=screenshot" style = "width:450px;height=200ph"' \
                   'onclick="window.open("").document.write(this.src.outerHTML)" align="right"/></div>'.format(
                screenshot)
            extra.append(pytest_html.extras.html(html))
            report.extra = extra
