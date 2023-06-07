from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SEARCH_INPUT = (By.ID,'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
# PRODUCT_RESULT = (By.CSS_SELECTOR, ".s-image[alt='Sponsored Ad - Amazon Basics 6-Piece White Dinner Plate Set']")
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
BANNER = (By.ID, 'attach-close_sideSheet-link')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_button(context):
    # context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    # sleep(2)
    context.app.product_page.click_add_to_cart_btn()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Close Banner')
def close_banner(context):
    # context.driver.find_element(*BANNER).click()
    context.app.product_page.close_banner()


# ['Army Green', 'Black', 'Blue', 'Brown']
@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Burgundy', 'Charcoal Heather', 'Dark Olive', 'Navy',
                       'Brown, Floral Print', 'Golden Yellow',
                       'Green, Dots', 'Hot Pink', 'Light Camel', 'Navy/Pink, Floral Print', 'Soft Violet',
                       'Tan, Cheetah', 'Terracotta', 'Grey Heather, French Stripe', 'Black, French Stripe']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS) # => [WebElement1, WebElement2, WebElement3]

    for color in colors:
        # WebElement2
        color.click() # WebElement2.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'


