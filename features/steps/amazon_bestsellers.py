from behave import given, then
from selenium.webdriver.common.by import By


TOP_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
HEADER = (By.ID, "zg_banner_text")

@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers')

@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    print(len(actual_links))
    assert len(actual_links) == int(expected_links), f'Expected {expected_links}  links, but got {actual_links}'
