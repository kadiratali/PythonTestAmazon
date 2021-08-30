from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ScreenShot:

    def __init__(self, browser):
        self.browser = browser

    def every_page_take_screen_shot(self):
        self.browser.save_screenshot("C:/Users/Kadir/Desktop/ScreenShot/test.png")

