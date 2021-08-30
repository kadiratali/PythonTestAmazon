import pytest
from src.Amazon_Page.pages.home_page import AmazonHomePage
from src.Amazon_Page.pages.search_result_page import AmazonSearchResultPage
from src.Amazon_Page.pages.thus_spoke_zarathustra import FriedrichNietzsche
from src.Amazon_Page.pages.screen_shot import ScreenShot


@pytest.mark.regressiontest
def test_search_nietzsche(browser):
    home_page = AmazonHomePage(browser)
    search_result_page = AmazonSearchResultPage(browser)
    thus_spoke_zarathustra = FriedrichNietzsche(browser)
    screen_shot = ScreenShot(browser)
    search_item = 'friedrich nietzsche'

    # navigate to Amazon.com home page
    home_page.load_page()

    # verify that web page title is Amazon.com
    home_page.verify_title()

    # search for friedrich nietzsche
    home_page.search_item(search_item)

    # take a screenshot
    screen_shot.every_page_take_screen_shot()

    # verify that web page title contains friedrich nietzsche
    search_result_page.verify_title(search_item)

    # click button
    home_page.search_click(search_item)

    # click book
    search_result_page.click_book()

    # click sound
    thus_spoke_zarathustra.play_button()
