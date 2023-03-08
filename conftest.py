import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request) -> webdriver:
    driver = None
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # run in headless mode
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")  # run in headless mode
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
