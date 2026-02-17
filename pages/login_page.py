from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    Email_field = (By.CSS_SELECTOR, 'input[placeholder="Email"]')
    Password_field = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
    Continue_button = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')

    def login(self):
        self.find_element(*self.Email_field).send_keys('rifaidounia988@gmail.com')
        self.find_element(*self.Password_field).send_keys('Passport0-')
        self.find_element(*self.Continue_button).click()