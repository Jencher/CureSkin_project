from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
    PRODUCT = (By.CSS_SELECTOR, ".a-truncate-cut")
    EMPTY_CART = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
    CART = (By.ID, 'nav-cart-count')
    CART_PAGE = (By.ID, 'nav-cart')


    def verify_cart_is_empty(self):
        expected_text = 'Your Amazon Cart is empty'
        self.verify_element_text(expected_text, *self.EMPTY_CART)


    def verify_cart_count(self, expected_count):
        # cart_count = self.driver.find_element(*self.CART).text
        # assert expected_count == cart_count, f'expected {expected_count} items, but got {cart_count}'
        expected_result = expected_count
        self.verify_element_text(expected_result, *self.CART)


    def verify_cart_has_correct_product(self, expected_text):
        # actual_name = self.driver.find_element(*self.PRODUCT_NAME).text
        # assert self.product_name[:30] in actual_name, f'Expected {self.product_name} but got {actual_name}'
        # expected_text = "Plate"
        self.wait_for_element_click(*self.CART_PAGE)
        name = self.find_element(*self.PRODUCT).text
        print(name)


    def verify_product_name(self, part_name):
        self.verify_partial_text(part_name, *self.PRODUCT_NAME)