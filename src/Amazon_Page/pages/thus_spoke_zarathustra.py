from selenium.webdriver.common.by import By


class FriedrichNietzsche:

    def __init__(self, browser):
        self.browser = browser

    # Element Locators
    PlAY_BUTTON = (By.XPATH, "//span[@class='audioListen']")

    # Methods
    def play_button(self):
        self.browser.find_element(*self.PlAY_BUTTON).click()
