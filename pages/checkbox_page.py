from pages.base_page import BasePage
from pages.locators import CheckBoxPageLocators


class CheckBoxPage(BasePage):
    SUCCESS_TEXT = 'You have selected :\nwordFile'

    def check_success_msg_text(self) -> bool:
        current_text = self.driver.find_element(*CheckBoxPageLocators.SUCCESS_MESSAGE).text
        return current_text == self.SUCCESS_TEXT
