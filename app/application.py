from pages.base_page import Page
from main_page import MainPage
from login_page import LoginPage
from market_page import MarketPage

class application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.market_page = MarketPage(driver)