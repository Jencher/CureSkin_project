from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    CART = (By.ID, 'nav-cart-count')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def click_cart_icon(self):
        self.click(*self.CART)


