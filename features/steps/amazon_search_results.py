from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, "div img.s-image")


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
   # actual_result = context.driver.find_element(*RESULT_TEXT).text
   # assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'
    context.app.search_results_page.verify_search_results(expected_result)


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


#new*

@then('Verify that every product has a name and an image')
def verify_product_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Image is not found'


@then('Verify correct department {department} shown')
def verify_dept(context, department):
    context.app.search_results_page.verify_dept(department)
