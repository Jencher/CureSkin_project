from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    BOOKS_SUBMENU = (By.CSS_SELECTOR, "[data-category='books']")
    # GROCERY_SUBMENU = (By.CSS_SELECTOR, "[data-category='grocery']")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

        ### Class example (we didn't have verify_element_text() in base Page):
        # actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        # assert expected_result == actual_result, \
         #   f'Error! Expected {expected_result} bot got actual {actual_result}'

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)

    def verify_dept(self, department):
        GROCERY_SUBMENU = (By.CSS_SELECTOR, f"[data-category='{department}']")
        self.wait_for_element_click(*GROCERY_SUBMENU)


