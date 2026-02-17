from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

MARKET_BUTTON = (By.CSS_SELECTOR,'a[href="/"]')


@given ('open main page')
 def open_main_page(context)
    context.app.base_page.open_main_page()


@when('login into page')
 def login(context)
    context.app.login_page.login()


@when('click on market on the left side menu')
 def click_on_market(context)
    context.app.base_page.click_on_market(*MARKET_BUTTON).click()








