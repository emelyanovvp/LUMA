from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class HomePage(BasePage) :
    def click_link_sign_in_and_go_to_login_page(self):
        self.driver.find_element(*HomePageLocators.SIGN_IN_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def click_link_create_account_and_go_to_regform_page(self):
        self.driver.find_element(*HomePageLocators.CREATE_ACCOUNT_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

