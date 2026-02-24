from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

MARKET_BUTTON = (By.CSS_SELECTOR, 'div[wized="loadUser"] a')


@given('open reelly main page')
def open_main_page(context):
   context.app.main_page.open_main_page()


@when('log into page')
def login(context):
   context.app.login_page.login()
   sleep(5)





@when('Click on “market” in the left side menu')
def click_on_market(context):
    sleep(15)
    # context.app.base_page.click(*MARKET_BUTTON)
    market = context.driver.find_elements(*MARKET_BUTTON)
    print(len(market))
    market[6].click()









