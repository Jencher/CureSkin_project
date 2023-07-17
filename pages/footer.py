from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Footer(Page):
    SHOP_BTN = (By.XPATH, "//section[@data-id='51a75f7'] //a[@href='https://shop.cureskin.com/collections/all']")

    def click_shop_icon(self):
        self.click(*self.SHOP_BTN)