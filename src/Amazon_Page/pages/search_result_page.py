from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonSearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    # page title

    PAGE_TITLE = 'Amazon.com : '

    # Element Locators
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Go']")
    SEARCH_BOOK = (By.XPATH, "(//img[contains(@alt, 'Thus Spoke Zarathustra')])")

    # Methods

    def search_item(self, item):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(item + Keys.RETURN)

    def verify_title(self, item):
        assert self.browser.title == self.PAGE_TITLE + item

    def click_book(self):
        self.browser.find_element(*self.SEARCH_BOOK).click()
