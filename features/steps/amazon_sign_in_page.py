from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on returns button')
def click_on_returns_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()
    sleep(5)


@then('Verify sign-in text is visible')
def verify_sign_in_text(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'


@then('Verify email field is presented')
def verify_email_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'
