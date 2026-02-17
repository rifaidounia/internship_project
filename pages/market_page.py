from selenium.webdriver.common.by import By
from pages.base_page import Page

class MarketPage(Page):
    CORRECT_TEXT = (By.CSS_SELECTOR, 'div[class="new-market-h1"]')

    def correct_text(self):
        return self.driver.find_element(*self.CORRECT_TEXT).text


