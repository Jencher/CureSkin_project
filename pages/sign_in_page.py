from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, 'ap_email')

    def verify_sign_page_open(self):
        query = '/ap/signin'
        self.verify_url_contains_query(query)

    def verify_header(self):
        expected_result = "Sign in"
        # actual_result = self.driver.find_element(*self.SIGNIN_HEADER).text
        # assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'
        self.verify_element_text(expected_result, *self.SIGNIN_HEADER)
        # Verify email field present
        self.driver.find_element(*self.EMAIL)

    def verify_email_is_present(self):
        assert self.driver.find_element(*self.EMAIL).is_displayed(), 'Email field not shown'
