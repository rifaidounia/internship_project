from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    Email_field = (By.CSS_SELECTOR, 'input[placeholder="Email"]')
    Password_field = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
    Continue_button = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')

    def login(self):
        sleep(2)
        self.find_element(*self.Email_field).send_keys('rifaidounia988@gmail.com')
        sleep(2)
        self.find_element(*self.Password_field).send_keys('Passport0-')
        sleep(2)
        self.find_element(*self.Continue_button).click()