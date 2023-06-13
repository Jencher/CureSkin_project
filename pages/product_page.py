from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    BANNER = (By.ID, 'attach-close_sideSheet-link')
    PRODUCT_NAME = (By.ID, 'productTitle')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[aria-label*='New Arrivals']")
    DEALS = (By.CSS_SELECTOR, 'div[id*="subnav-sl-megamenu-8"] .mm-column a.mm-merch-panel ul li h3')

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def close_banner(self):
        self.click(*self.BANNER)

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)

        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(3)

    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS)