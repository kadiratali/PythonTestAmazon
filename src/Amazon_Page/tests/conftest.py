import time

import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:/Users/Kadir/Desktop/chromedriver.exe")
    # wait 10 seconds
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    time.sleep(10)
    # when test is done, close ALL windows of the browser
    browser.quit()
