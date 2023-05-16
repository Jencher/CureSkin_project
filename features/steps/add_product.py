from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_INPUT = (By.ID,'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
PRODUCT_RESULT = (By.CSS_SELECTOR, ".s-image[alt='Sponsored Ad - Amazon Basics 6-Piece White Dinner Plate Set']")
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
BANNER = (By.ID, 'attach-close_sideSheet-link')

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@when('Click on Add to cart button')
def click_add_button(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Close Banner')
def close_banner(context):
    context.driver.find_element(*BANNER).click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    sleep(10)
    assert expected_count == cart_count, f'expected {expected_count} items, but got {cart_count}'