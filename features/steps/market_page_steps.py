from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

AGENCY_CARDS = (By.CSS_SELECTOR,'div[class="new-market-description"]')
AGENCY_FILTER = (By.XPATH, "//*[@wized='servicesOffersFilterAgency']")
AGENCY_TAG = (By.CSS_SELECTOR, 'div[class="new-market-card-tag"]')
MARKET_TAG = (By.CSS_SELECTOR, 'div[class="new-market-txt-tags"]')


@then('verify right page opens')
def verify_right_page(context):
    context.app.base_page.find_elements(*MARKET_TAG)
    sleep(5)


@when('Click on “Agency” filter at the top of the page')
def click_on_agency(context):
    sleep(5)
    context.driver.find_element(*AGENCY_FILTER).click()
    sleep(5)
    #context.app.base_page.click(*AGENCY_FILTER)


@then ('Verify all cards have the “Agency” tag')
def verify_agency_tag(context):
    cards = context.app.base_page.find_elements(*AGENCY_CARDS)
    expected_tag = "Agency"
    for card in cards:
        tag = context.app.base_page.find_element(*AGENCY_TAG).text
        assert expected_tag in tag, f'Expected tag: {expected_tag} but got: {tag}'

    # if 'Agency' in tag:
    #     pass
    # else:
    #     print(f'Expected tag: {expected_tag} but got: {tag}')