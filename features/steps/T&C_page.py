from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[target='_blank'][href*='privacy']")
PRIVACY_NOTICE_TEXT = (By.ID, 'GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64')


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_img(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('Verify Amazon Privacy Notice page is opened')
def privacy_notice_page_opened(context):
   assert context.driver.find_element(*PRIVACY_NOTICE_TEXT).text
   sleep(3)


@then('User can close new window and switch back to original')
def close_new_switch_to_old_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    sleep(2)
