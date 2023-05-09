from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count-container').click()
    sleep(5)


@then('Verify Your Amazon Cart is empty')
def verify_cart_is_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'