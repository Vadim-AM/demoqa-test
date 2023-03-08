from selenium import webdriver

from pages.checkbox_page import CheckBoxPage
from pages.locators import MainPageLocators, ElementsPageLocators, CheckBoxPageLocators


class TestCheckboxPage:
    MAIN_PAGE_URL = 'https://demoqa.com'
    ELEMENTS_PAGE_URL = 'https://demoqa.com/elements'
    CHECKBOX_PAGE_URL = 'https://demoqa.com/checkbox'

    def test_word_file_checkbox_selected(self, driver: webdriver):
        page = CheckBoxPage(driver, self.MAIN_PAGE_URL)
        page.open()
        assert page.should_be_some_page(self.MAIN_PAGE_URL), f'This is a {driver.get_current.url} page'
        page.find_and_click_element(MainPageLocators.ELEMENTS_CARD)
        assert page.should_be_some_page(self.ELEMENTS_PAGE_URL), f'This is a {driver.get_current.url} page'
        page.find_and_click_element(ElementsPageLocators.CHECK_BOX)
        assert page.should_be_some_page(self.CHECKBOX_PAGE_URL), f'This is a {driver.get_current.url} page'
        page.find_and_click_element(CheckBoxPageLocators.HOME)
        assert page.is_element_present(CheckBoxPageLocators.DOWNLOADS), 'Home directory is not expanded'
        page.find_and_click_element(CheckBoxPageLocators.DOWNLOADS)
        page.find_and_click_element(CheckBoxPageLocators.WORD_FILE)
        assert page.check_success_msg_text(), 'Дooks like the Word File checkbox has not been selected'
