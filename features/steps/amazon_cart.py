from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
EMPTY_CART = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()
   # context.driver.find_element(By.ID,'nav-cart-count-container').click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    # cart_count = context.driver.find_element(*CART).text
    # sleep(5)
    # assert expected_count == cart_count, f'expected {expected_count} items, but got {cart_count}'
    context.app.cart_page.verify_cart_count(expected_count)


@then('Verify cart has {product}')
def verify_product_name(context, product):
    # actual_name = context.driver.find_element(*PRODUCT_NAME).text
    # assert context.product_name[:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'
    context.app.cart_page.verify_cart_has_correct_product(product)


    # part_name = context.product_name[:30]
    # context.app.cart_page.verify_cart_has_correct_product(part_name)



@then('Verify Your Amazon Cart is empty')
def verify_cart_is_empty(context):
    # expected_result = 'Your Amazon Cart is empty'
    context.app.cart_page.verify_cart_is_empty()

   # expected_text = 'Your Amazon Cart is empty.'
    # actual_text = context.driver.find_element(*EMPTY_CART).text
   # assert expected_text == actual_text, \
       # f' Expected {expected_text}, but got {actual_text}'


