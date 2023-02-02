import time
from .base_page import BasePage
from .locators import HomePageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .jackets_women_page import JacketsWomenPage
from selenium.webdriver.common.action_chains import ActionChains
class HomePage(BasePage) :
    def click_link_sign_in_and_go_to_login_page(self):
        self.driver.find_element(*HomePageLocators.SIGN_IN_LINK).click()
        time.sleep(3)
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def click_link_create_account_and_go_to_regform_page(self):
        self.driver.find_element(*HomePageLocators.CREATE_ACCOUNT_LINK).click()
        time.sleep(3)
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def move_mouse_to_women_tops_jackets_link_and_click(self):
        select1 = self.driver.find_element(*HomePageLocators.WOMEN_LINK)
        ActionChains(self.driver).move_to_element(select1).perform()
        select2 = self.driver.find_element(*HomePageLocators.WOMEN_TOPS_LINK)
        ActionChains(self.driver).move_to_element(select2).perform()
        select3 = self.driver.find_element(*HomePageLocators.WOMEN_TOPS_JACKETS_LINK).click()
        time.sleep(3)
        return JacketsWomenPage(driver=self.driver, url=self.driver.current_url)