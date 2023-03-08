from selenium import webdriver
from selenium.common import NoSuchElementException


class BasePage:

    def __init__(self, driver: webdriver, url: str, timeout=5) -> None:
        self.driver = driver
        self.url = url
        self.timeout = timeout

    def open(self) -> None:
        self.driver.get(self.url)

    def is_element_present(self, locator: tuple) -> bool:
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_some_page(self, url: str) -> bool:
        return url in self.driver.current_url

    def find_and_click_element(self, locator) -> None:
        self.driver.find_element(*locator).click()
