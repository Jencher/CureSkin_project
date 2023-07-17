from selenium.webdriver.common.by import By
from pages.base_page import Page


class ShopPage(Page):

    def verify_shop_page_opens(self):
        query = 'https://shop.cureskin.com/collections/all'
        self.verify_url_contains_query(query)