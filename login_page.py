import time
from .base_page import BasePage
from .my_account_page import MyAccountPage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LoginPage(BasePage):
    def customer_can_put_data_into_login_form_and_sign_in(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys("greg@gmail.com")
        self.driver.find_element(*LoginPageLocators.INPUT_PASS).send_keys("123456GREG&greg")
        self.driver.find_element(*LoginPageLocators.SIGN_IN).click()
        return MyAccountPage(driver=self.driver, url=self.driver.current_url)


