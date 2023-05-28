from behave import given, then
from selenium.webdriver.common.by import By


TOP_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
# TOP_LINKS = (By.CSS_CELECTOR, "#zg_header a"
HEADER = (By.ID, "zg_banner_text")


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers')


@then('Verify there are {expected_links} top links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    print(len(actual_links))
    assert len(actual_links) == int(expected_links), f'Expected {expected_links}  links, but got {actual_links}'


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'

