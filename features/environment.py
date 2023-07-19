import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


from app.application import Application
from support.logger import logger


# Allure command:
# python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/amazon_sign_in.feature

# To run behave with allure in terminal, use:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/amazon_search.feature

# To generate report, run: allure serve test_results/

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    # ############################### FIREFOX ######################
    # service = FirefoxService(executable_path='/Users/bill/Desktop/AutomationQA/python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    #  ##############################################################

    # context.driver = webdriver.Safari()

    #### HEADLESS MODE ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(
        options=options,
        service=service)

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")   ### RUN IN GEADLESS MODE WITHOUT A GUI ####
    # chrome_options.add_argument("--disable-gpu")   ### DISABLE GPU ACCELERATION (optional) ####
    # driver = webdriver.Chrome(options=chrome_options)
    #

    #### BROWSERSTACK ####
    # desired_cap = {
    #     'osVersion': '11',
    #     'os': 'Windows',
    #     'sessionName': test_name
    # }
    # options = ChromeOptions()
    # options.set_capability('bstack:options', desired_cap)
    # bs_user = 'evgeniiacherniav_jVcIbo'
    # bs_key = 'NGZYyy2DVmZcKAenn395'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    # browser_init(context)
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)



def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'
        # )

        # Attach a screenshot to Allure report in case the step fails:
        # allure.attach(
        #     context.driver.get_screenshot_as_png(),
        #     name=f'{step.name}.png',
        #     attachment_type=AttachmentType.PNG
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
