from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(driver, timeout=10)
        self.base_url = 'https://soft.reelly.io/'

    def open_url(self, end_url=''):
            logger.info(f'Opening URL: {self.base_url}{end_url}')
            self.driver.get(f'{self.base_url}{end_url}')

    def find_element(self, *locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def click(self, *locator):
        logger.info(f'Clicking on element by {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Inputting text {text} to {locator}')
        self.driver.find_element(*locator).send_keys(text)