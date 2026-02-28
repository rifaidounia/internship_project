from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

MARKET_BUTTON = (By.CSS_SELECTOR, 'a[href="https://soft.reelly.io"]')
MOBILE_MARKET_BTN = (By.CSS_SELECTOR, 'a[class="relative flex flex-col items-center justify-center gap-1"]')


@given('open reelly main page')
def open_main_page(context):
   context.app.main_page.open_main_page()


@when('log into page')
def login(context):
   context.app.login_page.login()


@when('Click on “market” in the left side menu')
def click_on_market(context):
    sleep(15)
    context.app.base_page.click(*MARKET_BUTTON)


@when('Click on “market” in bottom menu')
def click_on_market_btn(context):
    sleep(15)
    context.app.base_page.click(*MOBILE_MARKET_BTN)












