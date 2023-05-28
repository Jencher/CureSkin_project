from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FILED = (By.ID, 'APjFqb')
SEARCH_BTN = (By.XPATH, "//input[@class='gNO89b']")


@given('Open Google main page')
def open_google_main_page(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into Google search field')
def search_google(context, search_word):
    context.driver.find_element(*SEARCH_FILED).send_keys(search_word)


@when('Click Google Search button')
def google_search_click(context):
    # sleep(2)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify Page URL has {search_result} in it')
def verify_page_has_search_word(context, search_result):
    assert search_result in context.driver.current_url, f'Error! {search_result} not in {context.driver.current_url}'