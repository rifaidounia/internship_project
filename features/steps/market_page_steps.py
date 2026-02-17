from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

AGENCY_CARDS = (By.CSS_SELECTOR ,'div[class="new-market-description"]')
AGENCY_FILTER = (By.CSS_SELECTOR, 'div[class="new-market-tag active"]')
AGENCY_TAG = (By.CSS_SELECTOR, 'div[class="new-market-card-tag"]')


@when('verify right page open')
 def verify_right_page(context)
    context.app.Market_page.correct_text()


@when('Click on “Agency” filter at the top of the page')
 def click_on_agency(context)
    context.app.base_page.click_on_agency(*AGENCY_FILTER).click()


 @then ('Verify all cards have the “Agency” tag')
   def verify_agency_tag(context)

    cards = context.app.base_page.find_element(*AGENCY_FILTER)
    for card in cards:
        tag = context.app.base_page.find_element(*AGENCY_TAG)
        assert tag is in cards, 'tag not found'

