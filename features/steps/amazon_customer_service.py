from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


WELCOME_HEADER = (By.XPATH, "//h1[text()='Welcome to Amazon Customer Service']")
HELP_BOXES = (By.CSS_SELECTOR, ".issue-card-wrapper")
SEARCH_HELP_INPUT = (By.ID, 'hubHelpSearchInput')
SEARCH_HELP_TEXT = (By.XPATH, "//h2[text()='Search our help library']")
ALL_HELP_TOPICS = (By.XPATH, "//h2[text()='All help topics']")
HELP_TOPICS_MENU = (By.CSS_SELECTOR, ".help-topics-list-wrapper")


@given('Open Amazon Customer Service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify Welcome text is visible')
def verify_welcome_text(context):
    expected_result = "Welcome to Amazon Customer Service"
    actual_result = context.driver.find_element(*WELCOME_HEADER).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'


@then ('Verify {expected_boxes} help boxes are displayed')
def verify_boxes(context, expected_boxes):
    expected_boxes = int(expected_boxes)
    actual_boxes = context.driver.find_elements(*HELP_BOXES)
    assert len(actual_boxes) == expected_boxes, f'Expected {expected_boxes}  boxes, but we see {len(actual_boxes)}'


@then('Verify Search our help library text is visible')
def verify_search_help_text(context):
    expected_result = "Search our help library"
    actual_result = context.driver.find_element(*SEARCH_HELP_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'


@then('Verify search help input is presented')
def verify_email_field(context):
    assert context.driver.find_element(*SEARCH_HELP_INPUT).is_displayed(), 'Search help field not shown'


@then('Verify All help topics text is visible')
def verify_search_help_text(context):
    context.driver.find_element(*ALL_HELP_TOPICS)


@then('Verify help topics menu is presented')
def verify_help_menu_presented(context):
    assert context.driver.find_element(*HELP_TOPICS_MENU).is_displayed(), 'Help topics menu is not shown'