from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    BANNER = (By.ID, 'attach-close_sideSheet-link')

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def close_banner(self):
        self.click(*self.BANNER)