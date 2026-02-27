from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #Mobil Web Config#
    mobile_emulation = {
        "deviceName": "Nexus 7"  # Choose a mobile device
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Initialize WebDriver with mobile emulation
    services = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=services, options=options)


    #Firefox#
#    driver_path = GeckoDriverManager().install()
#    service = Service(driver_path)
#    context.driver = webdriver.Firefox(service=service)

    #HEADLESS MODE#
#    options = webdriver.ChromeOptions()
#    options.add_argument('headless')
#    context.driver = webdriver.Chrome(options=options)

    #Browserstack#
    # bs_user = 'douniarifai_YM36D2'
    # bs_key = 'MgYNxwWB9uSy3vu5QPWh'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     "browserVersion" : "latest",
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name,
    #  }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.app = Application(context.driver)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()

#Allur#
#to run allure report the command is
#behave -f allure_behave.formatter:AllureFormatter -o test_results/
#and you have to specify which feature to run so the full command is
#ex: behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/main_page.feature
#then type to generate the report: allure serve test_results/