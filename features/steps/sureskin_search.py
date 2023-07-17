from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SHOP_BTN = (By.XPATH, "//section[@data-id='51a75f7'] //a[@href='https://shop.cureskin.com/collections/all']")

@given('Open CureSkin main page')
def open_cureskin_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on shop button from footer menu')
def click_shop_button_from_footer_menu(context):
    # context.driver.find_element(*SHOP_BTN).click()
    context.app.footer.click_shop_icon()


@then('Verify Shop page opens')
def verify_shop_page_opens(context):
    # context.driver.wait.until(EC.url_contains('https://shop.cureskin.com/collections/all')
    context.app.shop_page.verify_shop_page_opens()