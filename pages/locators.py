from selenium.webdriver.common.by import By


class MainPageLocators:
    ELEMENTS_CARD = (By.CSS_SELECTOR, '.category-cards > div:first-of-type')


class ElementsPageLocators:
    CHECK_BOX = (By.CSS_SELECTOR, '#item-1')


class CheckBoxPageLocators:
    HOME = (By.CSS_SELECTOR, '.rct-collapse')
    DOWNLOADS = (By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(3) > span > button')
    WORD_FILE = (By.CSS_SELECTOR, '.rct-node-leaf:first-child > span > label .rct-checkbox')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#result')
